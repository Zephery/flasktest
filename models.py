# encoding=utf8
import MySQLdb
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/hello'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_NATIVE_UNICODE']=False
# app.con
# conn = MySQLdb.Connect(host='localhost', user='root', passwd='root', db='kebiao', port=3306, charset='utf8')
# cur = conn.cursor()
db = SQLAlchemy(app)


class User(db.Model):  # 用户信息
    __tablename__ = 'users'
    student_id = db.Column(db.String(10), primary_key=True)
    student_name = db.Column(db.String(10))
    sex = db.Column(db.String(10))
    grade = db.Column(db.String(10))
    college = db.Column(db.String(60))
    major = db.Column(db.String(60))
    inclass = db.Column(db.String(40))
    length_of_schooling = db.Column(db.String(10))

    def __init__(self, student_id, student_name, sex, grade, college, major, inclass, length_of_schooling):
        self.student_id = student_id
        self.student_name = student_name
        self.sex = sex
        self.grade = grade
        self.college = college
        self.major = major
        self.inclass = inclass
        self.length_of_schooling = length_of_schooling


class Score(db.Model):  # 成绩表
    __tablename__ = 'score'
    class_id = db.Column(db.String(20), primary_key=True)
    class_name = db.Column(db.String(60))
    score = db.Column(db.String(10))
    school_year = db.Column(db.String(10))
    semester = db.Column(db.String(10))
    student_id = db.Column(db.String(10))

    def __init__(self, class_id, class_name, score, school_year, semester, student_id):  # 各种初始化
        self.class_id = class_id
        self.class_name = class_name
        self.score = score
        self.school_year = school_year
        self.semester = semester
        self.student_id = student_id
