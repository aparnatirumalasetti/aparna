# Generated by Django 3.2.5 on 2021-08-18 07:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_post_student_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='student_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 18, 7, 45, 9, 127072, tzinfo=utc)),
        ),
    ]