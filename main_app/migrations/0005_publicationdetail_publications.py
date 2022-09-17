# Generated by Django 3.2.5 on 2022-09-17 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20220918_0230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('descriptions', models.TextField(blank=True, max_length=8000, null=True)),
                ('image', models.ImageField(upload_to='chairman')),
            ],
        ),
        migrations.CreateModel(
            name='PublicationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(blank=True, max_length=300, null=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PublicationDetail', to='main_app.publications')),
            ],
        ),
    ]