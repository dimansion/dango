# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='convert',
            name='ekstensi',
            field=models.CharField(default='', max_length=5, choices=[(b'.png', b'.png'), (b'.jpg', b'.jpg')]),
            preserve_default=False,
        ),
    ]
