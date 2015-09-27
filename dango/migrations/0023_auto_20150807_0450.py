# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0022_auto_20150807_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convert',
            name='ekstensi',
            field=models.CharField(max_length=9, choices=[(b'png', b'png'), (b'bnp', b'bnp'), (b'tiff', b'tiff'), (b'pdf', b'pdf')]),
        ),
    ]
