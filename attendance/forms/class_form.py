from django import forms

from attendance.models import Class, Lecture


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['number', 'course', 'semester']


class ClassStudentForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['students']
