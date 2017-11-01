# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='id',
        ),
        migrations.RemoveField(
            model_name='items',
            name='id',
        ),
        migrations.AddField(
            model_name='categories',
            name='ID',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='items',
            name='ID',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]