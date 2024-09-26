from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q

from attendance.models import Semester


class SemesterForm(forms.ModelForm):
    year = forms.IntegerField(required=True)
    semester = forms.CharField(required=True)
    start_date = forms.DateField(required=True)
    end_date = forms.DateField(required=True)

    class Meta:
        model = Semester
        fields = ['year', 'semester', 'start_date', 'end_date']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date >= end_date:
            self.add_error(None, ValidationError(
                'Start date must be before end date.', code='invalid'))

            # overlapping_semesters = Semester.objects.filter(
            #     Q(start_date__range=(start_date, end_date)) | Q(end_date__range=(start_date, end_date))
            # )
            #
            # if overlapping_semesters.exists():
            #     raise ValidationError(f"This semester overlaps with an existing semester: {overlapping_semesters}")

        return cleaned_data
