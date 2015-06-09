# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0019_meme_url_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convert',
            name='ekstensi',
            field=models.CharField(max_length=10, choices=[(b'png', b'png'), (b'jpg', b'jpg'), (b'tiff', b'tiff'), (b'jpeg-2000', b'jpeg-2000'), (b'pdf', b'pdf')]),
        ),
    ]
