# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioPlayer', '0008_auto_20170718_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiofile',
            name='audio',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='audiofile',
            name='image',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='member',
            name='profile_image',
            field=models.FileField(upload_to=''),
        ),
    ]
