# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0003_auto_20150507_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convert',
            name='image_converted',
            field=models.ImageField(null=True, upload_to=b'images/', blank=True),
        ),
    ]
