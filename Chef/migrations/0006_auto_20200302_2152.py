# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-03-02 18:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Chef', '0005_auto_20200302_2110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='text',
            new_name='message',
        ),
    ]
