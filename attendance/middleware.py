from django.shortcuts import redirect
from django.urls import resolve
# from django.http import Http404


from attendance.models import GROUP_LECTURE, GROUP_STUDENT


class AccessLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        view_name = resolve(request.path).view_name
        if not request.user.is_authenticated:
            if view_name != 'login':
                return redirect('login')

        lecture = request.user.groups.filter(name=GROUP_LECTURE)
        if lecture.count() > 0 and not view_name.startswith('dashboard_attendance'):
            if view_name != 'logout' and view_name != 'login' and view_name != 'dashboard_home':
                if view_name != 'error_403':
                    return redirect('error_403')

        student = request.user.groups.filter(name=GROUP_STUDENT)
        if student.count() > 0:
            if view_name != 'logout' and view_name != 'login' and view_name != 'dashboard_home':
                if view_name != 'error_403':
                    return redirect('error_403')

        response = self.get_response(request)
        return response
