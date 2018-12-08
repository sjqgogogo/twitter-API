This is my BU EC601 mini project3. This project is based on my mini project1, which can download some images of a certain twitter user using twitter API, convert images into a video using ffmpeg, and understand the video using google-vision API. In this project, I add database support including mySQL and mongoDB, which can store relative information into database when someone uses mini3.py.


Here is how to test my code.

1, get a twitter developer account and have your consumer key, consumer secret, access token, access secret ready

2, get a google cloud account, activate google-vision API and download the credential json file

3, open mini3.py and type in your consumer key, consumer secret, access token, access secret, target twetter id(default is BU_Tweets), 
number of pictures(default is 100) and the path of download folder(default is d:/downloadIMAGES,you can choose a new one as well), and type in the path of your google-vision credential json file, and your database configuration.

4, install some packages including:

pip install tweepy

pip install ffmpeg
(and add it to environment)

pip install google.cloud

pip install google.cloud.visioin


5, run mini3.py

6, you can use functions in twitter_mongo.py and twitter_mysql.py to check the database.
