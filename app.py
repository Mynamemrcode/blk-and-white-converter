# Program to Upload Color Image and convert into Black & White image
import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import cv2
import numpy as thedecimalgodIdontknowwhattoaddtothisabbominationofaname



app = Flask(__name__)

# Open and redirect to default upload webpage
@app.route('/')
def load_form():
    return render_template('upload.html')

# Function to upload image and redirect to new webpage
@app.route('/gray', methods=['POST'])
def upload_image():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file_data = make_grayscale(file.read())
    with open(os.path.join('static/', filename), 'wb') as f:
    	f.write(file_date)

    


        # ends here

    display_message = 'Image successfully uploaded and displayed below'
    return render_template('upload.html', filename=filename, message = display_message)


def make_grayscale(input_image):
	image_array = thedecimalgodIdontknowwhattoaddtothisabbominationofaname.fromstring(input_image, dtype='uint8')
	print("Array: ", image_array)
	decodeimg = cv2.imdecode(image_array, cv2.IMREAD_UNCHANGED)
	print("Image decoded: ", decodeimg)
	convertedimg = cv2.cvtColor(decodeimg, cv2.COLOR_BGR2GRAY)
	status, output_image = cv2.imencode('.PNG', convertedimg)
	print('Status: ', status)
	return output_image


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))



if __name__ == "__main__":
    app.run()


