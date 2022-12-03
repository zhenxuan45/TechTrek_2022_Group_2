import os
from re import T
from types import new_class
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
from sqlalchemy.sql.schema import ForeignKey
from datetime import datetime
from datetime import date
import json
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql://MrLeKB:Ydauu2w7@spmdatabase.cffxztdrjjzg.ap-southeast-1.rds.amazonaws.com/lnd_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class CourseMaterial(db.Model):
    __tablename__ = 'CourseMaterial'

    MaterialID = db.Column(db.Integer, primary_key=True)
    Material_Link = db.Column(db.String(20))

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class SectionMaterial(db.Model):

    __tablename__ = 'SectionMaterial'

    CourseID = db.Column(db.String(5), primary_key=True)
    ClassID = db.Column(db.String(2), primary_key=True)
    SectionID = db.Column(db.String(2), primary_key=True)
    MaterialID = db.Column(db.Integer, primary_key=True)

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Quiz(db.Model):
    __tablename__ = 'Quiz'
    QuizID = db.Column(db.String(5), primary_key = True)
    TimeLimit = db.Column(db.Integer)
    gradeType = db.Column(db.String(1))


    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class CourseHistory(db.Model):
    __tablename__ = 'CourseHistory'

    CourseID = db.Column(db.String(5),primary_key=True)
    ClassID = db.Column(db.String(2),primary_key=True)
    LearnerID = db.Column(db.String(4),primary_key=True)
    Completed = db.Column(db.String(1))

    def __init__(self,CourseID, ClassID, LearnerID, Completed):
        self.CourseID = CourseID
        self.ClassID = ClassID
        self.LearnerID = LearnerID
        self.Completed = Completed

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


    # def json(self):
    #     return {"CourseID": self.CourseID,"ClassID": self.ClassID,"LearnerID": self.LearnerID,"Completed": self.Completed}

class Class(db.Model):

    __tablename__ = 'Class'

    ClassID = db.Column(db.String(2), primary_key=True)
    CourseID = db.Column(db.String(5),primary_key=True)
    TrainerID = db.Column(db.String(10))
    StartDate = db.Column(db.String(10))
    EndDate = db.Column(db.String(10))
    StartTime = db.Column(db.String(10))
    EndTime = db.Column(db.String(10))
    ClassSize = db.Column(db.Integer)
    
    def __init__(self, CourseID, ClassID, TrainerID, Sdate, Edate, Stime, Etime, ClassSize):
        self.CourseID = CourseID
        self.ClassID = ClassID
        self.TrainerID = TrainerID
        self.StartDate = Sdate
        self.EndDate = Edate
        self.StartTime = Stime
        self.EndTime = Etime
        self.ClassSize = ClassSize

    def getClassSize(self):
        return (self.ClassSize)
    
    def getStartDate(self):
        return (self.StartDate)

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    # def json(self):
    #     return {"CourseID": self.CourseID, "ClassID": self.ClassID, "TrainerID": self.TrainerID, "Sdate": self.StartDate,"Edate":self.EndDate,"Stime":self.StartTime,"Etime":self.EndTime,"ClassSize":self.ClassSize}
    
class EnrolRecord(db.Model):
    __tablename__ = 'EnrolRecord'

    CourseID = db.Column(db.String(10), primary_key=True)
    ClassID = db.Column(db.String(10), primary_key=True)
    LearnerID = db.Column(db.String(4),primary_key=True)
    Acceptance = db.Column(db.String(10))
    Enrollment = db.Column(db.String(10))

    
    def __init__(self,CourseID,ClassID,LearnerID,Acceptance,Enrollment): 
        self.CourseID =CourseID
        self.ClassID= ClassID
        self.LearnerID = LearnerID
        self.Acceptance = Acceptance
        self.Enrollment = Enrollment

    # def getEnrolStatus(self):
    #     return (self.Acceptance)
    
    def acceptLearner(self):
        self.Acceptance = "confirmed"
        return "learner accepted"
    
    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    # def json(self):
    #     return {"CourseID": self.CourseID, "ClassID": self.ClassID, "LearnerID": self.LearnerID, "Acceptance": self.Acceptance,"Enrollment":self.Enrollment}

