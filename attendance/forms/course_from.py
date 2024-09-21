from django import forms

from attendance.models import Course


class CourseForm(forms.ModelForm):
    code = forms.CharField(required=True)
    name = forms.CharField(required=True)

    class Meta:
        model = Course
        fields = ['code', 'name']
