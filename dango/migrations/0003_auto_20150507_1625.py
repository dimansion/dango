# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dango', '0002_convert_ekstensi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_original', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('image_converted', models.ImageField(upload_to=b'images/')),
                ('persen', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='convert',
            name='ekstensi',
            field=models.CharField(max_length=5),
        ),
    ]