class Course(db.Model):
    __tablename__ = 'Course'

    CourseID = db.Column(db.String(5), primary_key = True)
    CourseName = db.Column(db.String(10))
    
    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Question(db.Model):
    __tablename__ = 'Question'
    #__table_args__ = {'mysql_engine':'lnd_database'}
    QuizID = db.Column(db.String(7), db.ForeignKey(Quiz.QuizID), primary_key=True)
    QuestionID = db.Column(db.String(7), primary_key=True)
    Question = db.Column(db.String(255))
    QuestionType=db.Column(db.String(3))

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Option(db.Model):
    __tablename__ = 'Options'
    QuizID = db.Column(db.String(7), db.ForeignKey(Quiz.QuizID), primary_key=True)
    QuestionID = db.Column(db.String(7), db.ForeignKey(Question.QuestionID), primary_key=True)
    OptionID = db.Column(db.String(7),primary_key=True)
    Option = db.Column(db.String(1))
    Answer = db.Column(db.Integer)
    

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Section(db.Model):
    __tablename__ = 'Section'
    SectionID = db.Column(db.String(2), primary_key = True)
    CourseID = db.Column(db.String(5), ForeignKey(Course.CourseID), primary_key = True)
    ClassID = db.Column(db.String(2), ForeignKey(Class.ClassID), primary_key = True)
    QuizID = db.Column(db.String(5),ForeignKey(Quiz.QuizID))
    
    def add_quiz_id(self,quizID):
        self.QuizID = quizID
    def get_quiz_id(self):
        return self.QuizID
    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class User(db.Model):
    
    __tablename__ = 'UserRecord'

    
    UserID = db.Column(db.String(4), primary_key=True)
    UserRole = db.Column(db.String(25), nullable=False)
    EmployeeID = db.Column(db.Integer, nullable=False)
    
    # def getUserID(self):
    #     return(self.UserID)
        
    # def getRole(self):
    #     return (self.UserRole)

    # def getEmployeeID(self):
    #     return (self.EmployeeID)
    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class PreRequisite(db.Model):
    __tablename__ = 'Pre_Requisite_Course'

    CourseID = db.Column(db.String(5), primary_key=True)
    PreCourseID = db.Column(db.String(5), primary_key=True)

    # def getCourseID(self):
    #     return(self.CourseID)
        
    def getPreCourseID(self):
        return (self.PreCourseID)

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

@app.route("/prerequisite/<courseID>")
def get_prerequisite_id(courseID):
    prerequisite = PreRequisite.query.filter_by(CourseID = courseID).first()
    prerequisite_id = prerequisite.getPreCourseID()
    if prerequisite_id:
        return jsonify({
            "data": prerequisite_id
        }), 200
    else:
        return jsonify({
            "message": "Person not found."
        }), 404

    
@app.route("/users/<int:UserID>")
def user_by_id(UserID):
    user = User.query.filter_by(UserID=UserID).first()
    if user:
        return jsonify({
            "data": user.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Person not found."
        }), 404
 
@app.route("/userrole/<string:role>")
def user_by_role(role):
    user_list = User.query.filter_by(UserRole=role).all()
    if len(user_list):
        return jsonify({
            "data": [user.to_dict() for user in user_list]
        }), 200
    else:
        return jsonify({
            "message": "Person not found."
        }), 404       

@app.route("/user/create", methods=['POST'])
def create_user():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('UserID', 'UserRole',
                       'EmployeeID')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    request_data = json.loads(request.data)

    user = User(UserID=request_data['UserID'], UserRole=request_data['UserRole'],EmployeeID=request_data['EmployeeID'])
    try:  
        db.session.add(user)
        db.session.commit()
        
    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500
    return jsonify({
            "data": user.to_dict()
            }), 201

@app.route("/coursematerial")
def coursematerial_all():
    coursematerial_list = CourseMaterial.query.all()
    print(coursematerial_list)
    if len(coursematerial_list):
        return jsonify({
            "data": [coursematerial.to_dict() for coursematerial in coursematerial_list]
        }), 200
    else:
        return jsonify({
            "message": "Course Material not found."
        }), 404

