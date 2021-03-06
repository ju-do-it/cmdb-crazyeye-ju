# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-21 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0006_asset_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='os_distribution',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='发型版本'),
        ),
        migrations.AddField(
            model_name='server',
            name='os_release',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='操作系统版本'),
        ),
        migrations.AddField(
            model_name='server',
            name='os_type',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='操作系统类型'),
        ),
        migrations.AddField(
            model_name='server',
            name='raid_type',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='raid类型'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='cabinet_num',
            field=models.CharField(max_length=30, null=True, verbose_name='机柜号'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='cabinet_order',
            field=models.CharField(max_length=30, null=True, verbose_name='机柜中序号'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='latest_date',
            field=models.DateField(null=True, verbose_name='最后更新时间'),
        ),
    ]
