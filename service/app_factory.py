from flask import Flask
from flask_restx import Api
import time

def create_app():
    time.sleep(10)
    app = Flask(__name__)
    api = Api(app)

    # Register API resources with version prefixes
    from resources import FarePercentileHistogramResource, PassengerListResource, PassengerResource
    api.add_resource(FarePercentileHistogramResource, '/v1/fare-histogram')
    api.add_resource(PassengerListResource, '/v1/passengers')
    api.add_resource(PassengerResource, '/v1/passengers/<int:passenger_id>')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)