@app.route("/coursematerial/<int:MaterialID>")
def coursematerial_by_id(MaterialID):
    coursematerial = CourseMaterial.query.filter_by(MaterialID=MaterialID).first()
    if coursematerial:
        return jsonify({
            "data": coursematerial.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Course Material not found."
        }), 404

@app.route("/coursematerial/create", methods=['POST'])
def create_coursematerial():
    data = request.get_json()
    if not 'Material_Link':
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    coursematerial = CourseMaterial(**data)
    print(coursematerial)
    try:
        db.session.add(coursematerial)
        db.session.commit()
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500
    return jsonify(coursematerial.to_dict()), 201

@app.route("/sectionmaterial/<string:CourseID>/<string:ClassID>/<string:SectionID>")
def get_sectionmaterial(CourseID, ClassID, SectionID):

    sectionmaterial = SectionMaterial.query.filter_by(CourseID=CourseID, ClassID=ClassID, SectionID=SectionID).first()
    if sectionmaterial:
        return jsonify({
            "data": sectionmaterial.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Section material not found."
        }), 404

@app.route("/sectionmaterialAll/<string:CourseID>/<string:ClassID>")
def get_all_sectionmaterial(CourseID, ClassID):

    sectionmaterial_list = SectionMaterial.query.filter_by(CourseID=CourseID, ClassID=ClassID).all()
    if len(sectionmaterial_list):
        return jsonify({
            "data": [sectionmaterial.to_dict() for sectionmaterial in sectionmaterial_list]
        }), 200
    else:
        return jsonify({
            "message": "Section material not found."
        }), 404

