from datetime import timedelta

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from attendance.forms import SemesterForm
from attendance.models import Semester, Class, CollegeDay
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        semester = self.get_object()
        context['classes'] = Class.objects.filter(semester=semester)
        return context


def generate_college_days(semester_instance):
    date_list = []
    current_date = semester_instance.start_date
    while current_date <= semester_instance.end_date:
        date_list.append(current_date)
        collegeDay, _ = CollegeDay.objects.get_or_create(
            semester=semester_instance,
            date=current_date,
        )
        collegeDay.save()
        current_date += timedelta(days=1)


def semester_create(request):
    errors = []
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            semester_instance = form.save()
            generate_college_days(semester_instance)

            return redirect(reverse_lazy('dashboard_semesters'))
        else:
            errors = format_form_errors(form.errors)

    return render(
        request=request,
        template_name='semesters/dashboard_semesters_create.html',
        context={'errors': errors},
    )


def semester_update(request, pk):
    errors = []
    semester = Semester.objects.get(id=pk)
    if request.method == 'POST':
        form = SemesterForm(request.POST, instance=semester)
        if form.is_valid():
            semester_instance = form.save()
            generate_college_days(semester_instance)
            return redirect(reverse_lazy('dashboard_semesters'))
        else:
            errors = format_form_errors(form.errors)

    return render(
        request=request,
        template_name='semesters/dashboard_semesters_update.html',
        context={
            'semester': semester,
            'errors': errors
        },
    )


class SemesterDeleteView(DeleteView):
    model = Semester
    template_name = 'semesters/dashboard_semesters_delete_confirm.html'
    success_url = reverse_lazy('dashboard_semesters')
