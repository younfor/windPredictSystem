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
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
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
                ('factory', models.ForeignKey(to='wind.Factory')),
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
    ]
