from django import template

from attendance.models import Attendance

register = template.Library()


@register.filter
def present_count_by_student(class_ref, student):
    return Attendance.objects.filter(class_ref=class_ref, student=student, status='P').count()


@register.filter
def absent_count_by_student(class_ref, student):
    return Attendance.objects.filter(class_ref=class_ref, student=student, status='A').count()
