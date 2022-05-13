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
def detect_objects(image):
    pass

# flask stuffs
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# API endpoint for GET request (to get potential hazards)
# should receive a base64 string as input
@app.route("/get_labels", methods=['GET'])
def get_labels():

    data = request.get_json()
    base64_img = data['img']
    imgdata = base64.b64decode(base64_img) #decode the encoded img back into image
    image = vision.Image(content=imgdata)
    objects = client.object_localization(image=image).localized_object_annotations
    return_objects = {}

    try:
        for object in objects:
            name = object.name
            bounding_poly = object.bounding_poly.normalized_vertices
            bottom_left = bounding_poly[0]
            bottom_right = bounding_poly[1]
            top_right = bounding_poly[2]
            top_left = bounding_poly[3]

            return_objects[name] = {
                "name": name, 
                "bottom_left": (bottom_left.x, bottom_left.y),
                "botton_right": (bottom_right.x, bottom_right.y),
                "top_right": (top_right.x, top_right.y),
                "top_left": (top_left.x, top_left.y)
                }

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
            "data": return_objects
        }
    ), 201

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000, debug=True)

