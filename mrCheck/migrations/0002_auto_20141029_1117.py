# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrCheck', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='backupLocation',
            field=models.CharField(max_length=60),
            preserve_default=True,
        ),
    ]