@app.route("/sectionmaterial/create", methods=['POST'])
def create_sectionmaterial():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('CourseID', 'ClassID',
                       'SectionID', 'MaterialID')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    sectionmaterial = SectionMaterial(**data)
    try:
        db.session.add(sectionmaterial)
        db.session.commit()
        return jsonify(sectionmaterial.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

@app.route("/sectionmaterial/update", methods=['PUT'])
def update_sectionmaterial():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('CourseID', 'ClassID',
                       'SectionID', 'MaterialID')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    sectionmaterial = SectionMaterial(**data)
    try:
        db.session.add(sectionmaterial)
        db.session.commit()
        return jsonify(sectionmaterial.to_dict()), 201
    except Exception as e:
        print(e)
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

@app.route("/question/create", methods= ['POST'])
def create_question():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('QuestionID', 'Question',
                       'QuizID','QuestionType')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    question = Question(**data)
    try:
        db.session.add(question)
        db.session.commit()
        
    except Exception as e:
        print(e)
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

    return jsonify(question.to_dict()), 201

@app.route("/question/<quizID>")
def question_by_quiz(quizID):
    questions = Question.query.filter_by(QuizID=quizID)
    question_list= json.dumps([question.to_dict() for question in questions])
    if question_list:
        return {"data":json.loads(question_list)}, 200
    else:
        return jsonify({
            "message": "Quiz not found"
    })

@app.route("/question/<quizID>/<questionID>")
def question_by_id(questionID,quizID):
    question = Question.query.filter_by(QuestionID=questionID, QuizID=quizID).first()
    if question:
        return jsonify({
            "data": question.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Questions not found."
        }), 404

@app.route('/question/create-multiple', methods=['POST'])
def create_multiple_questions():
    data = json.loads(request.get_json())
    if not all (key in each_data.keys() for key in ('QuizID', 'QuestionID',
                       'Question','QuestionType') for each_data in data):
        return jsonify({
            "message": "Incorrect JSON object provided"
        }), 500
    questions= []
    for each_data in data:
        questions.append(Question(**each_data))
        print(questions)    

    try:
        for question in questions:
            db.session.add(question)
            db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({
            "message": "Unable to commit to database."
        }), 500
    return jsonify({"message": "successfully created"}), 201

@app.route("/option")
def all_options():
    options= Option.query.all()
    option_list = json.dumps([option.to_dict() for option in options])
    if option_list:
        return  {"data":json.loads(option_list)}, 200
        
    else:
        return jsonify({
            "message": "Options not found."
        })

@app.route("/option/<quizID>/<questionID>")
def option_by_question(quizID,questionID):
    options = Option.query.filter_by(QuestionID=questionID, QuizID=quizID)
    if options:
        #returns a list of options objects in json
        options_list = [option.to_dict() for option in options]

        return jsonify({
            "data": options_list
        }), 200
    else:
        return jsonify({
            "message": "Options not found."
        }), 404

@app.route("/option/create", methods= ['POST'])
def create_option():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('QuestionID','OptionID', 'Option',
                       'Answer')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    option = Option(**data)
    try:
        db.session.add(option)
        db.session.commit()
        
    except Exception as e:
        print(e)
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

    return jsonify(option.to_dict()), 201
    
@app.route("/option/create-multiple", methods=['POST'])
def option_create_multiple():
    data = json.loads(request.get_json())
    if not all (key in each_data.keys() for key in ('QuestionID','OptionID', 'Option',
                       'Answer') for each_data in data):
        return jsonify({
            "message": "Incorrect JSON object provided"
        }), 500
    options= []
    for each_data in data:
        options.append(Option(**each_data))
    try:
        for option in options:
            db.session.add(option)
            db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({
            "message": "Unable to commit to database."
        }), 500
    return jsonify({"message": "successfully created"}), 201

@app.route("/courses")
def get_courses():
    course_list =  Course.query.all()

    return jsonify({
        "data": [each_course.to_dict() for each_course in course_list]
    }), 200

@app.route("/course/<string:courseID>")
def course_by_id(courseID):
    course = Course.query.filter_by(CourseID=courseID).first()
    
    if course:
        return jsonify({
            "data": course.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Quiz not found."
        }), 404

@app.route("/quiz/create", methods=['POST'])
def create_quiz():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('QuizID', 'TimeLimit','gradeType')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    quiz = Quiz(**data)
    try:
        db.session.add(quiz)
        db.session.commit()
        return jsonify(quiz.to_dict()), 201
    except Exception as e:
        # print(e)
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

@app.route("/quiz")
def get_all_quiz():
    quiz_list = Quiz.query.all()
    if len(quiz_list):
        return jsonify({
            "data": [quiz.to_dict() for quiz in quiz_list]
        }), 200
    else:
        return jsonify({
            "message": "Quiz not found."
        }), 404


@app.route("/quiz/<quizID>")
def quiz_by_id(quizID):
    quiz = Quiz.query.filter_by(QuizID=quizID).first()
    if quiz:
        return jsonify({
            "data": quiz.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Quiz not found."
        }), 404

@app.route('/section/<courseID>/<classID>')
def section_by_class(courseID, classID):
    sections = Section.query.filter_by(CourseID=courseID, ClassID=classID)
    section_list =json.dumps([section.to_dict() for section in sections])
    if section_list:
        return {"data":json.loads(section_list)}, 200
    else:
        return jsonify({
            "message": "Class not found"
    })

@app.route('/section/get-quiz/<courseID>/<classID>/<sectionID>')
def quiz_by_section(courseID, classID, sectionID):
    section = Section.query.filter_by(CourseID=courseID, ClassID=classID, SectionID=sectionID).first()
    if (section.get_quiz_id() and section ):
        return jsonify({
            "data" : section.get_quiz_id()
        }), 200
    else:
        return jsonify({
            "message": "Section not found."
        }), 404

@app.route('/section/<courseID>/<classID>/<sectionID>')
def section_by_id(courseID, classID, sectionID):
    section = Section.query.filter_by(CourseID=courseID, ClassID=classID, SectionID=sectionID).first()
    if section:
        return jsonify({
            "data": section.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Section not found."
        }), 404

@app.route("/section/add-quiz", methods=['PUT'])
def add_quiz():
    data = request.get_json()   
    if not all(key in data.keys() for
               key in ('CourseID', 'ClassID',
                       'SectionID','QuizID')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    section = Section.query.filter_by(CourseID=data["CourseID"], ClassID=data["ClassID"], SectionID=data["SectionID"]).first()
    print("SSSSSSSSSSSSSSS",section)
    newQuizID = data["QuizID"]
    section.add_quiz_id(newQuizID)
    try:
        db.session.add(section)
        db.session.commit()

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while adding the quiz. " + str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": section.to_dict()
        }
    ), 201
