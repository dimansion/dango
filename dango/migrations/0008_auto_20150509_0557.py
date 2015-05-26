# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0007_auto_20150509_0554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meme',
            name='direction',
        ),
        migrations.AddField(
            model_name='meme',
            name='teksatas',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meme',
            name='teksbawah',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
