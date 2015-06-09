# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0018_watermarkimg_url_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='url_image',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
    ]
