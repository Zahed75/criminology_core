# Generated by Django 3.2.5 on 2022-09-17 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20220918_0058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacherdetail',
            old_name='TeacherName',
            new_name='teacher_name',
        ),
        migrations.RenameField(
            model_name='teachersection',
            old_name='TeacherName',
            new_name='teacher_name',
        ),
    ]