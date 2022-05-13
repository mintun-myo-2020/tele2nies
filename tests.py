import os, io
from google.cloud import vision
from PIL import Image
import requests
from flask import Flask, request, jsonify
import base64
from io import BytesIO

# Set the correct env variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.JSON'

# Instantiate a client
client = vision.ImageAnnotatorClient()

#Function to detect the objects in an image
def detect_objects(image_source):
    pass

# API endpoint for GET request (to get potential hazards)
# The name of the image file to annotate
file_name = os.path.abspath('resources/wakeupcat.jpg')


# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)

# image manipulation
with open("resources/wakeupcat.jpg", "rb") as image_file:
    imgstring = base64.b64encode(image_file.read())

imgdata = base64.b64decode(imgstring)
im = Image.open(BytesIO(imgdata))
image = vision.Image(content=imgdata)
# Performs label detection on the image file
response = client.label_detection(image=image)
labels1 = response.label_annotations
print('Labels:')
for label in labels1:
    print(label.description)
im.show()