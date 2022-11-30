from flask_wtf import FlaskForm
import wtforms as ws


from app import app
from . import models
from datetime import date


class StudentForm(FlaskForm):
    name = ws.StringField('ФИО студента',validators=[ws.validators.DataRequired(),])
    birth_date = ws.DateField('Дата рождения',validators=[ws.validators.DataRequired(),])
    phone = ws.StringField(' Номер телефона',validators=[ws.validators.DataRequired(),])
    course_id = ws.SelectField('Курс', choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.course_choices = []
        with app.app_context():
            for course in models.Course.query.all():
                self.course_choices.append((course.id, course.name))
            self._fields['course_id'].choices = self.course_choices

    def validate(self):
        if not super().validate() == True:
            return False

        error_counter = 0
        date_now = date.today()

        for name in self.name.data:
            if not name.isalpha() and not ' ' in name:
                self.name.errors.append('ФИО не может содержать цифры или спец символы!')
                error_counter += 1

        for num in self.phone.data:
            if not num.isdigit() and not '+' in num:
                self.phone.errors.append('В номер не должно быть спец символы и букв!')
                error_counter += 1

        if self.phone.data[0] != '+':
            self.phone.errors.append('Номер телефона должен начинаться с +!')
            error_counter += 1

        age = date_now.year - self.birth_date.data.year
        if age < 18:
            self.birth_date.errors.append('Студенту должно быть 18 и более лет!')
            error_counter += 1

        if error_counter > 0:
            return False
        else:
            return True


class CourseForm(FlaskForm):
    name = ws.StringField('Названия курса',validators=[ws.validators.DataRequired(),])
    duration = ws.StringField('Длительность курса',validators=[ws.validators.DataRequired(),])
    mentor_id = ws.SelectField('Ментор',choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mentor_choices = []
        with app.app_context():
            for mentor in models.Mentor.query.all():
                self.mentor_choices.append((mentor.id, mentor.name))
            self._fields['mentor_id'].choices = self.mentor_choices


class MentorForm(FlaskForm):
    name = ws.StringField('ФИО ментор', validators=[ws.validators.DataRequired(), ])
    birth_date = ws.DateField('Дата рождения', validators=[ws.validators.DataRequired(), ])
    phone = ws.StringField(' Номер телефона', validators=[ws.validators.DataRequired(), ])
    speciality = ws.StringField('Специальность', validators=[ws.validators.DataRequired(), ])
    experience = ws.IntegerField('Стаж', validators=[ws.validators.DataRequired(), ])

    def validate(self):
        if not super().validate() == True:
            return False

        error_counter = 0
        date_now = date.today()

        for name in self.name.data:
            if not name.isalpha() and not ' ' in name:
                self.name.errors.append('ФИО не может содержать цифры или спец символы!')
                error_counter += 1

        for num in self.phone.data:
            if not num.isdigit() and not '+' in num:
                self.phone.errors.append('В номер не должно быть спец символы и букв!')
                error_counter += 1

        if self.phone.data[0] != '+':
            self.phone.errors.append('Номер телефона должен начинаться с +!')
            error_counter += 1

        age = date_now.year - self.birth_date.data.year
        if age < 18:
            self.birth_date.errors.append('Студенту должно быть 18 и более лет!')
            error_counter += 1

        age = date_now.year - self.birth_date.data.year
        if age - self.experience.data < 18:
            self.experience.errors.append('Стаж веден не верно!')
            error_counter += 1

        if error_counter > 0:
            return False
        else:
            return True


class UserForm(FlaskForm):
    username = ws.StringField('Имя пользователя', validators=[ws.validators.DataRequired(),ws.validators.length(min=4,max=20) ])
    password = ws.PasswordField('Пароль', validators=[ws.validators.DataRequired(),ws.validators.length(min=8,max=24) ])





