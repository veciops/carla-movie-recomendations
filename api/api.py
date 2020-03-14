from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from recommender import *
from recommender import recommender

app = Flask(__name__)
api = Api(app)


# querystring example: cpu=Snapdragon 855&storage-capacity=128 GB&removable-storage=No&ram=6 GB&os=Android 8.1
# "Oreo"&battery=3500mAh&display=6.41" 2340x1080 AMOLED&camera=Dual 12 MP + 13 MP (rear camera) 24.8 MP (front
# camera)&fingerprint-scanner=Under screen&facial-recognition=Yes
class Recommendations(Resource):
    # return a list of recommendations
    def get(self):

        return jsonify(
            recommender.get_recommendations(request.args.get('cpu'),
                                            request.args.get('storage-capacity'),
                                            request.args.get('removable-storage'),
                                            request.args.get('ram'),
                                            request.args.get('os'),
                                            request.args.get('battery'),
                                            request.args.get('display'),
                                            request.args.get('camera'),
                                            request.args.get('fingerprint-scanner'),
                                            request.args.get('facial-recognition')))

class Filters(Resource):
    # return a list of filters
    def get(self):
        return jsonify(
            recommender.get_filters())




api.add_resource(Recommendations, '/recommendations')
api.add_resource(Filters, '/filters' )

if __name__ == '__main__':
    app.run()
