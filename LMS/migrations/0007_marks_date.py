# Generated by Django 4.2 on 2023-04-13 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0006_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='date',
            field=models.DateField(default=datetime.date(2023, 4, 13)),
        ),
    ]