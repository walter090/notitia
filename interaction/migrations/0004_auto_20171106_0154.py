# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 01:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0003_auto_20171105_0607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='content_body',
        ),
    ]