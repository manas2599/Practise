# Generated by Django 4.1.7 on 2023-04-12 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0003_alter_courses_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(default='Course 1', max_length=100)),
                ('Assignment', models.CharField(max_length=600)),
                ('date', models.DateField()),
            ],
        ),
    ]
