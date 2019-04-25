# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-20 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('douban', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('price', models.CharField(max_length=10)),
                ('imgurl', models.CharField(max_length=128)),
                ('url', models.CharField(max_length=128)),
                ('info', models.CharField(max_length=4096)),
            ],
        ),
    ]