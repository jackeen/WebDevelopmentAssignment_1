from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect


def login_custom(request):
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
