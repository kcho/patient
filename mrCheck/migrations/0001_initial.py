# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hospitalID', models.CharField(max_length=8)),
                ('initial', models.CharField(max_length=5)),
                ('group', models.CharField(max_length=5)),
                ('folderName', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('t1Number', models.IntegerField()),
                ('dtiNumber', models.IntegerField()),
                ('restNumber', models.IntegerField()),
                ('dkiNumber', models.IntegerField()),
                ('backupLocation', models.CharField(max_length=30)),
                ('scanDate', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
