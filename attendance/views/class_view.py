from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from attendance.forms import ClassForm
from attendance.models import Class, Lecture, Course, Semester
from attendance.views import format_form_errors


class ClassListView(ListView):
    model = Class
    context_object_name = 'classes'
    template_name = 'class/dashboard_classes.html'


class ClassDetailView(DetailView):
    model = Class
    context_object_name = 'class'
    template_name = 'class/dashboard_classes_detail.html'

    def get_object(self, queryset=None):
        return Class.objects.get(pk=self.kwargs['pk'])


def class_create(request):
    errors = []
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('dashboard_classes'))
        else:
            errors = format_form_errors(form.errors)

    return render(
        request=request,
        template_name='class/dashboard_classes_create.html',
        context={
            'semesters': Semester.objects.all(),
            'lectures': Lecture.objects.all(),
            'courses': Course.objects.all(),
            'errors': errors
        },
    )

