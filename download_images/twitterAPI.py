# -*- coding: utf-8 -*-
# ffmpeg命令: ffmpeg -f image2 -i d:/downloadIMAGES/%d.jpg -vcodec libx264 -r 25 -b 2000k test.mp4
"""
Created on Wed Sep 26 10:19:23 2018

@author: sjqgo
"""
import tweepy
from tweepy import OAuthHandler
import json
import wget 
import os
consumer_key = 'X8C7TcTQ02ko5aO7H57wlFQB5'
consumer_secret = 'VxDFXs7o4vJunY8tGSSjSRNsETrVQCj9dpLR89FDFRG2ciFnw7'
access_token = '1034472972273299456-P0HZdo1AqNaUKMM9CBbZsuzXI1cCGQ'
access_secret = 'TJOA8hBis0rsuWxzvmIVPX3ra2nfyuMjuWXz4rEDvKyKj'
target =  'nba'
num = 100
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
print(path)        
i=1        
for media_file in media_files:
    if(i<num):
        i=i+1
        wget.download(url=media_file,out="D:\downloadIMAGES\\"+filenum[i-1]+".jpg")
    else:
        break;
            
        