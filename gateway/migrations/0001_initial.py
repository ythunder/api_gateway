# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AclList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vers_id', models.IntegerField()),
                ('match_req', models.CharField(max_length=128)),
                ('auth_type', models.IntegerField()),
                ('cre_time', models.TimeField(max_length=32)),
                ('upd_time', models.TimeField(max_length=32)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ApiInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.IntegerField()),
                ('api_name', models.CharField(max_length=16)),
                ('api_desc', models.CharField(max_length=256)),
                ('usr_id', models.IntegerField()),
                ('cre_time', models.TimeField(max_length=32)),
                ('upd_time', models.TimeField(max_length=32)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VersInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vers_id', models.IntegerField()),
                ('vers_name', models.CharField(max_length=16)),
                ('api_id', models.IntegerField()),
                ('ser_url', models.URLField()),
                ('auth_type', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
    ]
