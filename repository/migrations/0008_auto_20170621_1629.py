# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-21 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0007_auto_20170621_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufactory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufactory', models.CharField(max_length=64, unique=True, verbose_name='厂商名称')),
                ('support_num', models.CharField(blank=True, max_length=30, verbose_name='支持电话')),
                ('memo', models.CharField(blank=True, max_length=128, verbose_name='备注')),
            ],
            options={
                'verbose_name_plural': '厂商',
                'verbose_name': '厂商',
            },
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='SN号')),
                ('model', models.CharField(max_length=128, verbose_name='内存型号')),
                ('slot', models.CharField(max_length=64, verbose_name='插槽')),
                ('capacity', models.IntegerField(verbose_name='内存大小(MB)')),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='备注')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Asset')),
            ],
            options={
                'verbose_name_plural': 'RAM',
                'verbose_name': 'RAM',
            },
        ),
        migrations.AddField(
            model_name='disk',
            name='asset',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='repository.Asset'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='bonding',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='macaddress',
            field=models.CharField(default=1, max_length=64, unique=True, verbose_name='MAC'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='memo',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='网卡名'),
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='netmask',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='update_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nic',
            name='asset',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='repository.Asset'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='networkdevice',
            name='management_ip',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='公网IP'),
        ),
        migrations.AlterUniqueTogether(
            name='ram',
            unique_together=set([('asset', 'slot')]),
        ),
    ]
