# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-11-24 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chef', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='gallery_img',
            field=models.ImageField(upload_to='food/galley_images'),
        ),
    ]
