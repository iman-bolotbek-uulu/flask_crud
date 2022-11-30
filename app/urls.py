from . import views
from app import app

app.add_url_rule('/', view_func=views.students_list,
                 endpoint='students_list')

app.add_url_rule('/student/create', view_func=views.student_create, methods=['GET', 'POST'],
                 endpoint='student_create')
app.add_url_rule('/course/create', view_func=views.course_create, methods=['GET', 'POST'],
                 endpoint='course_create')
app.add_url_rule('/mentor/create', view_func=views.mentor_create, methods=['GET', 'POST'],
                 endpoint='mentor_create')

app.add_url_rule('/student/<int:id>', view_func=views.student_detail, methods=['GET', 'POST'],
                 endpoint='student_detail')
app.add_url_rule('/student/<int:id>/update', view_func=views.student_update, methods=['GET', 'POST'],
                 endpoint='student_update')
app.add_url_rule('/student/<int:id>/delete', view_func=views.student_delete, methods=['GET', 'POST'],
                 endpoint='student_delete')

app.add_url_rule('/course/<int:id>', view_func=views.course_detail, methods=['GET', 'POST'],
                 endpoint='course_detail')
app.add_url_rule('/course/<int:id>/update', view_func=views.course_update, methods=['GET', 'POST'],
                 endpoint='course_update')
app.add_url_rule('/course/<int:id>/delete', view_func=views.course_delete, methods=['GET', 'POST'],
                 endpoint='course_delete')

app.add_url_rule('/mentor/<int:id>', view_func=views.mentor_detail, methods=['GET', 'POST'],
                 endpoint='mentor_detail')
app.add_url_rule('/mentor/<int:id>/update', view_func=views.mentor_update, methods=['GET', 'POST'],
                 endpoint='mentor_update')
app.add_url_rule('/mentor/<int:id>/delete', view_func=views.mentor_delete, methods=['GET', 'POST'],
                 endpoint='mentor_delete')

app.add_url_rule('/register',view_func=views.register_view,methods=['GET','POST'],endpoint='register')
app.add_url_rule('/login',view_func=views.login_view,methods=['GET','POST'],endpoint='login')
app.add_url_rule('/logout',view_func=views.logout_view,endpoint='logout')