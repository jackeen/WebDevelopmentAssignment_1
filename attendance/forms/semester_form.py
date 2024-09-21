from django import forms
from attendance.models import Semester


class SemesterForm(forms.ModelForm):
    year = forms.IntegerField(required=True)
    semester = forms.CharField(required=True)

    class Meta:
        model = Semester
        fields = ['year', 'semester']
