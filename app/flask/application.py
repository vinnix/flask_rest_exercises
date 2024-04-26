
from PIL import Image
import os
from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename



port = 5100

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')

app.config['MAX_CONTENT_LENGTH'] = 1500 * 1500
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif','.jpeg']
app.config['UPLOAD_PATH'] = 'upload'


#class topic_tags(Resource):
        #def get(self):
            #return {'hello': 'world world'}

# Associating API with path
#api.add_resource(topic_tags,'/topics')



# Error handling if file is above the limit
# 
@app.errorhandler(413)
def too_large(e):
        return "File is too large", 413


# Index.html used for redirect in an attempt for refreshing after upload
#
@app.route('/')
def root():
    return render_template('index.html')

# Used to retrive the file from the directory
# and allow GET method to pass it to the browser
@app.route('/upload/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)



# Show upload form and list files in the directory 
#
@app.route('/api/submit')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('submit.html', files=files)



# Open file coming from request, resize and save it
# This uses Image from PIL, which also verify file sanity
def upload_check_resize_image(post_image, filename):
    basedir = os.path.abspath(os.path.dirname(__file__))
    with Image.open(post_image) as new_image:
        image = new_image.resize((1500, 1500))
        image.save(os.path.join(basedir, app.config['UPLOAD_PATH'], filename))

# Function that accepts REST api-call for handling and saving the file
# It does perform some checks (i.e.: valid extensions) and pass
# the call to the function upload_check_resize_image which
# not only resizes but by opening the image validates the file content
@app.route('/api/submit', methods=['POST','PUT'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    
    # redirect to index if filename is empty OR SAVE IT
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        # abort if not in the allowed extensions
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)

        # Self-explanatory, however, simplyfing the process
        # now we are using a function which open the image
        # resize it to 1500x1500 defined in the exercise
        # presuming height with also 1500
        upload_check_resize_image(uploaded_file,filename)

    # If no errors presented redirect to index() function
    # XXX: Not reloading the page after upload
    #return redirect(url_for('root'))
    return '',204




#
#
# MAIN BLOCK
#
#
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)

