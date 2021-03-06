from __future__ import print_function

from google.cloud import vision

import os

image_uri = 'gs://cloud-samples-data/vision/using_curl/shanghai.jpeg'

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key.json"

client = vision.ImageAnnotatorClient()
image = vision.Image()
image.source.image_uri = image_uri

response = client.label_detection(image=image)

print('Labels (and confidence score):')
print('=' * 30)
for label in response.label_annotations:
    print(label.description, '(%.2f%%)' % (label.score*100.))