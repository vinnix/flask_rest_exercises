

# import imghdr # XXX: Deprecated at this version of python I'm using
from PIL import Image # XXX: Replacement for `imghdr`
import os
from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory
from werkzeug.utils import secure_filename



port = 5100

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif','.jpeg']
app.config['UPLOAD_PATH'] = 'upload'

def validate_image(stream):
    image = Image.open(stream)
    format = image.format()
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')



@app.route('/up/submit')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('submit.html', files=files)

@app.route('/up/submit', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']: # \ or file_ext != validate_image(uploaded_file.filename): ### XXX: Include actual datatype validation using PIL
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return redirect(url_for('index'))

@app.route('/upload/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)

