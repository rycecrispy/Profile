from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
from data.quiz_data_master import *
from api.quiz_master import *
from flask import request

# Create instance of QuizMaster that creates quizes and keeps track
# of user's test scores
quiz_master = QuizMaster()

quiz_master_app_api = Blueprint('quiz_master_api', __name__,
                   url_prefix='/api/quiz')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
quiz_master_api = Api(quiz_master_app_api)

class QuizMasterRest:
    
    # Make a quiz by randomly pick N questions
    # from the specified subject (e.g., Statistics, Calculus, or CS)
    class _CreateQuiz(Resource):
        def get(self, user, subject, totalQsInQuiz ):
            return quiz_master.create_quiz(user, subject, totalQsInQuiz)
            
    class _Read(Resource):
        def get(self):
            return quiz_master.get_quiz_data(SUBJ_Cal)

 
    # put method: addQuestionYes
    class _CheckAnswer(Resource):
        def put(self):
            return quiz_master.check_answer(request.json['question'], request.json['answer'])
    
    # building RESTapi resources/interfaces, these routes are added to Web Server
    quiz_master_api.add_resource(_CreateQuiz, '/create/<string:user>/<string:subject>/<int:totalQsInQuiz>')
    quiz_master_api.add_resource(_Read, '/')
    # quiz_master_api.add_resource(_CheckAnswer, '/checkanswer')
    
 