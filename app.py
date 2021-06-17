#!/usr/bin/env python
import os
import sys

from flask import Flask, request, jsonify, send_file, render_template
from io import BytesIO #used to help file-related input and output operations
from  import Image, ImageOps #PILLOW is usd for data processing
import base64 #used to encode binary file such as image with script
import urllib #used to read the url in python

import numpy as np #used for working with array
import scipy.misc  #it is used the python imaging library to read the image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os
import tensorflow as tf #used to develop and train models using python and deploy it in cloud or database
import numpy as np
from tensorflow import keras #used to provide the python interface for ANN
from skimage import io #used for input output processing
from tensorflow.keras.preprocessing import image


# Flask utils
from flask import Flask, redirect, url_for, request, render_template #used for web development
from werkzeug.utils import secure_filename #it returns the secure vesion of file
from gevent.pywsgi import WSGIServer #it is used to handl many request concurrently
from tensorflow.keras.models import load_model #used for loading image in webdesk



app = Flask(__name__)
MODEL_PATH ='model.h5'

# Load your trained model
model = load_model(MODEL_PATH)

def model_predict(img_path, model):
    img = image.load_img(img_path, grayscale=False, target_size=(64, 64))
    show_img = image.load_img(img_path, grayscale=False, target_size=(64, 64))
    x = image.img_to_array(img) #Converts a PIL Image instance to a Numpy array.
    x = np.expand_dims(x, axis=0)
    x = np.array(x, 'float32') #converted the elements to float32
    x /= 255
    preds = model.predict(x)
    return preds
	
@app.route("/")
@app.route('/first')
def first():
	return render_template('first.html')

@app.route('/abstract')
def abstract():
	return render_template('abstract.html')

@app.route('/future')
def future():
	return render_template('future.html')    

@app.route('/login')
def login():
	return render_template('login.html')
@app.route('/pie')
def pie():
	return render_template('pie.html')
@app.route('/chart')
def chart():
	return render_template('chart.html')    




@app.route("/index",methods=['GET'])
def index():
	return render_template('index.html')


@app.route("/upload", methods=['POST'])
def upload_file():
	print("Hello")
	try:
		img = Image.open(BytesIO(request.files['imagefile'].read())).convert('RGB')
		img = ImageOps.fit(img, (224, 224), Image.ANTIALIAS)
	except:
		error_msg = "Please choose an image file!"
		return render_template('index.html', **locals())

	# Call Function to predict
	args = {'input' : img}
	out_pred, out_prob = predict(args)
	out_prob = out_prob * 100

	print(out_pred, out_prob)
	danger = "danger"
	if out_pred=="You Are Safe, But Do keep precaution":
		danger = "success"
	print(danger)
	img_io = BytesIO()
	img.save(img_io, 'PNG')

	png_output = base64.b64encode(img_io.getvalue())
	processed_file = urllib.parse.quote(png_output)

	return render_template('result.html',**locals())

def predict(args):
	img = np.array(args['input']) / 255.0
	img = np.expand_dims(img, axis = 0)

	model = 'covid_model_v4.h5'
	# Load weights into the new model
	model = load_model(model)

	pred = model.predict(img)

	if np.argmax(pred, axis=1)[0] == 1:
		out_pred = 'You Are Safe, But Do keep precaution'
	else:
		out_pred = 'You may have Coronavirus'

	return out_pred, float(np.max(pred))
@app.route('/second', methods=['GET'])

#used for ct scan
def second():
    # Main page
    return render_template('second.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        print(preds[0])

        # x = x.reshape([64, 64]);
        disease_class = ['Covid-19','Non Covid-19']
        a = preds[0]
        ind=np.argmax(a)
        print('Prediction:', disease_class[ind])
        result=disease_class[ind]
        return result
    return None    

if __name__ == '__main__':
    app.run(debug=True)

