# Generated by Django 3.2.5 on 2022-09-17 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherdetail',
            name='teacher_information',
            field=models.TextField(blank=True, max_length=8000, null=True),
        ),
    ]
