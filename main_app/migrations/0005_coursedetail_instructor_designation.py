# Generated by Django 4.0.4 on 2022-09-05 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_coursedetails_coursedetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetail',
            name='instructor_designation',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
    ]
