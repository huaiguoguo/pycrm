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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=40)),
                ('mobile', models.IntegerField(default='NULL')),
                ('qq', models.IntegerField(default='NULL')),
                ('wangwang', models.CharField(max_length=10)),
                ('gender', models.IntegerField(default='NULL')),
                ('createdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departmentname', models.CharField(default='NULL', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Saler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('salername', models.CharField(default='NULL', max_length=20)),
                ('mobile', models.IntegerField(default='NULL')),
                ('qq', models.IntegerField(default='NULL')),
                ('islead', models.IntegerField(default='NULL')),
                ('department', models.ForeignKey(to='crm.Department')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='saler',
            field=models.ForeignKey(to='crm.Saler'),
        ),
    ]
