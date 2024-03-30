import sys
import os, shutil
import glob
import re
import numpy as np
import cv2
import math

from flask import Flask,flash, request, render_template,send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='')
app.secret_key = os.urandom(24)

app.config['DEBLURRED_FOLDER'] = 'deblurred_images'
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/uploads/<filename>')
def upload_img(filename):
    
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/deblurred_images/<filename>')
def deblurred_img(filename):
    
    return send_from_directory(app.config['DEBLURRED_FOLDER'], filename)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['DEBLURRED_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
        app.run(debug=True, host="localhost", port=3060)
