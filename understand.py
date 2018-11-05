import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account


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
for i in range(1,100):								#picture number	
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




