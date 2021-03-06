# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-10-01 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('PIZ', 'Pizza'), ('SAN', 'Sandwich'), ('BUR', 'Burger'), ('FRI', 'Fried'), ('SAL', 'Salad'), ('APP', 'Appetizer')], default='Pizza', max_length=3)),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('picture_food', models.ImageField(upload_to='static/food/images/all-food')),
            ],
        ),
    ]
