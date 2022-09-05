# Generated by Django 4.0.4 on 2022-09-05 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_course_class_durations_course_class_size_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_instructor', models.CharField(blank=True, max_length=200, null=True)),
                ('instructor_fb', models.URLField(blank=True, max_length=20, null=True)),
                ('instructor_twitter', models.URLField(blank=True, max_length=20, null=True)),
                ('course_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courseDetails', to='main_app.course')),
            ],
        ),
    ]
