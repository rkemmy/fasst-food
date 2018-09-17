from flask import Blueprint
from flask_restful import Api
from .api.v1.views import  Orders

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Orders, '/orders')
