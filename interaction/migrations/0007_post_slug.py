# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0006_auto_20171107_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='slug'),
        ),
    ]
