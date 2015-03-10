# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wind', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('province', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75)),
                ('bank_account', models.CharField(max_length=30)),
                ('begintime', models.DateTimeField(null=True)),
                ('endtime', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PowerStation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('province', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75)),
                ('bank_account', models.CharField(max_length=30)),
                ('begintime', models.DateTimeField(null=True)),
                ('endtime', models.DateTimeField(null=True)),
                ('factory', models.ForeignKey(to='wind.Factory')),
                ('location', models.ForeignKey(null=True, to='wind.Location', unique=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WindTurbine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('longitude', models.CharField(max_length=12)),
                ('latitude', models.CharField(max_length=12)),
                ('contact', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75)),
                ('begintime', models.DateTimeField(null=True)),
                ('endtime', models.DateTimeField(null=True)),
                ('location', models.ForeignKey(null=True, to='wind.Location', unique=True)),
                ('powerstation', models.ForeignKey(to='wind.PowerStation')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='factories',
            name='user',
        ),
        migrations.RemoveField(
            model_name='powerstations',
            name='factory',
        ),
        migrations.DeleteModel(
            name='Factories',
        ),
        migrations.RemoveField(
            model_name='powerstations',
            name='user',
        ),
        migrations.RemoveField(
            model_name='windturbines',
            name='powerstation',
        ),
        migrations.DeleteModel(
            name='PowerStations',
        ),
        migrations.RemoveField(
            model_name='windturbines',
            name='user',
        ),
        migrations.DeleteModel(
            name='WindTurbines',
        ),
        migrations.AddField(
            model_name='powerdata',
            name='turbine',
            field=models.ForeignKey(to='wind.WindTurbine', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factory',
            name='location',
            field=models.ForeignKey(null=True, to='wind.Location', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factory',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='father',
            field=models.ForeignKey(default=None, blank=True, to='wind.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='level',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='telephone',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
