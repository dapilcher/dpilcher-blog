# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]