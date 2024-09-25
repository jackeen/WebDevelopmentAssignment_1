"""
Views for home page and dashboard
"""
from django.shortcuts import render, redirect


def index(request):
    #if not request.user.is_authenticated:
    #    return redirect('login')

    return redirect('dashboard')


def dashboard(request):
    #if not request.user.is_authenticated:
    #    return redirect('login')

    return render(
        request=request,
        template_name='dashboard.html'
    )
