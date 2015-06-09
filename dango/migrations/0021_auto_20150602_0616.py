# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0020_auto_20150602_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convert',
            name='ekstensi',
            field=models.CharField(max_length=9, choices=[(b'png', b'png'), (b'jpg', b'jpg'), (b'tiff', b'tiff'), (b'jpeg-2000', b'jpeg-2000'), (b'pdf', b'pdf')]),
        ),
    ]
