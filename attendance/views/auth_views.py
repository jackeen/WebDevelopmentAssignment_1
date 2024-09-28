from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect

from attendance.views import format_form_errors


def login_custom(request):
    errors = []
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard_home')
        else:
            errors = format_form_errors(form.errors)

    return render(
        request=request,
        template_name='login.html',
        context={'errors': errors}
    )


def logout_custom(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
