# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-07 22:41
from __future__ import unicode_literals

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200608_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=pyuploadcare.dj.models.ImageField(),
        ),
    ]
