# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioPlayer', '0009_auto_20170719_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiofile',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
