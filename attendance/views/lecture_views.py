from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from attendance.forms import UserUpdateForm, LectureUpdateForm, UserCreateForm, LectureCreateForm
from attendance.models import Lecture, GROUP_LECTURE
from attendance.views import format_form_errors


class LectureListView(ListView):
    model = Lecture
    context_object_name = 'lectures'
    template_name = 'lecture/dashboard_lectures.html'


class LectureDetailView(DetailView):
    model = Lecture
    context_object_name = 'lecture'
    template_name = 'lecture/dashboard_lectures_detail.html'

    def get_object(self, queryset=None):
        return Lecture.objects.get(id=self.kwargs['pk'])


def lecture_create(request):
    errors = []
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        lecture_form = LectureCreateForm(request.POST)
        if user_form.is_valid() and lecture_form.is_valid():
            user: User = user_form.save(commit=False)
            lecture: Lecture = lecture_form.save(commit=False)

            user.password = lecture.date_of_birth.strftime('%Y%m%d')
            user.save()

            group, _ = Group.objects.get_or_create(name=GROUP_LECTURE)
            group.user_set.add(user)
            group.save()

            lecture.user = user
            lecture.save()
            return redirect('dashboard_lectures')
        else:
            errors = lecture_form.errors
            errors.update(user_form.errors)
            errors = format_form_errors(errors)

    return render(
        request=request,
        template_name='lecture/dashboard_lectures_create.html',
        context={
            'errors': errors
        }
    )


def lecture_update(request, pk):
    lecture = Lecture.objects.get(id=pk)
    user = lecture.user
    errors = []
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        lecture_form = LectureUpdateForm(request.POST, instance=lecture)
        if user_form.is_valid() and lecture_form.is_valid():
            user = user_form.save()
            lecture = lecture_form.save(commit=False)
            lecture.user = user
            lecture.save()
            return redirect('dashboard_lectures')
        else:
            errors = lecture_form.errors
            errors.update(user_form.errors)
            errors = format_form_errors(errors)

    return render(
        request=request,
        template_name='lecture/dashboard_lectures_update.html',
        context={
            'lecture': lecture,
            'errors': errors
        }
    )


class LectureDeleteView(DeleteView):
    model = Lecture
    template_name = 'lecture/dashboard_lectures_delete_confirm.html'
    success_url = reverse_lazy('dashboard_lectures')

    def get_object(self, queryset=None):
        return Lecture.objects.get(id=self.kwargs['pk'])
