# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wind', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('province', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PowerData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.CharField(max_length=30)),
                ('NWP_speed', models.CharField(max_length=30)),
                ('CFD_speed', models.CharField(max_length=30)),
                ('Observed_speed', models.CharField(max_length=30)),
                ('Observed_power', models.CharField(max_length=30)),
                ('Predicted_speed', models.CharField(max_length=30)),
                ('Speed_dev', models.CharField(max_length=30)),
                ('Predicted_power', models.CharField(max_length=30)),
                ('Power_dev', models.CharField(max_length=30)),
                ('turbine', models.ForeignKey(to='wind.WindTurbine', unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='factory',
            name='begintime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factory',
            name='endtime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factory',
            name='location',
            field=models.ForeignKey(null=True, to='wind.Location', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='powerstation',
            name='begintime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='powerstation',
            name='endtime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='powerstation',
            name='location',
            field=models.ForeignKey(null=True, to='wind.Location', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='windturbine',
            name='begintime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='windturbine',
            name='endtime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='windturbine',
            name='location',
            field=models.ForeignKey(null=True, to='wind.Location', unique=True),
            preserve_default=True,
        ),
    ]
