# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 14:19
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('Assign_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Assignment_File', models.FileField(default='hello.pdf', upload_to='AssignmentsFolder/')),
                ('Start_Time', models.DateTimeField(default=django.utils.timezone.now)),
                ('End_Time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_time', models.DateTimeField(default=datetime.datetime(2017, 10, 12, 14, 19, 17, 874798))),
                ('Marked', models.CharField(default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance_Session',
            fields=[
                ('Session_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Date_time', models.DateTimeField(default=datetime.datetime(2017, 10, 12, 14, 19, 17, 874227))),
                ('Status', models.IntegerField()),
                ('Location', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('Course_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Course_Name', models.CharField(default='', max_length=50)),
                ('Course_description', models.CharField(default='', max_length=255)),
                ('Course_Credits', models.IntegerField()),
                ('Course_Year', models.IntegerField()),
                ('Course_Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Dept_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Dept_Name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('Doc_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Doc_Name', models.CharField(default='', max_length=50)),
                ('Document', models.FileField(upload_to='uploaded_file/')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('Event_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Event_Date', models.DateField()),
                ('Event_Name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Instructors_Courses',
            fields=[
                ('IC_id', models.AutoField(primary_key=True, serialize=False)),
                ('Start_Date', models.DateField(verbose_name=datetime.date(2017, 1, 1))),
                ('End_Date', models.DateField(verbose_name=datetime.date(2017, 1, 1))),
                ('Course_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='LoginTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.CharField(default='', max_length=12)),
                ('Start_time', models.DateTimeField(default=datetime.datetime(2017, 10, 12, 14, 19, 17, 876140))),
                ('End_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('Person_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Department')),
                ('LDAP', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('Role_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Role_name', models.CharField(default='', max_length=50)),
                ('level', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_Year', models.IntegerField(default=2013)),
                ('End_Year', models.IntegerField(default=2017)),
                ('Student_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Personnel')),
            ],
        ),
        migrations.CreateModel(
            name='Students_Courses',
            fields=[
                ('SC_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Reg_Date', models.DateField(verbose_name=datetime.date(2017, 1, 1))),
                ('Course_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses')),
                ('Student_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Personnel')),
            ],
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('Sub_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Sub_Time', models.DateTimeField(default=django.utils.timezone.now)),
                ('Sub_Status', models.BooleanField(default=False)),
                ('Score', models.FloatField(default=0)),
                ('Assign_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Assignment')),
                ('Student_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Personnel')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('T_ID', models.AutoField(primary_key=True, serialize=False)),
                ('T_days', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('Start_time', models.TimeField(auto_now_add=True)),
                ('End_time', models.TimeField(auto_now_add=True)),
                ('Class_ID', models.CharField(default='', max_length=10)),
                ('Course_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses')),
            ],
        ),
        migrations.AddField(
            model_name='personnel',
            name='Role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Roles'),
        ),
        migrations.AddField(
            model_name='instructors_courses',
            name='Inst_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Personnel'),
        ),
        migrations.AddField(
            model_name='attendance_session',
            name='Course_Slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Timetable'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='ASession_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Attendance_Session'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='Student_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Personnel'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='Course_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
    ]
