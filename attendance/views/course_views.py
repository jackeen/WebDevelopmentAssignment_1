from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from attendance.forms.course_from import CourseForm
from attendance.models import Course
from attendance.views import format_form_errors


class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'course/dashboard_courses.html'


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'course/dashboard_courses_detail.html'

    def get_object(self, queryset=None):
        return Course.objects.get(pk=self.kwargs['pk'])


def course_create(request):
    errors = []
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            redirect(reverse_lazy('dashboard_courses'))
        else:
            errors = format_form_errors(form.errors)

    return render(
        request=request,
        template_name='course/dashboard_courses_create.html',
        context={'errors': errors}
    )