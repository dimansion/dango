# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0006_auto_20150507_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_original', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('image_converted', models.ImageField(upload_to=b'images/')),
                ('direction', models.CharField(max_length=7, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='resize',
            name='image_converted',
            field=models.ImageField(null=True, upload_to=b'images/', blank=True),
        ),
    ]
