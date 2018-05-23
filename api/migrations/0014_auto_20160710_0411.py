# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-07-10 04:11
from __future__ import unicode_literals

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20160710_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horchata',
            name='location',
            field=location_field.models.plain.PlainLocationField(default={'x': 1.0, 'y': 1.0}, max_length=63),
        ),
    ]