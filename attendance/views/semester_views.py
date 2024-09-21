from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from attendance.forms import SemesterForm
from attendance.models import Semester
from attendance.views.utils import format_form_errors


class SemesterListView(ListView):
    model = Semester
    context_object_name = 'semesters'
    template_name = 'semesters/dashboard_semesters.html'


class SemesterDetailView(DetailView):
    model = Semester
    context_object_name = 'semester'
    template_name = 'semesters/dashboard_semesters_detail.html'

    def get_object(self, queryset=None):
        return Semester.objects.get(id=self.kwargs['pk'])


# class SemesterCreateView(CreateView):
#     model = Semester
#     form_class = SemesterForm
#     template_name = 'semesters/dashboard_semesters_create.html'
#     success_url = reverse_lazy('dashboard_semesters')


def semester_create(request):
    errors = ""
    if request.method == 'POST':
        form = SemesterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect(reverse_lazy('dashboard_semesters'))
        else:
            errors = format_form_errors(form.errors)

    return render(
        request=request,
        template_name='semesters/dashboard_semesters_create.html',
        context={'errors': errors},
    )