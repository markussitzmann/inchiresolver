# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resolver', '0002_auto_20170313_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='uriendpoint',
            name='description',
            field=models.TextField(blank=True, max_length=32768, null=True),
        ),
    ]