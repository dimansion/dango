# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0016_auto_20150513_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='watermarktxt',
            name='url_image',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
    ]
