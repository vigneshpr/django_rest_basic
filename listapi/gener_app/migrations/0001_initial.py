# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-11 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gener_api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(blank=True, max_length=20, unique=True)),
                ('author', models.CharField(blank=True, default='', max_length=10)),
                ('publication', models.TextField(max_length=30)),
                ('dept', models.CharField(max_length=30)),
                ('published_year', models.IntegerField(default=0)),
            ],
        ),
    ]
