# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-13 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridges', '0002_auto_20160113_0825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fridges',
            old_name='fridgename',
            new_name='fridgegroup',
        ),
        migrations.RenameField(
            model_name='fridges',
            old_name='body',
            new_name='situated',
        ),
        migrations.RemoveField(
            model_name='fridges',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='fridges',
            name='temperature',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
