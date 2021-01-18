# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('CID', models.AutoField(primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=8)),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=1, choices=[('F', 'Female'), ('M', 'Male')])),
                ('BDate', models.DateField()),
                ('City', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('SID', models.AutoField(primary_key=True, serialize=False)),
                ('SName', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AlterUniqueTogether(
            name='supplier',
            unique_together=set([('SID', 'SName')]),
        ),
    ]
