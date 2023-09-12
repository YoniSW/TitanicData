import unittest
from flask import Flask
from flask_restx import Api
from app_factory import create_app

class TestAppFactory(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_app_exists(self):
        self.assertIsNotNone(self.app)

    def test_api_initialized(self):
        api = self.app.extensions['restx']
        self.assertIsInstance(api, Api)

    def test_fare_histogram_resource_registered(self):
        api = self.app.extensions['restx']
        histogram_resource = api.resources['FarePercentileHistogramResource']
        self.assertIsNotNone(histogram_resource)

    def test_passenger_list_resource_registered(self):
        api = self.app.extensions['restx']
        list_resource = api.resources['PassengerListResource']
        self.assertIsNotNone(list_resource)

    def test_passenger_resource_registered(self):
        api = self.app.extensions['restx']
        passenger_resource = api.resources['PassengerResource']
        self.assertIsNotNone(passenger_resource)

    def test_routes_exist(self):
        routes = [
            '/v1/fare-histogram',
            '/v1/passengers',
            '/v1/passengers/1'
        ]
        for route in routes:
            response = self.client.get(route)
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
