# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-11 11:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gener_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gener_api',
            options={'ordering': ('bookname',)},
        ),
    ]