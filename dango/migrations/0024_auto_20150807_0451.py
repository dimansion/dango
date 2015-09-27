# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0023_auto_20150807_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convert',
            name='ekstensi',
            field=models.CharField(max_length=9, choices=[(b'png', b'png'), (b'jpg', b'jpg'), (b'tiff', b'tiff'), (b'pdf', b'pdf')]),
        ),
    ]
