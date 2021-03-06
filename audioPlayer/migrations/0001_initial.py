# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('artists', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=10)),
                ('live', models.BooleanField()),
            ],
        ),
    ]
