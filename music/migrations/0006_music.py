# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-04 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20190304_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('artist', models.CharField(max_length=120)),
                ('song_tittle', models.CharField(max_length=120)),
            ],
        ),
    ]