# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprof', '0007_post_post_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
    ]
