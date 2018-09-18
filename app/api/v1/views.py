from flask_restful import Resource
from flask import request


orders_data = []

class Orders(Resource):

    def get(self):
        if len(orders_data) == 0:
            return ({"message":"empty list"}, 404)
        else:
            return ({"Orders": orders_data})

    