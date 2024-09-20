from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    student_id = models.IntegerField(unique=True)
    date_of_birth = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Student: {self.student_id}, {self.user.first_name} {self.user.last_name}"


class Lecture(models.Model):
    staff_id = models.IntegerField(unique=True)
    date_of_birth = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Lecture: {self.staff_id}, {self.user.first_name} {self.user.last_name}"


class Semester(models.Model):
    year = models.IntegerField()
    semester = models.CharField(max_length=50)
    courses = models.ManyToManyField('Course', related_name='semesters')

    def __str__(self):
        return f"Semester: {self.year}, {self.semester}"


class Course(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Course: {self.code}, {self.name}"


class Class(models.Model):
    number = models.IntegerField(unique=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE)
    students = models.ManyToManyField('Student', related_name='classes')

    def __str__(self):
        return f"Class: {self.number}, {self.course.name}"


class CollegeDay(models.Model):
    date = models.DateField()
    class_ref = models.ForeignKey('Class', on_delete=models.CASCADE)
    students = models.ManyToManyField('Student', related_name='college_days')

    def __str__(self):
        return f"CollegeDay: {self.date}"


class Attendance(models.Model):
    ATTENDANCE_STATUS = [
        ('P', 'Present'),
        ('A', 'Absent'),
    ]
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    class_ref = models.ForeignKey('Class', on_delete=models.CASCADE)
    college_day = models.ForeignKey('CollegeDay', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=ATTENDANCE_STATUS)

    def __str__(self):
        return f"{self.student} at {self.college_day} attend {self.class_ref} by {self.status}"
