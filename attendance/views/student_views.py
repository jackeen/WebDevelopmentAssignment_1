from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from attendance.models import Student, GROUP_STUDENT


class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'student/dashboard_students.html'


class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'student/dashboard_students_detail.html'

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

        group, _ = Group.objects.get_or_create(name=GROUP_STUDENT)
        group.user_set.add(user)
        group.save()

        student = Student(
            student_id=student_id,
            user=user,
            date_of_birth=date_of_birth,
        )
        student.save()

        return redirect('dashboard_students')

    return render(
        request=request,
        template_name='student/dashboard_students_create.html',
        context={

        }
    )


class StudentDeleteView(DeleteView):
    model = Student
    context_object_name = 'student'
    template_name = 'student/dashboard_students_delete_confirm.html'
    success_url = reverse_lazy('dashboard_students')

    def get_object(self, queryset=None):
        return Student.objects.get(student_id=self.kwargs['pk'])
