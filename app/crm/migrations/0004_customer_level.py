# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_remove_customer_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='level',
            field=models.ForeignKey(related_name='levelforeign', to='crm.Level', default=True),
        ),
    ]
