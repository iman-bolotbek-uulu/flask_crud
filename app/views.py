from flask import request, render_template, redirect, url_for,flash
from flask_login import login_user, logout_user, login_required
from app import db
from . import models
from . import forms


def students_list():
    students = models.Student.query.all()
    return render_template('students_list.html',students=students)


@login_required
def student_create():
    title = "Добавить студента"
    save = 'Сохранить'
    form = forms.StudentForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            student = models.Student()
            form.populate_obj(student)
            db.session.add(student)
            db.session.commit()
            flash('Студент успешно сохранен!','success')
            return redirect(url_for('students_list'))
    return render_template('student_form.html',form=form,title=title,save=save)

@login_required
def course_create():
    save = 'Сохранить'
    title = "Добавить курс"
    form = forms.CourseForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            course = models.Course()
            form.populate_obj(course)
            db.session.add(course)
            db.session.commit()
            return redirect(url_for('students_list'))
    return render_template('student_form.html',form=form,title=title,save=save)

@login_required
def mentor_create():
    title = "Добавить ментора"
    save = 'Сохранить'
    form = forms.MentorForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            mentor = models.Mentor()
            form.populate_obj(mentor)
            db.session.add(mentor)
            db.session.commit()
            return redirect(url_for('students_list'))
    return render_template('student_form.html',form=form,title=title,save=save)


def student_detail(id):
    student = models.Student.query.get(id)
    return render_template('student_detail.html',student=student)

@login_required
def student_update(id):
    title = "Добавить студента"
    save = 'Сохранить'
    student = models.Student.query.get(id)
    form = forms.StudentForm(request.form,obj=student)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(student)
            db.session.add(student)
            db.session.commit()
            return redirect(url_for('students_list'))
    return render_template('student_form.html',form=form,title=title,save=save)

@login_required
def student_delete(id):
    student = models.Student.query.get(id)
    if request.method == 'POST':
            db.session.delete(student)
            db.session.commit()
            return redirect(url_for('students_list'))
    return render_template('student_delete.html',student=student)


def course_detail(id):
    course = models.Course.query.get(id)
    return render_template('course_detail.html',course=course)


@login_required
def course_update(id):
    title = "Добавить курс"
    save = 'Сохранить'
    course = models.Course.query.get(id)
    form = forms.CourseForm(request.form,obj=course)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(course)
            db.session.add(course)
            db.session.commit()
            return redirect(url_for('students_list'))
    return render_template('student_form.html',form=form,title=title,save=save)


@login_required
def course_delete(id):
    course = models.Course.query.get(id)
    if request.method == 'POST':
            db.session.delete(course)
            db.session.commit()
            return redirect(url_for('students_list'))
    return render_template('course_delete.html',course=course)


def mentor_detail(id):
    mentor = models.Mentor.query.get(id)
    return render_template('mentor_detail.html',mentor=mentor)


@login_required
def mentor_update(id):
    title = "Добавить ментора"
    save = 'Сохранить'
    mentor = models.Mentor.query.get(id)
    form = forms.MentorForm(request.form,obj=mentor)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(mentor)
            db.session.add(mentor)
            db.session.commit()
            return redirect(url_for('students_list'))
    return render_template('student_form.html',form=form,title=title,save=save)


@login_required
def mentor_delete(id):
    mentor = models.Mentor.query.get(id)
    if request.method == 'POST':
            db.session.delete(mentor)
            db.session.commit()
            return redirect(url_for('students_list'))
    return render_template('mentor_delete.html', mentor=mentor)


def register_view():
    title = 'Регистрация пользоваться'
    save = 'Зарегистрировать'
    form = forms.UserForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = models.User()
            form.populate_obj(user)
            # user = models.User(username=request.form.get('username'))
            # user.set_password(request.form.get('password'))
            db.session.add(user)
            db.session.commit()
            flash(f'Пользователь {user.username} успешно зарегистрирован!','success')
            return redirect(url_for('login'))
    return render_template('student_form.html', form=form,title=title,save=save)


def login_view():
    title = 'Войти'
    save = 'Войти'
    form = forms.UserForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            # user = models.User()
            # form.populate_obj(user)
            user = models.User.query.filter_by(username=request.form.get('username')).first()
            if user and user.check_password(request.form.get('password')):
                login_user(user)
                flash('Успешно авторизован!','primary')
                return redirect(url_for('students_list'))
            else:
                flash('Неправильно введенные логин или пароль!', 'danger')
    return render_template('student_form.html', form=form,title=title,save=save)


def logout_view():
    logout_user()
    return redirect(url_for('students_list'))


