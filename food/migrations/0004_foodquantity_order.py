# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-11-22 15:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0003_auto_20191004_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('PEN', 'Pending'), ('CAN', 'Is Cancelled'), ('VER', 'Verified'), ('DEL', 'Is Delivered')], max_length=3)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('shipping_cost', models.PositiveIntegerField(default=0)),
                ('payment_method', models.CharField(blank=True, choices=[('CR', 'Credit'), ('CA', 'Cash')], max_length=2)),
                ('name_delivery', models.CharField(blank=True, max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('foods', models.ManyToManyField(to='food.FoodQuantity')),
            ],
        ),
    ]
