from ultralytics import YOLO
from annotator import annotate_image
import cv2
from flask import Flask, request, jsonify, current_app
from flask_cors import CORS, cross_origin
import numpy as np
import base64
import json
import torch




app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def readb64(uri):
   """
   Returns cv2 image from base64 input uri.
   """
   encoded_data = uri.split(',')[1]
   nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
   img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
   return img

def encode_image(image):
    """
    Returns base64 encoded version of image.
    """
    _, encoded_image = cv2.imencode('.jpg', image)
    encoded_string = base64.b64encode(encoded_image).decode('utf-8')
    
    return encoded_string

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    # Get the uploaded image from the request.
    image = json.loads(request.data)['image']
    image = readb64(image)
    
    raw_result = annotate_image(image, current_app.model)
    
    encoded_image = encode_image(image)
    # Format the prediction results into a response object.
    response = {
        'image':encoded_image,
        'raw_result':raw_result
    }

    # Return the response object as JSON
    return jsonify(response)

if __name__ == '__main__':
    with app.app_context():
        print('Loading YOLO model...')
        #Load model once on app launch for future use.
        current_app.model = YOLO("yolov8n.pt")
        if torch.cuda.is_available():
            current_app.model.to('cuda')
    app.run(host='0.0.0.0')




