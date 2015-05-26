# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0010_auto_20150509_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatermarkImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_original', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('image_converted', models.ImageField(upload_to=b'images/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
