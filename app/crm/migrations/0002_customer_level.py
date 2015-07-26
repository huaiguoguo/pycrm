# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='level',
            field=models.ForeignKey(related_name='levelforeign', default=1, to='crm.Level'),
            preserve_default=False,
        ),
    ]
