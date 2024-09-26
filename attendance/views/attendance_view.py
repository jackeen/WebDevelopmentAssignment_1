from datetime import datetime

from django.shortcuts import render, redirect

from attendance.models import Class, Attendance, Student, Lecture, CollegeDay


def attendance_manage(request, class_id):
    class_ref = Class.objects.get(id=class_id)
    students = class_ref.students.all()

    attendance_dict = {}
    for student in students:
        present_count = Attendance.objects.filter(
            student=student,
            class_ref=class_ref,
            status='P'
        ).count()
        absent_count = Attendance.objects.filter(
            student=student,
            class_ref=class_ref,
            status='A'
        ).count()
        attendance_dict[student.id] = {
            'present_count': present_count,
            'absent_count': absent_count
        }

    return render(
        request=request,
        template_name='attendance/dashboard_attendance_manage.html',
        context={
            'class': class_ref,
            'attendance_dict': attendance_dict
        }
    )


def attendance_confirm(request, class_id, student_id, status):
    class_ref = Class.objects.get(id=class_id)
    student = Student.objects.get(id=student_id)
    lecture = Lecture.objects.filter(user=request.user).first()
    semester = class_ref.semester

    college_days = CollegeDay.objects.filter(
        date__gte=semester.start_date,
        date__lte=semester.end_date
    ).all()

    if request.method == 'POST':
        select_day_str = request.POST.get('college_day')
        select_date = datetime.strptime(select_day_str, "%Y-%m-%d").date()
        college_day = CollegeDay.objects.filter(date=select_date).first()

        attendance, _ = Attendance.objects.get_or_create(
            student=student,
            class_ref=class_ref,
            lecture=lecture,
            college_day=college_day
        )
        attendance.status = status
        attendance.save()
        return redirect('dashboard_attendance_manage', class_id)

    return render(
        request=request,
        template_name='attendance/dashboard_attendance_confirm.html',
        context={
            'class': class_ref,
            'student': student,
            'lecture': lecture,
            'college_days': college_days,
            'status': status
        }
    )