@app.route("/section/create", methods=['POST'])
def create_section():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('CourseID', 'ClassID',
                       'SectionID')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    section = Section(**data)
    try:
        db.session.add(section)
        db.session.commit()
        return jsonify(section.to_dict()), 201
    except Exception as e:
        print(e)
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

@app.route("/class/create", methods=["POST"])
def create_class():
    data = request.get_json()
    print(data)
    if not all(key in data.keys() for
               key in ('ClassID','CourseID','TrainerID','StartDate','EndDate','StartTime','EndTime',
                       'ClassSize')):
        return jsonify({
            
            "message": "Incorrect JSON object provided.",
        }), 500

    #check if startdate is > today
    if datetime.strptime(data['StartDate'], '%d-%b-%y').date() <= date.today():
        return jsonify({
            "message": "Date provided not valid."
        }), 500
    #check if startdate is earlier than enddate
    if datetime.strptime(data['StartDate'], '%d-%b-%y').date() > datetime.strptime(data['EndDate'], '%d-%b-%y').date():
        return jsonify({
            "message": "Date provided not valid."
        }), 500

    #Validate trainer
    trainer = User.query.filter_by(EmployeeID=data['TrainerID']).first()
    if not trainer:
        return jsonify({
            "message": "Trainer not valid."
        }), 500

    #validate course
    course = Course.query.filter_by(CourseID=data['CourseID']).first()
    if not course:
        return jsonify({
            "message": "Course not valid."
        }), 500

    new_class = Class(**data)
    try:
        db.session.add(new_class)
        db.session.commit()
        return jsonify(new_class.to_dict()), 201

    except Exception as e:
        print(e)
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

@app.route("/classes")
def get_classes():
    class_list =  Class.query.all()
    #print(class_list)
    return jsonify({
        "data": [one_class.to_dict() for one_class in class_list]
    }), 200
    

@app.route("/classes/<course_id>")    
def classes_by_course(course_id):
    if course_id:
        class_list = Class.query.filter_by(CourseID = course_id)
        print("class_list", class_list)
    else:
        class_list = Class.query.all()
    return jsonify(
        {
            "data": [one_class.to_dict() for one_class in class_list]
        }
    ), 200

@app.route("/class/<string:CourseID>/<string:ClassID>")
def get_class(CourseID, ClassID):
    Class_Entry = Class.query.filter_by(CourseID=CourseID,ClassID=ClassID ).first()
    if Class_Entry:
        return jsonify({
            "data": Class_Entry.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Class not found."
        }), 404


@app.route("/enrolRecord")
def enrol_get_all():
    Enrollist = EnrolRecord.query.all()
    if len(Enrollist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "classes": [e.to_dict() for e in Enrollist]
                }
            }
        )
    return jsonify(
        {
            "code": 200,
        "data": {
                    "classes": []
                }
        }
    ), 200

