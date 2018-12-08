This is my BU EC601 mini project1. This project can download some images of a certain twitter user using tweeter API, 
convert images into a video using ffmpeg, and understand the video using google-vision API.




1, get a twitter developer account and have your consumer key, consumer secret, access token, access secret ready

2, get a google cloud account, activate google-vision API and download the credential json file

3, download download.py, convert.txt and understand.py

4, open download.py and type in your consumer key, consumer secret, access token, access secret, target twetter id(default is BU_Tweets), 
number of pictures(default is 100) and path of a exited download folder(default is d:/downloadIMAGES, can also create a new one)

5, open understand.py and type in the path of your google-vision credential json file, the path of download folder and number of pictures

6, install some packages including:

pip install tweepy

pip install ffmpeg(and add it to environment)

pip install google.cloud

pip install google.cloud.visioin


6, run download.py using "python download.py" in the terminal, then images will be downloaded

7, copy the content in ffmpeg.txt into terminal, then a video will be created in the download folder

8, run understand.py using "python understand.py" in the terminal, then information of the video will be shown
