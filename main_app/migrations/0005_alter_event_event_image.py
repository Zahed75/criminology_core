# Generated by Django 3.2.5 on 2022-09-17 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_event_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(blank=True, null=True, upload_to='event'),
        ),
    ]
