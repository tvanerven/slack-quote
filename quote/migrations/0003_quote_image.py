# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0002_auto_20160707_0553'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name=models.FileField(upload_to='uploads/')),
        ),
    ]
