# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wind', '0004_factory_scope'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factory',
            name='location',
        ),
        migrations.RemoveField(
            model_name='powerstation',
            name='location',
        ),
        migrations.RemoveField(
            model_name='windturbine',
            name='location',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.AlterField(
            model_name='factory',
            name='scope',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
