
import logging


from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
from flask import send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from flask import Flask, render_template, request
import sys
import os
import json
import binascii

from model import Base,Car, CarsList, insert_car


#############################################################################
# Open Flask Framework and Define Port
#############################################################################
UPLOAD_FOLDER = './upload'
app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://image_app:im4g3_4pp@localhost/image'
app_port = 5100

# Port number can be overrided

if sys.argv.__len__() > 1:
    app_port = sys.argv[1]
print("Api running on port: {} ".format(app_port))

# Configure Flask logging
app.logger.setLevel(logging.INFO)  # Set log level to INFO
handler = logging.FileHandler('experiments.log')  # Log to a file
app.logger.addHandler(handler)

# Parsing options
parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('carname', type=str, required=True, help="car name is a required parameter!")
parser.add_argument('company', type=str, required=True, help="company required parameter!")
parser.add_argument('picture', type=bytes, required=False, help="picture of a car!")


#############################################################################
# SQLAlchemy and Flask integration
#############################################################################

api = Api(app)
db = SQLAlchemy( model_class=Base)


#############################################################################
# App exceptions
#############################################################################
@app.errorhandler(500)
def server_error(error):
    app.logger.exception('An exception occurred during a request.')
    return 'Internal Server Error', 500



#############################################################################
# Using distinct style on Flask allowing integration of a class
# and its method, get to integrate with RESTFUL API calls
#############################################################################
class topic_tags(Resource):
        def get(self):
            return {'hello': 'world world'}

# Associating API with path
api.add_resource(topic_tags,'/topics')

#############################################################################
# Using distinct style on Flask allowing integration of a class
# and its method, get to integrate with RESTFUL API calls
#############################################################################
class test_db(Resource):
        def get(self):
            return {'testing': 'database'}

#
# Associating API with path
#
api.add_resource(test_db,'/db')
api.add_resource(CarsList, '/cars')
api.add_resource(Car, '/car/<record_id>')

#############################################################################


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return render_template('upload.html',msg="there is no file in form!")
        file_data = request.files['file1']
        json_data=request.form.get("json_data")
        jd = json.loads(json_data)

        insert_car(jd['carname'],jd['company'],file_data.read())
        return render_template('upload.html',msg="upload done!")
    return render_template('upload.html',msg="there is no file in form!")


@app.route('/ui/<path:path>')
def send_report(path):
        return send_from_directory('ui', path)


@app.route('/multi_add', methods=['POST'])
def multi_add():
    if request.headers['Content-Type'].startswith('multipart/form-data'):
        app.logger.info('multi-form data')
        json_data=request.form.get("json_data")
        jd = json.loads(json_data)
        file_data=request.files['file']

        insert_car(jd['carname'],jd['company'],file_data.read())
        return "200 Ok" 


#############################################################################
# Main block to initially 
#############################################################################

if __name__ == '__main__':
    ## This initialize/create tables and databases based on the DB Model 
    ## if not created already
    with app.app_context():
        db.init_app(app)
        db.create_all()
    app.run(host="0.0.0.0", port=app_port, debug=True)



