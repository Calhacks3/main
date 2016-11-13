# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.CharField(max_length=256)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_id', models.CharField(max_length=30)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=10)),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
    ]