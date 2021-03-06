# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-08 08:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_remove_studentform_your_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentform',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 6, 8, 8, 34, 16, 516449, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentform',
            name='your_email',
            field=models.EmailField(max_length=254),
        ),
    ]
