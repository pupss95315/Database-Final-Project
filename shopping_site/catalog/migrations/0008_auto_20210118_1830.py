# Generated by Django 3.1.5 on 2021-01-18 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20210118_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='NO',
        ),
        migrations.AlterField(
            model_name='customer',
            name='CID',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
