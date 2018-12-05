# -*- coding: utf-8 -*-
# ffmpeg command: ffmpeg -f image2 -i d:/downloadIMAGES/%d.jpg -vcodec libx264 -r 25 -b 2000k test.mp4
"""
Created on Wed Sep 26 10:19:23 2018

@author: sjqgo
"""
import tweepy
from tweepy import OAuthHandler
import json
import wget 
import os
import io
from google.cloud import storage
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account
import pymysql.cursors
import pymongo
import shutil
from datetime import datetime

consumer_key = 'X8C7TcTQ02ko5aO7H57wlFQB5'
consumer_secret = 'VxDFXs7o4vJunY8tGSSjSRNsETrVQCj9dpLR89FDFRG2ciFnw7'
access_token = '1034472972273299456-P0HZdo1AqNaUKMM9CBbZsuzXI1cCGQ'
access_secret = 'TJOA8hBis0rsuWxzvmIVPX3ra2nfyuMjuWXz4rEDvKyKj'
target =  'CityOfBoston'			#enter ur twitter id
num = 50					#enter downloaded picture number


#connection to mysql database
#enter mysql config
mysql_connection = pymysql.connect(host='127.0.0.1',
						    user='root',
                            password='sjq_mysql',
                            db='sql_mini3',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)



#enter mongo config
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = myclient["mongo_mini3"]
mongo_col = mongo_db['twitter']




num = num+1
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status
 
# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
# User() is the data model for a user profil
tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse
# You need to do it for all the models you need
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


tweets = api.user_timeline(screen_name=target,
                           count=200, include_rts=False,
                           exclude_replies=True)





tweets = api.user_timeline(screen_name=target,
                           count=200, include_rts=False,
                           exclude_replies=True)
last_id = tweets[-1].id
 
while (True):
    more_tweets = api.user_timeline(screen_name=target,
                                count=200,
                                include_rts=False,
                                exclude_replies=True,
                                max_id=last_id-1)
# There are no more tweets
    if (len(more_tweets) == 0):
        break
    else:
        last_id = more_tweets[-1].id-1
        tweets = tweets + more_tweets
      
      
      
media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])
        
  



filenum=[]
for i in range(num):
    filenum.append(str(i))





path = os.getcwd()
if os.path.isdir("D:\\downloadIMAGES"):
	shutil.rmtree("D:\\downloadIMAGES")
os.mkdir('D:\\downloadIMAGES')

i=1
for media_file in media_files:
	if(i<num):
		i=i+1
		wget.download(url=media_file,out="D:\\downloadIMAGES\\"+filenum[i-1]+".jpg")
	else:
		break;





# convert pictures to a video
ffmpegstr = 'ffmpeg -y -f image2 -i d:/downloadIMAGES/%d.jpg -vcodec libx264 -r 25 -b 2000k ' + target +'.mp4'
print(ffmpegstr)
os.system(ffmpegstr)



client = vision.ImageAnnotatorClient()



# Explicitly use service account credentials by specifying the private key
# file.
storage_client = storage.Client.from_service_account_json(
       'D:/googleAPI/google_vision.json')              #input the location of your json file

# Make an authenticated API request
buckets = list(storage_client.list_buckets())


current_labels=[]	
# The name of the image file to annotate
string='D:downloadIMAGES/'
for i in range(1,num):                              
    file_name = os.path.join(
      os.path.dirname(__file__),
      'D:/downloadIMAGES/'+str(i)+'.jpg')           #input your download folder

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
      content = image_file.read()

    image = types.Image(content=content)

# Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations			#store labels

    same=0
    for a in labels:
        for b in current_labels:
            if a.description==b:
                same=1
                break
            else:
                same=0
            
        if same==0:
            current_labels.append(a.description)
            #write to mysql db
            try:
                with mysql_connection.cursor() as cursor:
                	# Create a new record
                	#sql = "INSERT INTO `sql_mini3` (`twitter_id`, `label`,`time`) VALUES (%s, %s,%s)"
                    sql = 'INSERT INTO sql_mini3(twitter_id, label, time) VALUES (%s,%s,%s)'
                    cursor.execute(sql, (target, a.description, datetime.now()))

	    # connection is not autocommit by default. So you must commit to save
	    # your changes.
                mysql_connection.commit()

            finally:
                sql = 1




            #write to mongo db
            mongo_dict = {"twitter_id":target,"label":a.description,'time':datetime.now()}
            mongo_col.insert_one(mongo_dict)
            print('insert:',mongo_dict)





b=1








mysql_connection.close()
print('this video is about:')
for a in sorted(current_labels):
    if b>4:
        b=1
        print(a)

    else:
        b=b+1
        print(a,end=';')








# Instantiates a client
client = vision.ImageAnnotatorClient()

from google.cloud import storage

    # Explicitly use service account credentials by specifying the private key
    # file.
storage_client = storage.Client.from_service_account_json(
        'D:/googleAPI/google_vision.json')

    # Make an authenticated API request
buckets = list(storage_client.list_buckets())


current_labels=[]
# The name of the image file to annotate
string='D:downloadIMAGES/'
for i in range(1,num):                              #picture number 
    file_name = os.path.join(
      os.path.dirname(__file__),
      'D:/downloadIMAGES/'+str(i)+'.jpg')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
      content = image_file.read()

    image = types.Image(content=content)

# Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    same=0
    for a in labels:
        for b in current_labels:
            if a.description==b:
                same=1
                break
            else:
                same=0
            
        if same==0:
            current_labels.append(a.description)

b=1





print('this video is about:')
for a in sorted(current_labels):
    if b>4:
        b=1
        print(a)

    else:
        b=b+1
        print(a,end=',')