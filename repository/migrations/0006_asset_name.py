# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-21 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_newassetapprovalzone'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='name',
            field=models.CharField(default=1, max_length=64, unique=True),
            preserve_default=False,
        ),
    ]
