
from django.contrib import admin
from django.urls import path

from onlineapp.API_views import college_list, college_detail, college_students, student_detail
from onlineapp.views import *
from django.conf import settings
from django.conf.urls import include, url

#from onlineapp.views.auth import CreateUserView  # commented out on 3/7/2018 7:22 PM as already imported all from views above

app_name = "onlineapp"
''' 
    path('hello/',hello),
    path('college_details/',college_details),
    path('index/',index),
    path('college_details_template/',college_details_template),
    path('student-list/',student_details_with_college_name),
    path('student-list/<int:num>/',student_individual_details),
    path('student-list-button/',student_total_with_button),
    path('student-list/<clg>', student_college_vise_details),
    path('test-session-with-counter/', counter),
    path('test-session/', url_hit_count_with_session)
'''

urlpatterns = [
    path('colleges/',CollegeView.as_view(),name='bootstrap.html'),
    path(r'colleges/<int:pk>/',CollegeDetailsView.as_view(),name='redirect_page'),
    path('addcollege/',createCollegeView.as_view(),name='colleges_html.html'),
    path('colleges/<int:pk>/addstudent/', createStudentView.as_view(), name='student_form.html1'),
    path('colleges/<int:clg_id>/<int:pk>/editstudent/',EditStudentView.as_view(),name = 'student_form.html2'),
    path('colleges/<int:clg_id>/<int:pk>/deletestudent/',DeleteStudentView.as_view(),name = 'student_form.html3'),
    path('colleges/<int:pk>/editcollege/',EditCollegeView.as_view(),name = "edit_college"),
    path('colleges/addcollege/',CreateCollegeView.as_view(),name="add_college"),
    path('signup/',CreateUserView.as_view(),name="sign_up"),
    path('login/',LoginView.as_view(),name = 'login_into'),
    path('logout/',LogoutView,name='logout_into'),
    path('api/colleges/<int:pk>/students/', college_students.as_view(), name='college_students'),
    path('api/colleges/<int:pk>/students/<int:id>/',student_detail.as_view(),name = 'student_detail'),
    path('api/colleges/',college_list,name='colleges_list'),
    path('api/colleges/<int:pk>/',college_detail,name='college_detail'),
    #path('api/colleges/<int:c_pk>/studens/',)
]
