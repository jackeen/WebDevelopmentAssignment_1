from django import forms

from attendance.models import Lecture


class LectureCreateForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['staff_id', 'date_of_birth']


class LectureUpdateForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['staff_id', 'date_of_birth']
