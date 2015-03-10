# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wind', '0004_auto_20150109_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='father',
            field=models.ForeignKey(default=None, blank=True, to='wind.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
