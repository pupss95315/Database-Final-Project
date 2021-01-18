# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20201227_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='CID',
            field=models.CharField(primary_key=True, max_length=8, serialize=False),
        ),
    ]
