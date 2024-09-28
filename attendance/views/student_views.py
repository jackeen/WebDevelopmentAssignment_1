from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from attendance.forms import UserCreateForm, UserUpdateForm
from attendance.forms.student_form import StudentForm
from attendance.models import Student, GROUP_STUDENT
from attendance.views import format_form_errors


class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'student/dashboard_students.html'


class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'student/dashboard_students_detail.html'

    def get_object(self, queryset=None):
        return Student.objects.get(id=self.kwargs['pk'])


def student_create(request):
    errors = []
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        student_form = StudentForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            student: Student = student_form.save(commit=False)
            user: User = user_form.save(commit=False)
            user.password = student.date_of_birth.strftime('%Y%m%d')
            user.save()

            group, _ = Group.objects.get_or_create(name=GROUP_STUDENT)
            group.user_set.add(user)
            group.save()

            student.user = user
            student.save()
            return redirect('dashboard_students')
        else:
            errors = user_form.errors
            errors.update(student_form.errors)
            errors = format_form_errors(errors)

    return render(
        request=request,
        template_name='student/dashboard_students_create.html',
        context={
            'errors': errors,
        }
    )


def student_update(request, pk):
    errors = []
    student = Student.objects.get(id=pk)
    user = student.user
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        student_form = StudentForm(request.POST, instance=student)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            return redirect('dashboard_students')
        else:
            errors = student_form.errors
            errors.update(user_form.errors)
            errors = format_form_errors(errors)

    return render(
        request=request,
        template_name='student/dashboard_students_update.html',
        context={
            'errors': errors,
            'student': student,
        }
    )


class StudentDeleteView(DeleteView):
    model = Student
    context_object_name = 'student'
    template_name = 'student/dashboard_students_delete_confirm.html'
    success_url = reverse_lazy('dashboard_students')

    def get_object(self, queryset=None):
        return Student.objects.get(student_id=self.kwargs['pk'])
