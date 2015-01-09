# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wind', '0003_userprofile_father'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='father',
            field=models.ForeignKey(default=None, blank=True, to='wind.UserProfile'),
            preserve_default=True,
        ),
    ]
