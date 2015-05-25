# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_customer_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='level',
        ),
    ]
