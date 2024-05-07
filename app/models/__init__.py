
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


#############################################################################
# SQLAlchemy and Flask integration
#############################################################################

class Base(DeclarativeBase):
      pass

db = SQLAlchemy(model_class=Base)

class CarRecord(db.Model):
    __tablename__ = 'car'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, nullable=False)
    carname: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    company: Mapped[str] = mapped_column(db.String, unique=False, nullable=False)
    picture: Mapped[bytes] = mapped_column(db.LargeBinary, unique=False, nullable=True)

    def serialize(self):
        if self.picture != None:
            img = binascii.b2a_base64(self.picture).decode().rstrip('\n')
        else:
            img = '<image-empty>' # breaks brower
            img = 'iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIAQMAAAD+wSzIAAAABlBMVEX///+/v7+jQ3Y5AAAADklEQVQI12P4AIX8EAgALgAD/aNpbtEAAAAASUVORK5CYII' # elegant empty

        return {
            'id': self.id,
            'carName': self.carname,
            'company': self.company,
            'picture': img
        }


#############################################################################
class CompanyRecord(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    companyname: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'companyName': self.companyname
        }

#############################################################################
#
#############################################################################

class CarsList(Resource):
    def get(self):
        records = CarRecord.query.all()
        return [CarRecord.serialize(record) for record in records]

    def post(self):
        args = parser.parse_args()
        car_record = CarRecord(carname=args['carname'], company=args['company'])
        db.session.add(car_record)
            
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            if "UNIQUE constraint failed: car.carname" in str(err):
                return False, "error, username already exists (%s)" % username
            elif "FOREIGN KEY constraint failed" in str(err):
                return False, "supplier does not exist"
            elif "duplicate key value violates unique constraint" in str(err):
                #app.logger.info('')
                #app.logger.debug('')
                #app.logger.warning('')
                #app.logger.error('')
                errm = "[CRITICAL] Duplicate key error (%s)" % (err)
                app.logger.critical(errm)

                return False, "Duplicate key"
            else:
                return False, "unknown error adding user"

        try:
            return [CarRecord.serialize(car_record)] , 201
        except AttributeError as err:
            errm = "[CRITICAL] Attribute ID unable to serialize" 
            app.logger.critical(errm)
            return "Insert failed",422

#############################################################################
#
#############################################################################
class Car(Resource):
    def put(self, record_id):
        args = parser.parse_args()
        record = CarRecord.query.filter_by(id=record_id)\
            .first_or_404(description='Record with id={} is not available'.format(record_id))
        record.carname = args['carname']
        record.company = args['company']
        db.session.commit()
        return CarRecord.serialize(record), 201


    def delete(self, record_id):
        record = CarRecord.query.filter_by(id=record_id)\
            .first_or_404(description='Record with id={} is not available'.format(record_id))
        db.session.delete(record)
        db.session.commit()
        return '', 204


#############################################################################
#
#############################################################################


#
#
def insert_car(name,company,picture):
    with app.app_context():
        db.session.add(CarRecord(carname=name, company=company, picture=picture))
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            if "UNIQUE constraint failed: car.carname" in str(err):
                return False, "error, username already exists (%s)" % username
            elif "FOREIGN KEY constraint failed" in str(err):
                return False, "supplier does not exist"
            elif "duplicate key value violates unique constraint" in str(err):
                #app.logger.info('')
                #app.logger.debug('')
                #app.logger.warning('')
                #app.logger.error('')
                errm = "[CRITICAL] Duplicate key error (%s)" % (err)
                app.logger.critical(errm)

                return False, "Duplicate key"
            else:
                return False, "unknown error adding user"

        cars = db.session.execute(db.select(CarRecord)).scalars()
        return cars




