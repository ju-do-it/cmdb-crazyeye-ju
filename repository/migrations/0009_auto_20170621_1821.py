# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-21 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0008_auto_20170621_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=128, unique=True, verbose_name='合同号')),
                ('name', models.CharField(max_length=64, verbose_name='合同名称')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('price', models.IntegerField(verbose_name='合同金额')),
                ('detail', models.TextField(blank=True, null=True, verbose_name='合同详细')),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('license_num', models.IntegerField(blank=True, verbose_name='license数量')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '合同',
                'verbose_name': '合同',
            },
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_model', models.CharField(blank=True, max_length=128, verbose_name='CPU型号')),
                ('cpu_count', models.SmallIntegerField(verbose_name='物理cpu个数')),
                ('cpu_core_count', models.SmallIntegerField(verbose_name='cpu核数')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'CPU部件',
                'verbose_name': 'CPU部件',
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='expire_date',
            field=models.DateField(blank=True, null=True, verbose_name='过保修期'),
        ),
        migrations.AddField(
            model_name='asset',
            name='manufactory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.Manufactory', verbose_name='制造商'),
        ),
        migrations.AddField(
            model_name='asset',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='价格'),
        ),
        migrations.AddField(
            model_name='asset',
            name='trade_date',
            field=models.DateField(blank=True, null=True, verbose_name='购买时间'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='asset',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='repository.Asset'),
        ),
        migrations.AddField(
            model_name='asset',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.Contract', verbose_name='合同'),
        ),
    ]