# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-25 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caaring', '0005_auto_20180326_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cab',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]