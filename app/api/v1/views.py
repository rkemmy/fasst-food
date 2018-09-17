from flask_restful import Resource
from flask import jsonify, request

orders_data = []

class Orders(Resource):

    def get(self):
        return jsonify({"Orders": orders_data})