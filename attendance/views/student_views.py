from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView

from attendance.models import Student

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'dashboard_students.html'


class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'dashboard_students_detail.html'

    def get_object(self, queryset=None):
        return Student.objects.get(student_id=self.kwargs['pk'])


def student_create(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        username = request.POST['user_name']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        password = date_of_birth.replace('-', '')

        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.save()

        student = Student(
            student_id=student_id,
            user=user,
            date_of_birth=date_of_birth,
        )
        student.save()

        return redirect('dashboard_students')

    return render(
        request=request,
        template_name='dashboard_students_create.html',
        context={

        }
    )