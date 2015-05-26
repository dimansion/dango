# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0011_watermarkimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='watermarkimg',
            name='image_logo',
            field=models.ImageField(null=True, upload_to=b'images/', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='watermarkimg',
            name='posisi',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
