# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 04:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Email',
            new_name='MailingListSubscriber',
        ),
    ]
