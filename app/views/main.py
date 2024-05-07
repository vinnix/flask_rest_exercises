from flask import Blueprint, request, jsonify
from app import db
from app.models.People import People
from datetime import datetime

main_bp = Blueprint('main', __name__)

# IMPORTANT : leave the root route to the Elastic Beanstalk Load Balancer health check, it performs a GET to '/' every 5 seconds and expects a '200'
@main_bp.route('/', methods=['GET'])
def EB_healthcheck():
    return 'OK', 200

@main_bp.route('/register', methods=['POST'])
def register_user():
    try:
        
        data = request.get_json()
        print('\n\nData\n\n',data,'\n\n')
        new_user = People(
            email = data["email"],
            age = data["age"],
            birthday = datetime.utcnow()
        )
        db.session.add(new_user)
        db.session.commit()
        return 'User added', 200
    except Exception as e:
        db.session.rollback()
        return f'An error occurred: {str(e)}', 500


@main_bp.route('/listusers', methods=['GET'])
def list_users():
    try:
        users = db.session.query(People).all()
        # calling the __str__ representation defined in the User model 
        return jsonify([str(u) for u in users])
    except Exception as e:
        db.session.rollback()
        return f'An error occurred: {str(e)}', 500
