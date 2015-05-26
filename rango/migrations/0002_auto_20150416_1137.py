# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='views',
            new_name='view',
        ),
        migrations.AddField(
            model_name='page',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]