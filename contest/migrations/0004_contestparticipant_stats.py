# Generated by Django 2.2.9 on 2020-04-06 15:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0003_auto_20200406_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestparticipant',
            name='stats',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BooleanField(default=None), default=[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], size=16),
        ),
    ]
