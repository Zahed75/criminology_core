# Generated by Django 3.2.5 on 2022-09-17 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_teacherdetail_teacher_information'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherdetail',
            name='FacebookLink',
        ),
        migrations.RemoveField(
            model_name='teacherdetail',
            name='TwitterLink',
        ),
        migrations.AddField(
            model_name='teachersection',
            name='FacebookLink',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teachersection',
            name='TwitterLink',
            field=models.URLField(blank=True, null=True),
        ),
    ]
