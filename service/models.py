from flask_restx import fields

def build_passenger_model(api):

    api.model('Passenger', {
        'passengerid': fields.Integer(description='Passenger ID'),
        'survived': fields.Boolean(description='Passenger survived'),
        'pclass': fields.Integer(description='Passenger pclass'),
        'name': fields.String(description='Passenger name'),
        'sex': fields.String(description='Passenger sex'),
        'age': fields.Integer(description='Passenger age'),
        'sibsp': fields.Integer(description='Passenger sibsp'),
        'parch': fields.Integer(description='Passenger parch'),
        'ticket': fields.String(description='Passenger ticket'),
        'fare': fields.Float(description='Passenger fare'),
        'cabin': fields.String(description='Passenger cabin'),
        'embarked': fields.String(description='Passenger ID'),
    })
