# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-19 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severity', models.CharField(default='Info', max_length=10)),
                ('message', models.CharField(default='No Message', max_length=1024)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
