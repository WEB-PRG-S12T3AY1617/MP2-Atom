# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 04:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprof', '0014_auto_20170811_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='op',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
