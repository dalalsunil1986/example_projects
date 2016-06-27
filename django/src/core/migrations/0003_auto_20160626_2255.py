# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=140, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=128, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='user',
            name='website',
            field=models.CharField(max_length=128, verbose_name='Website'),
        ),
    ]
