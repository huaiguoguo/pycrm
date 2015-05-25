# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('company', models.CharField(max_length=40)),
                ('mobile', models.IntegerField()),
                ('qq', models.IntegerField()),
                ('wangwang', models.CharField(max_length=10)),
                ('gender', models.IntegerField()),
                ('createdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('departmentname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('industryname', models.CharField(max_length=20)),
                ('createdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('levelname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Saler',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('salername', models.CharField(max_length=20)),
                ('mobile', models.IntegerField()),
                ('qq', models.IntegerField()),
                ('islead', models.IntegerField()),
                ('department', models.ForeignKey(related_name='departmentforeign', to='crm.Department')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='industry',
            field=models.ForeignKey(related_name='industryforeign', to='crm.Industry'),
        ),
        migrations.AddField(
            model_name='customer',
            name='saler',
            field=models.ForeignKey(related_name='salerforeign', to='crm.Saler'),
        ),
    ]
