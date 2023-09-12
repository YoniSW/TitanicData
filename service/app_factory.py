from flask import Flask
from flask_restx import Api
import time

from models import build_passenger_model

def set_swagger_endpoint(app):
    api = Api(app,
        version='1.0',
        title='Titanic Passenger Web Service',
        description='The Titanic Passenger Data Web Service is a tool designed to facilitate the ֿֿ\
            loading of raw Titanic passenger data into a PostgreSQL database and provide user-specific \
                details upon request. This service allows users to interact with the Titanic dataset, \
                    retrieve information, and perform various data operations.',
        doc='/swagger')
    
    build_passenger_model(api)
    return api


def create_app():
    time.sleep(10)
    app = Flask(__name__)
    api = set_swagger_endpoint(app)
    
    # Register API resources with version prefixes
    from resources import FarePercentileHistogramResource, PassengerListResource, PassengerResource
    api.add_resource(FarePercentileHistogramResource, '/v1/fare-histogram')
    api.add_resource(PassengerListResource, '/v1/passengers')
    api.add_resource(PassengerResource, '/v1/passengers/<int:passenger_id>', resource_class_kwargs={
        'model': api.models.get('Passenger')})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=False, host='0.0.0.0', port=5000)
