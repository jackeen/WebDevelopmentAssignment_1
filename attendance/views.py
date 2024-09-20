from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView

from attendance.models import Student, Lecture


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return redirect('dashboard')


def login_custom(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='login.html',
        context={'form': form}
    )


def logout_custom(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(
        request=request,
        template_name='dashboard.html'
    )


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


class LectureListView(ListView):
    model = Lecture
    context_object_name = 'lectures'
    template_name = 'dashboard_lectures.html'


class LectureDetailView(DetailView):
    model = Lecture
    context_object_name = 'lecture'
    template_name = 'dashboard_lectures_detail.html'

    def get_object(self, queryset=None):
        return Lecture.objects.get(staff_id=self.kwargs['pk'])


def lecture_create(request):
    if request.method == 'POST':
        staff_id = request.POST['staff_id']
        date_of_birth = request.POST['date_of_birth']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user_name = request.POST['user_name']
        password = date_of_birth.replace('-', '')

        user = User(
            username=user_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.save()

        lecture = Lecture(
            staff_id=staff_id,
            date_of_birth=date_of_birth,
            user=user
        )
        lecture.save()

        return redirect('dashboard_lectures')

    return render(
        request=request,
        template_name='dashboard_lectures_create.html'
    )
