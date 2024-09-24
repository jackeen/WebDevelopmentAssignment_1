# Generated by Django 5.1.1 on 2024-09-24 11:13

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_alter_class_lecture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collegeday',
            name='class_ref',
        ),
        migrations.RemoveField(
            model_name='collegeday',
            name='students',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='courses',
        ),
        migrations.AddField(
            model_name='attendance',
            name='lecture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='attendance.lecture'),
        ),
        migrations.AddField(
            model_name='collegeday',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='attendance.semester'),
        ),
        migrations.AddField(
            model_name='semester',
            name='end_date',
            field=models.DateField(default=datetime.date(2024, 9, 24)),
        ),
        migrations.AddField(
            model_name='semester',
            name='start_date',
            field=models.DateField(default=datetime.date(2024, 9, 24)),
        ),
        migrations.AlterField(
            model_name='class',
            name='lecture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='attendance.lecture'),
        ),
    ]
