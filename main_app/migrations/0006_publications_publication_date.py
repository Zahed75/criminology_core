# Generated by Django 3.2.5 on 2022-09-17 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_publicationdetail_publications'),
    ]

    operations = [
        migrations.AddField(
            model_name='publications',
            name='publication_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
