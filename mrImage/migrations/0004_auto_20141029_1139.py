# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrImage', '0003_auto_20141029_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mrimage',
            name='image_file',
            field=models.ImageField(upload_to=b'static_files/uploaded/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