@app.route("/assign", methods=['POST'])
def create_enrolRecord_Assign():
    try:
        data = request.get_json()

        print("-------------------Assigning learner--creating enrollment record---------------------")
        try:
            Class_Entry = Class.query.filter_by(CourseID=data['CourseID'],ClassID=data['ClassID'] ).first()
            class_size= Class_Entry.getClassSize()
            
        except:
            return jsonify({"code": 500,
                    "message": "Class do not exist " 
                    }), 500
        
        Enrollist = EnrolRecord.query.filter_by(CourseID=data['CourseID'],ClassID=data['ClassID'], Acceptance="confirmed").all()
        
        CoursePreRequistes = PreRequisite.query.filter_by(CourseID=data['CourseID']).all()
        StudentCompletedCourses = CourseHistory.query.filter_by(LearnerID=data['LearnerID'], Completed="T").all()

        if CoursePreRequistes != []:
            if StudentCompletedCourses == []:
                return jsonify({"code": 500,
                    "message": "Learner Does Not Fulfill the Course Pre-Requisite"
                }), 500
            else:
                PreList=[]
                for pre in CoursePreRequistes:
                    PreList.append(pre.getPreCourseID())
                
                matched= False
                for completed in StudentCompletedCourses:
                    if completed.CourseID in PreList:
                        matched= True
                        break
                if matched == False:
                    return jsonify({"code": 500,
                        "message": "Learner Does Not Fulfill the Course Pre-Requisite"
                    }), 500
            
        try:
            learnerEnrolled = EnrolRecord.query.filter_by(CourseID=data['CourseID'], LearnerID=data['LearnerID']).first()
            if learnerEnrolled:
                return jsonify({"code": 500,
                    "message": "Learner has already enrolled in the Course"
                    }), 500
        except:
            pass


        if len(Enrollist)<class_size:
            new_record = EnrolRecord(
                CourseID= data['CourseID'],
                ClassID=data['ClassID'],
                LearnerID=data['LearnerID'],
                Acceptance= 'confirmed',
                Enrollment= 'assigned'
            )
        else:
            return jsonify({
                "code": 404,
                "message": "Class has reached capacity"}), 404 
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the enrol record. " + str(e)
            }
        ), 500

    try:
        db.session.add(new_record)
        db.session.commit()

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the order. " + str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": new_record.to_dict()
        }
    ), 201

@app.route("/accept", methods=['PUT'])
def accept_learner():
    try:
        data = request.get_json()
    
        print("-------------------Accepting learner--creating enrollment record---------------------")
        try:
            Class_Entry = Class.query.filter_by(CourseID=data['CourseID'],ClassID=data['ClassID'] ).first()
            class_size= Class_Entry.getClassSize()
        except Exception as e:
            return jsonify({"code": 500,
                    "message": "An error occurred while creating the enrol record. " + str(e)
                    }), 500
        try:
            Enrollist = EnrolRecord.query.filter_by(CourseID=data['CourseID'],ClassID=data['ClassID'], Acceptance="confirmed").all()
            
        except Exception as e:
            return jsonify({"code": 500,
                    "message": "An error occurred while creating the enrol record. " + str(e)
                    }), 500

        if len(Enrollist)<class_size:
            learner=EnrolRecord.query.filter_by(CourseID=data['CourseID'],ClassID=data['ClassID'], LearnerID=data['LearnerID']).first()
            learner.acceptLearner()         
        else:
            return jsonify({
                "code": 404,
                "message": "Class has reached capacity"}), 404 
                
    except Exception as e:
        return jsonify({
                "code": 500,
                "message": "An error occurred while creating the enrol record. " + str(e)}), 500

    try:
        db.session.commit()

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the order. " + str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": learner.to_dict()
        }
    ), 201

@app.route('/enrolRecord/<string:CourseID>/<string:ClassID>')
def get_Enrol(CourseID, ClassID):
    Enrollist = EnrolRecord.query.filter_by(CourseID = CourseID, ClassID=ClassID).all()
    print(Enrollist)
    if len(Enrollist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "classes": [e.to_dict() for e in Enrollist]
                }
            }
        )
    return jsonify(
        {
            "code": 200,
        "data": {
                    "classes": []
                }
        }
    ), 200

@app.route('/enrolRecord/<string:LearnerID>')
def get_Enrol_by_learner(LearnerID):
    Enrol_list = EnrolRecord.query.filter_by(LearnerID = LearnerID).all()
    if len(Enrol_list):
        return jsonify(
            {
                "code": 200,
                "data": [e.to_dict() for e in Enrol_list]
                
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "You are not enrolled into any courses"
        }
    ), 404

@app.route('/enrolRecordbyStatus/<string:Acceptance>')
def get_Enrol_by_status(Acceptance):
    Enrol_list = EnrolRecord.query.filter_by(Acceptance=Acceptance).all()
    print(Enrol_list)
    if len(Enrol_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "classes": [enrol.to_dict() for enrol in Enrol_list]
                }
            }
        )
    return jsonify(
        {
            "code": 200,
        "data": {
                    "classes": []
                }
        }
    ), 200

@app.route("/CourseHistory")
def get_all():
    RecordList = CourseHistory.query.all()
    if len(RecordList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "students": [student.to_dict() for student in RecordList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Students."
        }
    ), 404

