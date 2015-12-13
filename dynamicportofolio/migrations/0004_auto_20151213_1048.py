# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicportofolio', '0003_post_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Portofolio',
        ),
    ]
