# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 22:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_lens_online', '0010_auto_20160509_0617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='movie_name',
        ),
    ]
