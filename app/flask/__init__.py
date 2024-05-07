from flask import Flask

def create_app():

    app = Flask(__name__)

    from app.views.main import main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    return app




from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{username}:{password}@{host}:{port}/{database}'.format(
        #username=os.environ['RDS_USERNAME'],
        #password=os.environ['RDS_PASSWORD'],
        #host=os.environ['RDS_HOSTNAME'],
        #port=os.environ['RDS_PORT'],
        #database=os.environ['RDS_DB_NAME'],
    #)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://image_app:im4g3_4pp@localhost/image'

    # connect the app to the database
    db.init_app(app)

    from app.views.main import main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    return app
