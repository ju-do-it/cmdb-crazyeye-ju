# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-22 11:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0009_auto_20170621_1821'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='server',
            options={'verbose_name': '服务器', 'verbose_name_plural': '服务器表'},
        ),
        migrations.RemoveField(
            model_name='server',
            name='manufacturer',
        ),
    ]
