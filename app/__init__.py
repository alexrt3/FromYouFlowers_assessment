from flask import Flask
from flask_restful import Resource, Api
from service import AnswerOne
from service2 import AnswerTwo

app = Flask(__name__)
api = Api(app)

class EndpointOne(Resource):
    
    def get(self):
        return AnswerOne.get_combinations(AnswerOne.total)

class EndpointTwo(Resource):

    def get(self):
        return AnswerTwo.get_combinations(AnswerTwo.den, AnswerTwo.total)

api.add_resource(EndpointOne, "/answerone")
api.add_resource(EndpointTwo, "/answertwo")

from app import views

if __name__ == "__main__":
    app.run(debug=True)