@app.route("/selfEnrol/add", methods=['POST'])
def add_learner():
    try:
        data = request.get_json()

        print("-------------------Student self enroll---------------------")
        try:
            Class_Entry = Class.query.filter_by(CourseID=data['CourseID'],ClassID=data['ClassID'] ).first()
            class_size= Class_Entry.getClassSize()
            print(class_size)
        except Exception as e:
            return jsonify({"code": 500,
                    "message": "Class do not exist " 
                    }), 500
        Enrollist = EnrolRecord.query.filter_by(CourseID=data['CourseID'],ClassID=data['ClassID'], Acceptance="confirmed").all()
        
        CoursePreRequistes = PreRequisite.query.filter_by(CourseID=data['CourseID']).all()
        StudentCompletedCourses = CourseHistory.query.filter_by(CourseID=data["CourseID"],LearnerID=data["LearnerID"],ClassID=data["ClassID"],Completed="T").all()
        
        # (1): Validate Student
        student = user_by_id(data['LearnerID'])
        if student==[]:
            return jsonify({
                "message":"Student does not exist."
            }),500

        #Validate Course Taken
        if CoursePreRequistes != []:
            if StudentCompletedCourses == []:
                return jsonify({"code": 500,
                    "message": "You do not fulfill the Course Pre-Requisite"
                }), 500
            else:
                PreList=[]
                for pre in CoursePreRequistes:
                    PreList.append(pre.getPreCourseID())
                
                matched= False
                for completed in StudentCompletedCourses:
                    if completed.CourseID in PreList:
                        matched= True
                        break
                if matched == False:
                    return jsonify({"code": 500,
                        "message": "You do not fulfill the Course Pre-Requisite"
                    }), 500
        try:
            learnerEnrolled = CourseHistory.query.filter_by(CourseID=data['CourseID'], LearnerID=data['LearnerID']).first()
            if learnerEnrolled:
                return jsonify({"code": 500,
                    "message": "You have already enrolled in the course"
                    }), 500
        except:
            pass

        try:
            learner_S_Enrolled = EnrolRecord.query.filter_by(CourseID=data['CourseID'], ClassID=data['ClassID'], LearnerID=data['LearnerID']).first()
            if learner_S_Enrolled:
                return jsonify({"code": 500,
                    "message": "You have already self enrolled in the course"
                    }), 500
        except:
            pass
        
        if len(Enrollist)<class_size:
            
            new_record = EnrolRecord(
                CourseID= data['CourseID'],
                ClassID=data['ClassID'],
                LearnerID=data['LearnerID'],
                Acceptance= 'pending',
                Enrollment= 'self'
            )


        else:
            return jsonify({
                "code": 404,
                "message": "Class has reached capacity"}), 404 
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message":"Error"
            }
        ), 500

    try:
        db.session.add(new_record)
        db.session.commit()

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the order. " + str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": new_record.to_dict()
        }
    ), 201

@app.route("/remove", methods=["DELETE"])
def remove_learner():
    try:
        data = request.get_json()

        print("-------------------Engineer withdraw---------------------")
        print(data)
        try:
            Enrol_Record = EnrolRecord.query.filter_by(CourseID=data['CourseID'],ClassID=data["ClassID"],LearnerID=data['LearnerID']).first()
        except Exception as e:
            return jsonify({"code": 500,
                    "message": "Enrol Record does not exist " 
                    }), 500
        
        Class_Record = Class.query.filter_by(CourseID=data['CourseID'],ClassID=data["ClassID"]).first()
        print(Class_Record.getStartDate())
        today = date.today()
        d4 = today.strftime("%d-%b-%y")

        if d4<Class_Record.getStartDate():
            return jsonify(
            {
                "code": 500,
                "message": "You are not allowed to withdraw at this time"
            }
        ), 500
         
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the enrol record. " + str(e)
            }
        ), 500

    try:
        db.session.delete(Enrol_Record)
        db.session.commit()

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the order. " + str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 200,
            "message":'Successfully Deleted'
        }
    ), 201

         

    

if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": student records ...")
    app.run(host='0.0.0.0', port=5001, debug=True)
