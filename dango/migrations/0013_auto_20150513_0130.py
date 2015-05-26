# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0012_auto_20150512_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convert',
            name='ekstensi',
            field=models.CharField(max_length=5, choices=[(b'png', b'png'), (b'jpg', b'jpg')]),
        ),
    ]
