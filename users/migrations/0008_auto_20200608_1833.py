# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-08 15:33
from __future__ import unicode_literals

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200608_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=pyuploadcare.dj.models.ImageField(),
        ),
    ]
