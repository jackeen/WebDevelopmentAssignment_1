from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from attendance.forms.course_from import CourseForm
from attendance.models import Course, Class
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

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        course = self.get_object()
        content['classes'] = Class.objects.filter(course=course).all()
        return content


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


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course/dashboard_courses_delete_confirm.html'
    success_url = reverse_lazy('dashboard_courses')

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        course = self.get_object()
        content['classes'] = Class.objects.filter(course=course).all()
        return content
