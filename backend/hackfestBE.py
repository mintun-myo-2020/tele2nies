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

#Function to detect if objects overlap in the image
 
# Returns true if two rectangles(l1, r1)
# and (l2, r2) overlap
def check_overlap(rect1, rect2):
    print(rect1, rect2)
    # To check if either rectangle is actually a line
      # For example  :  l1 ={-1,0}  r1={1,1}  l2={0,-1}  r2={0,1}
       
    if (rect1["top_left"][0] == rect1["bottom_right"][0] or rect1["top_left"][1] == rect1["bottom_right"][1] or rect2["top_left"][0] == rect2["bottom_right"][0] or rect2["top_left"][1] == rect2["bottom_right"][1]):
        # the line cannot have positive overlap
        return False
       
     
    # If one rectangle is on left side of other
    
    if(rect1["top_left"][0] >= rect2["bottom_right"][0] or rect2["top_left"][0] >= rect1["bottom_right"][0]):
        return False
 
    # If one rectangle is above other
    if(rect1["bottom_right"][1] >= rect2["top_left"][1] or rect2["bottom_right"][1] >= rect1["top_left"][1]):
        return False
 
    return True 
# This code is contributed by Vivek Kumar Singh



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
    too_close = []

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
                "bottom_right": (bottom_right.x, bottom_right.y),
                "top_right": (top_right.x, top_right.y),
                "top_left": (top_left.x, top_left.y)
                }
        # for i in range(len(return_objects)):
        #     print(return_objects[i])
        #     if check_overlap(return_objects[i], return_objects[i + 1]): 
        #         too_close.append([return_objects[i], return_objects[i + 1]])


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

