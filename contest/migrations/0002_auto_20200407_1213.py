# Generated by Django 2.2.9 on 2020-04-07 09:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestparticipant',
            name='stats',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BooleanField(default=None), blank=True, size=16),
        ),
    ]
