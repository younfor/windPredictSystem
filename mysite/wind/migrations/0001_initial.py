# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telephone', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('level', models.CharField(max_length=10, null=True)),
                ('father', models.ForeignKey(default=None, blank=True, to='wind.UserProfile', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
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
    ]
