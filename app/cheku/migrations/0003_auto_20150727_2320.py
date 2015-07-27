# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cheku', '0002_auto_20150727_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='BrandJianPin',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='brands',
            name='BrandLogo',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='brands',
            name='BrandName',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='brands',
            name='BrandPinYin',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='brands',
            name='BrandSouPin',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='brands',
            name='BrandUrl',
            field=models.CharField(max_length=255),
        ),
    ]
