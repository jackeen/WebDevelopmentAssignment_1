from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

from attendance.forms import ClassForm
from attendance.models import Class, Lecture, Course, Semester, Student
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


class ClassDeleteView(DeleteView):
    model = Class
    template_name = 'class/dashboard_classes_delete_confirm.html'
    success_url = reverse_lazy('dashboard_classes')


def class_assign_lecture(request, class_id):
    if request.method == 'POST':
        class_ref = Class.objects.get(id=class_id)
        lecture = Lecture.objects.filter(id=request.POST['lecture']).first()
        class_ref.lecture = lecture
        class_ref.save()
        return redirect(reverse_lazy('dashboard_classes'))

    return render(
        request=request,
        template_name='class/dashboard_classes_assign_lecture.html',
        context={
            'class': Class.objects.get(id=class_id),
            'lectures': Lecture.objects.all()
        }
    )


def class_assign_students(request, class_id):
    if request.method == 'POST':
        operator = request.POST['operator']
        class_ref = Class.objects.get(id=class_id)
        students_list = request.POST.getlist('student')

        if operator == 'add':
            for student in students_list:
                class_ref.students.add(student)
        elif operator == 'remove':
            for student in students_list:
                class_ref.students.remove(student)

        class_ref.save()
        return redirect(reverse_lazy('dashboard_classes_assign_students', kwargs={'class_id': class_id}))

    return render(
        request=request,
        template_name='class/dashboard_classes_assign_students.html',
        context={
            'class': Class.objects.get(id=class_id),
            'selected_students': Class.objects.get(id=class_id).students.all(),
            'students': Student.objects.all(),
        }
    )




