import random
from data.quiz_data_master import * 

class QuizMaster:
    
    current_quiz = []
    student_data = { "name" : 'na', "totalScore" : 0 }
    subject = ''
    # Make a quiz by randomly pick N questions
    # from the specified subject (e.g., Statistics, Calculus, or CS)
    def create_quiz(self, user, subject, totalQsInQuiz:int ):
        self.subject = subject
        # Init user's specific data
        self.student_data['name'] = user 
        # get questions for the specified subject (e.g., calculus, cs, etc)
        questions = quiz_data_master.get_questions(subject)
        # get unique questions for totalQsInQuiz
        self.current_quiz = random.sample(questions, totalQsInQuiz)
        
        # print the random list for debugging purpose
        qlist = []
        for q in self.current_quiz:
            qlist.append(q['question'])
        print('count : ', qlist.count, 'list:', qlist)

        # return this so the UI can use the questions for 
        # making the quiz wizzard
        return self.current_quiz
            
    def get_quiz_questions(self, subject):
        return quiz_data_master.get_questions(subject)
 
    # put method: addQuestionYes
    def check_answer(self, question, answer):
        QnA = {}
        result = {
            'correctAnswer': '', 
            'scoreForThisAnswer': 0,
            'totalScore': 0, 
            'solution': ''
        }
         
        for q in self.current_quiz:
            if question == q['question']:
                QnA = q
                break
        
        if (QnA == {}):
            return 'Cannot find question'

        result['correctAnswer'] =  QnA['answer']
        result['solution'] =  QnA['solution']
        if (answer == QnA['answer']):
            self.student_data['totalScore'] =  self.student_data['totalScore'] + QnA['score']
            result['scoreForThisAnswer'] = QnA['score']
            print('Good answer for : ', QnA['question'], QnA['score'])
        else:
            # no score since answer is incorrect. 
            # UI can check for this value and display incorrect message
            # and with correct answer
            result['scoreForThisAnswer'] = 0

        result['totalScore'] = self.student_data['totalScore']
        return result

     