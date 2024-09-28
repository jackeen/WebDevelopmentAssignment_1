from django import forms

from attendance.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'date_of_birth']