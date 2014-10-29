# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrImage', '0002_auto_20141029_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mrimage',
            name='description',
            field=models.TextField(max_length=400, blank=True),
            preserve_default=True,
        ),
    ]
