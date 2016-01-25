# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0002_auto_20151215_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='porto',
            name='link',
            field=models.URLField(null=True, blank=True),
        ),
    ]
