"""
Views for home page and dashboard
"""
from django.shortcuts import render, redirect

from attendance.models import GROUP_LECTURE, GROUP_STUDENT, Class


def index(request):
    #if not request.user.is_authenticated:
    #    return redirect('login')

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
        attendances = {}
        return render(
            request=request,
            template_name='dashboard.html',
            context={
                'attendances': attendances
            }
        )

    return render(
        request=request,
        template_name='dashboard.html',
    )
