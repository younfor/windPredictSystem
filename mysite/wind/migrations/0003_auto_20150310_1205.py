# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wind', '0002_auto_20150310_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powerdata',
            name='CFD_speed',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='powerdata',
            name='NWP_speed',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='powerdata',
            name='Observed_power',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='powerdata',
            name='Observed_speed',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='powerdata',
            name='Power_dev',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='powerdata',
            name='Predicted_power',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='powerdata',
            name='Predicted_speed',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='powerdata',
            name='Speed_dev',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='powerdata',
            name='time',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='powerdata',
            name='turbine',
            field=models.ForeignKey(null=True, to='wind.WindTurbine', unique=True),
        ),
    ]
