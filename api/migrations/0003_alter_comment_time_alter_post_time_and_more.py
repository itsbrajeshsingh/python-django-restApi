# Generated by Django 4.1.3 on 2022-11-29 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_comment_time_alter_post_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 29, 16, 19, 30, 707737, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 29, 16, 19, 30, 707737, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 29, 16, 19, 30, 707737, tzinfo=datetime.timezone.utc)),
        ),
    ]
