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

# flask stuffs
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# API endpoint for GET request (to get potential hazards)
# should receive a base64 string as input
@app.route("/get_labels", methods=['GET'])
def get_labels():

    data = request.json
    imgdata = base64.b64decode(data) #might need to edit to parse the correct stuff

    image = vision.Image(content=imgdata)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    return_labels = []
    # print('Labels:')
    # for label in labels:
    #     print(label.description)

    try:
        for label in labels:
            return_labels.append(label)
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": "something wrong get_labels"
            }
        ), 500

    return jsonify(
        {
            "code": 200,
            "data": return_labels
        }
    ), 201

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000, debug=True)

