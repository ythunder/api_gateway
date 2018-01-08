# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0002_auto_20180106_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acllist',
            name='vers_id',
        ),
        migrations.RemoveField(
            model_name='apiinfo',
            name='api_id',
        ),
        migrations.RemoveField(
            model_name='versinfo',
            name='vers_id',
        ),
        migrations.AddField(
            model_name='apiinfo',
            name='version',
            field=models.CharField(default=None, max_length=8),
            preserve_default=False,
        ),
    ]