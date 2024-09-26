"""
attendance URL Configuration

"""
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from attendance import views

urlpatterns = [
    path('', views.index, name='index'),

    # customer login views for common UI
    path('login', views.login_custom, name='login'),
    path('logout', views.logout_custom, name='logout'),

    # system login views
    path("login_system", LoginView.as_view(), name="login_system"),
    path("logout_system", LogoutView.as_view(), name="logout_system"),

    path('dashboard', views.dashboard, name='dashboard_home'),

    path('dashboard/students', views.StudentListView.as_view(), name='dashboard_students'),
    path('dashboard/students/<int:pk>', views.StudentDetailView.as_view(), name='dashboard_students_detail'),
    path('dashboard/students/create', views.student_create, name='dashboard_students_create'),
    path('dashboard/students/delete/<int:pk>', views.StudentDeleteView.as_view(), name='dashboard_students_delete'),

    path('dashboard/lectures', views.LectureListView.as_view(), name='dashboard_lectures'),
    path('dashboard/lectures/<int:pk>', views.LectureDetailView.as_view(), name='dashboard_lectures_detail'),
    path('dashboard/lectures/create', views.lecture_create, name='dashboard_lectures_create'),
    path('dashboard/lectures/delete/<int:pk>', views.LectureDeleteView.as_view(), name='dashboard_lectures_delete'),

    path('dashboard/semesters', views.SemesterListView.as_view(), name='dashboard_semesters'),
    path('dashboard/semesters/<int:pk>', views.SemesterDetailView.as_view(), name='dashboard_semesters_detail'),
    path('dashboard/semesters/create', views.semester_create, name='dashboard_semesters_create'),
    path('dashboard/semesters/delete/<int:pk>', views.SemesterDeleteView.as_view(), name='dashboard_semesters_delete'),

    path('dashboard/courses', views.CourseListView.as_view(), name='dashboard_courses'),
    path('dashboard/courses/<int:pk>', views.CourseDetailView.as_view(), name='dashboard_courses_detail'),
    path('dashboard/courses/create', views.course_create, name='dashboard_courses_create'),
    path('dashboard/courses/delete/<int:pk>', views.CourseDeleteView.as_view(), name='dashboard_courses_delete'),

    path('dashboard/classes', views.ClassListView.as_view(), name='dashboard_classes'),
    path('dashboard/classes/<int:pk>', views.ClassDetailView.as_view(), name='dashboard_classes_detail'),
    path('dashboard/classes/create', views.class_create, name='dashboard_classes_create'),
    path('dashboard/classes/delete/<int:pk>', views.ClassDeleteView.as_view(), name='dashboard_classes_delete'),
    path('dashboard/classes/assign/lecture/<int:class_id>',
         views.class_assign_lecture,
         name='dashboard_classes_assign_lecture'),
    path('dashboard/classes/assign/students/<int:class_id>',
         views.class_assign_students,
         name='dashboard_classes_assign_students'),

    path('dashboard/attendance/manage/<int:class_id>',
         views.attendance_manage,
         name='dashboard_attendance_manage'),

    path('dashboard/attendance/confirm/<int:class_id>/student/<int:student_id>/<str:status>',
         views.attendance_confirm,
         name='dashboard_attendance_confirm'),

    path('error/403', views.error_403_view, name='error_403'),
]
