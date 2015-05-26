# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0013_auto_20150513_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rotate',
            name='direction',
            field=models.CharField(blank=True, max_length=7, null=True, choices=[(b'kanan', b'kanan'), (b'kiri', b'kiri')]),
        ),
    ]
