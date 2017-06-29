# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-28 22:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appt_time',
            field=models.TimeField(default=datetime.datetime(2017, 6, 28, 22, 15, 38, 438702)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.TextField(default='Pending'),
        ),
    ]
