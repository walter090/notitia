# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0008_auto_20171107_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tldr',
            field=models.TextField(blank=True, verbose_name='tl;dr'),
        ),
    ]
