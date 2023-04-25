# Generated by Django 4.2 on 2023-04-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0005_remove_assignment_assignment_assignment_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('semester', models.CharField(default='Semester 1', max_length=15)),
                ('course1', models.CharField(max_length=500)),
                ('mark1', models.CharField(max_length=100)),
                ('course2', models.CharField(max_length=500)),
                ('mark2', models.CharField(max_length=100)),
                ('course3', models.CharField(max_length=500)),
                ('mark3', models.CharField(max_length=100)),
                ('course4', models.CharField(max_length=500)),
                ('mark4', models.CharField(max_length=100)),
                ('course5', models.CharField(max_length=500)),
                ('mark5', models.CharField(max_length=100)),
                ('course6', models.CharField(max_length=500)),
                ('mark6', models.CharField(max_length=100)),
            ],
        ),
    ]
