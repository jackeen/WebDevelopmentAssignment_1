from django.shortcuts import render


def error_403_view(request):
    return render(
        request=request,
        template_name='errors/403.html',
    )