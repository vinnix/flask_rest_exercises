from flask import Blueprint

main_bp = Blueprint('main', __name__)

# IMPORTANT for later : leave the root route to the Elastic Beanstalk Load Balancer health check as it performs a GET to '/' every 5 seconds and expects a '200' response
@main_bp.route('/', methods=['GET'])
def EB_healthcheck():
        return 'OK', 200
