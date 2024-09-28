from datetime import date

import pandas as pd
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
            form_student: Student = student_form.save(commit=False)
            form_user: User = user_form.save(commit=False)

            # create_user can hide raw password
            user = User.objects.create_user(
                username=form_user.username,
                first_name=form_user.first_name,
                last_name=form_user.last_name,
                email=form_user.email,
                password=form_student.date_of_birth.strftime('%Y%m%d')
            )
            user.save()

            group, _ = Group.objects.get_or_create(name=GROUP_STUDENT)
            group.user_set.add(user)
            group.save()

            form_student.user = user
            form_student.save()
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


def student_upload(request):
    if request.method == 'POST':
        file = request.FILES['file']
        if file:
            excel_file = pd.read_excel(file)
            data = pd.DataFrame(excel_file)
            username_list = data['username'].values.tolist()
            email_list = data['email'].values.tolist()
            first_name_list = data['first_name'].values.tolist()
            last_name_list = data['last_name'].values.tolist()
            date_of_birth_list = data['date_of_birth'].values.tolist()
            student_id_list = data['student_id'].values.tolist()
            for i in range(len(username_list)):
                username = username_list[i]
                email = email_list[i]
                first_name = first_name_list[i]
                last_name = last_name_list[i]
                date_of_birth = date.fromisoformat(date_of_birth_list[i])
                student_id = student_id_list[i]

                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=date_of_birth.strftime('%Y%m%d')
                )
                user.save()

                group, _ = Group.objects.get_or_create(name=GROUP_STUDENT)
                group.user_set.add(user)
                group.save()

                student = Student.objects.create(
                    user=user,
                    date_of_birth=date_of_birth,
                    student_id=student_id
                )
                student.save()

        return redirect('dashboard_students')

    return render(
        request=request,
        template_name='student/dashboard_students_upload.html'
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
