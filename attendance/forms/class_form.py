from django import forms

from attendance.models import Class


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['number', 'course', 'lecture', 'semester']
        widgets = {
            'number': forms.NumberInput(),
            'course': forms.Select(),
            'lecture': forms.Select(),
            'semester': forms.Select(),
        }
