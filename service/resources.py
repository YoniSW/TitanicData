import jsonify
from flask import jsonify, send_file
from flask_restx import Resource, reqparse, Namespace, fields
from io import BytesIO
import matplotlib.pyplot as plt
from loguru import logger
import numpy as np

from database import fetch_passengers, fetch_passenger_by_id

# Request parser for filtering attributes
parser = reqparse.RequestParser()
parser.add_argument('attributes', type=str, help='Comma-separated list of attributes to include')
api = Namespace('passenger', description='Passenger related operations')

# Passenger model for Swagger documentation
passenger_model = api.model('Passenger', {
    'passengerid': fields.Integer,
    'survived': fields.Integer,
    'pclass': fields.Integer,
    'name': fields.String,
    'sex': fields.String,
    'age': fields.Float,
    'sibsp': fields.Integer,
    'parch': fields.Integer,
    'ticket': fields.String,
    'fare': fields.Float,
    'cabin': fields.String,
    'embarked': fields.String,
})


class FarePercentileHistogramResource(Resource):
    def get(self):
        """Return a histogram of Fare prices in percentiles"""
        passengers = fetch_passengers()

        if not passengers:
            return jsonify({'error': 'No passenger data available'}), 404

        fares = [passenger['fare'] for passenger in passengers]

        if not fares:
            return jsonify({'error': 'No Fare data available'}), 404

        # Define percentiles
        percentiles = [i * 10 for i in range(1, 10)]

        # Calculate percentiles for fares
        fare_percentiles = np.percentile(fares, percentiles)

        # Create the histogram data
        histogram_data = [{'percentile': p, 'count': np.sum(fares <= fp).item()} for p, fp in zip(percentiles, fare_percentiles)]

        # Create the histogram (bar chart)
        percentiles_labels = [str(p) + "%" for p in percentiles]
        counts = [item['count'] for item in histogram_data]

        plt.bar(percentiles_labels, counts)
        plt.xlabel('Percentiles')
        plt.ylabel('Count')
        plt.title('Fare Percentile Histogram')

        # Save the chart as an image
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)

        # Return the image as a response
        return send_file(img_buffer, mimetype='image/png')


class PassengerListResource(Resource):
    @api.marshal_list_with(passenger_model)
    def get(self):
        """Get a list of all passengers"""
        return fetch_passengers()

class PassengerResource(Resource):
    @api.marshal_with(passenger_model)
    def get(self, passenger_id):
        """Get passenger data by PassengerId"""
        passenger = fetch_passenger_by_id(passenger_id)
        if passenger:
            return passenger
        api.abort(404, message="Passenger not found")

    def post(self, passenger_id):
        """Filter and return specific attributes for a passenger"""
        args = parser.parse_args()
        passenger = fetch_passenger_by_id(passenger_id)
        if passenger:
            if args.get('attributes'):
                attribute_list = args.get('attributes').strip().split(',')
                return {k: v for k, v in passenger.items() if k in attribute_list}
            else:
                return passenger
        api.abort(404, message="Passenger not found")