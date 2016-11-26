# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 18:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0003_quote_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=settings.STATIC_ROOT+'/uploads/'),
        ),
    ]
