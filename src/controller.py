#controller setup
from flask import Blueprint, request, Response
from flask_cors import CORS, cross_origin

#dependencies
import os
import json

import numpy as np

from tensorflow import keras

import traceback
import numpy as np
from PIL import Image

# function calls
from src.img_classifier.classifier import classify

# ---- Loading model ----
model = keras.models.load_model('./DepMod')


# --- initializing blueprint ----
process = Blueprint('process', __name__)


#______________________CLASSIFIER_____________________
#####################################################


@process.route('/classify', methods=['POST'])
@cross_origin()
def image_parser():
    try:

        if 'image' not in request.files:
            return Response(
                response=json.dumps({"error": "Missing image file"}),
                status=400,
                mimetype="application/json"
            )

        else:  
            if not os.path.exists('static'):
                os.makedirs('static')  

            img = Image.open(request.files['image'])
            img_path = "./static/processing.jpg"
            img.save(img_path)
            
            try:
                resp = classify(img_path, model)
            except Exception as e:
                resp = e

        return Response(response = json.dumps(resp),
            status=200,
            mimetype="application/json")
        
    except Exception as e:
        resp = {
            "status": "FAIL",
            "message": str(e),
            "result": {}
        }

        return Response(response=json.dumps(resp),
            status=400,
            mimetype="application/json"
        )