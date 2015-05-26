# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0005_rotate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rotate',
            name='direction',
            field=models.CharField(max_length=7, null=True, blank=True),
        ),
    ]
