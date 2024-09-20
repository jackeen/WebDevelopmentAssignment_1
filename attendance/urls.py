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

    path('dashboard', views.dashboard, name='dashboard'),

    path('dashboard/students', views.StudentListView.as_view(), name='dashboard_students'),
    path('dashboard/students/<int:pk>', views.StudentDetailView.as_view(), name='dashboard_students_detail'),
    path('dashboard/students/create', views.student_create, name='dashboard_students_create'),
]
