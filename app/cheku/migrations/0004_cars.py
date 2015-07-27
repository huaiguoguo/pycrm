# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cheku', '0003_auto_20150727_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('CarsCode', models.IntegerField()),
                ('CarsName', models.CharField(max_length=20)),
                ('BrandId', models.ForeignKey(to='cheku.Brands', related_name='carsofbrandsforeign')),
            ],
        ),
    ]
