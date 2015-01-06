# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wind', '0003_auto_20150106_0809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('province', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PowerStations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('longitude', models.CharField(max_length=12)),
                ('latitude', models.CharField(max_length=12)),
                ('factory', models.ForeignKey(to='wind.Factories')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
