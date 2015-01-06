# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wind', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='name',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='phone',
        ),
        migrations.AddField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2015, 1, 6, 7, 44, 18, 306, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='email',
            field=models.EmailField(default=datetime.datetime(2015, 1, 6, 7, 44, 51, 662451, tzinfo=utc), unique=True, max_length=255, verbose_name=b'email address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_admin',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
