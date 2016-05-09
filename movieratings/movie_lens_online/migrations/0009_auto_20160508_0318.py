# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-08 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_lens_online', '0008_rater_auth_u'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rater',
            name='auth_u',
        ),
        migrations.AddField(
            model_name='rating',
            name='movie_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]