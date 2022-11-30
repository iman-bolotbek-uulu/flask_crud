from app import db,bcrypt,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Mentor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable=False,unique=True)
    birth_date = db.Column(db.Date)
    phone = db.Column(db.String)
    speciality = db.Column(db.String)
    experience = db.Column(db.String)

    def __repr__(self):
        return self.name


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    duration = db.Column(db.String)
    mentor = db.relationship(Mentor, backref=db.backref('course', lazy='dynamic'))
    mentor_id = db.Column(db.Integer, db.ForeignKey('mentor.id'))

    def __repr__(self):
        return self.name


class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    birth_date = db.Column(db.Date)
    phone = db.Column(db.String)
    course = db.relationship(Course, backref=db.backref('student', lazy='dynamic'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

    def __repr__(self):
        return self.name


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String,nullable=False,unique=True)
    password_hash = db.Column(db.String,nullable=False)

    def __repr__(self):
        return self.username

    @property
    def password(self):
        return None

    @password.setter
    def password(self,password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self,password):
        return bcrypt.check_password_hash(self.password_hash, password)

