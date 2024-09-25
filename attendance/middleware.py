from django.shortcuts import redirect
from django.urls import resolve
# from django.http import Http404


class AccessLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        view_name = resolve(request.path).view_name
        if not request.user.is_authenticated:
            if view_name != 'login':
                return redirect('login')

        # lecture
        # if view_name.startswith('dashboard_students'):
        #     if view_name != 'error_403':
        #         return redirect('error_403')


        # student


        response = self.get_response(request)
        return response
