# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrCheck', '0002_auto_20141029_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='scanDate',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
