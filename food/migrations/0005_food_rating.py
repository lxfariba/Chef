# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-03-26 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_foodquantity_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='rating',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
