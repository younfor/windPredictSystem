# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wind', '0002_auto_20150107_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='father',
            field=models.ForeignKey(default=None, to='wind.UserProfile'),
            preserve_default=True,
        ),
    ]
