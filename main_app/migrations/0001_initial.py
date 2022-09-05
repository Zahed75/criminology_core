# Generated by Django 4.0.4 on 2022-09-05 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=500)),
                ('course_image', models.ImageField(upload_to='course_images')),
                ('course_descriptions', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]