# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('BrandCode', models.IntegerField()),
                ('BrandName', models.CharField(max_length=20)),
                ('BrandPinYin', models.CharField(max_length=20)),
                ('BrandJianPin', models.CharField(max_length=20)),
                ('BrandLogo', models.CharField(max_length=20)),
                ('BrandSouPin', models.CharField(max_length=20)),
                ('BrandUrl', models.CharField(max_length=20)),
            ],
        ),
    ]
