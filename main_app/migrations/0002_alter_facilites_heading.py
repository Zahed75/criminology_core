# Generated by Django 4.1.1 on 2022-09-16 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilites',
            name='heading',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
