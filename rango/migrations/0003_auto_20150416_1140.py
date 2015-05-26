# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20150416_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='likes',
            new_name='views',
        ),
        migrations.RemoveField(
            model_name='page',
            name='view',
        ),
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='view',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
