"""
Views for home page and dashboard
"""
from django.shortcuts import render, redirect

from attendance.models import GROUP_LECTURE, GROUP_STUDENT, Class, Student


def index(request):
    return redirect('dashboard_home')


def dashboard(request):
    if request.user.groups.filter(name=GROUP_LECTURE).exists():
        lecture_classes = Class.objects.filter(lecture__user=request.user).all()
        return render(
            request=request,
            template_name='dashboard.html',
            context={
                'classes': lecture_classes
            }
        )

    # not???????
    if request.user.groups.filter(name=GROUP_STUDENT).exists():
        classes = Class.objects.filter(students__user=request.user).all()
        return render(
            request=request,
            template_name='dashboard.html',
            context={
                'student': Student.objects.filter(user=request.user).first(),
                'classes': classes
            }
        )

    return render(
        request=request,
        template_name='dashboard.html',
    )
