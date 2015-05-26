# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0014_auto_20150513_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watermarktxt',
            name='posisi',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'kanan atas', b'kanan atas'), (b'kanan bawah', b'kanan bawah'), (b'kiri atas', b'kiri atas'), (b'kiri bawah', b'kiri bawah')]),
        ),
    ]
