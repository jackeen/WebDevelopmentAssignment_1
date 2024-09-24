from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from attendance.models import Lecture


class LectureListView(ListView):
    model = Lecture
    context_object_name = 'lectures'
    template_name = 'lecture/dashboard_lectures.html'


class LectureDetailView(DetailView):
    model = Lecture
    context_object_name = 'lecture'
    template_name = 'lecture/dashboard_lectures_detail.html'

    def get_object(self, queryset=None):
        return Lecture.objects.get(staff_id=self.kwargs['pk'])


def lecture_create(request):
    if request.method == 'POST':
        staff_id = request.POST['staff_id']
        date_of_birth = request.POST['date_of_birth']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user_name = request.POST['user_name']
        password = date_of_birth.replace('-', '')

        user = User(
            username=user_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.save()

        lecture = Lecture(
            staff_id=staff_id,
            date_of_birth=date_of_birth,
            user=user
        )
        lecture.save()

        return redirect('dashboard_lectures')

    return render(
        request=request,
        template_name='lecture/dashboard_lectures_create.html'
    )


class LectureDeleteView(DeleteView):
    model = Lecture
    template_name = 'lecture/dashboard_lectures_delete_confirm.html'
    success_url = reverse_lazy('dashboard_lectures')

    def get_object(self, queryset=None):
        return Lecture.objects.get(staff_id=self.kwargs['pk'])
