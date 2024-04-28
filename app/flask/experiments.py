from flask import Flask, request
from flask_restful import Resource, Api
from flask import send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from flask import Flask, render_template, request
import sys
import os











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



#############################################################################
# SQLAlchemy and Flask integration
#############################################################################

class Base(DeclarativeBase):
      pass

db = SQLAlchemy(app, model_class=Base)
api = Api(app)

class Car(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    carname: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)



def insert_car():
    with app.app_context():
        db.create_all()
        db.session.add(Car(carname="Beetle3"))
        db.session.add(Car(carname="Camaro3"))

        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            if "UNIQUE constraint failed: car.carname" in str(err):
                return False, "error, username already exists (%s)" % username
            elif "FOREIGN KEY constraint failed" in str(err):
                return False, "supplier does not exist"
            else:
                return False, "unknown error adding user"


        cars = db.session.execute(db.select(Car)).scalars()
        return cars


insert_car()


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

# Associating API with path
api.add_resource(test_db,'/db')


#############################################################################


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        return path

        return 'ok'
        return '''
        <h1>Upload new File</h1>
        <form method="post" enctype="multipart/form-data">
        <input type="file" name="file1">
        <input type="submit">
        </form>
        '''




@app.route('/ui/<path:path>')
def send_report(path):
        return send_from_directory('ui', path)




#############################################################################
# Main block to initially 
#############################################################################

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=app_port)



