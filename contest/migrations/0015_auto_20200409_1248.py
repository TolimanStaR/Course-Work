# Generated by Django 2.2.9 on 2020-04-09 09:48

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0014_auto_20200409_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestparticipant',
            name='stats',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(default=0), blank=True, size=16),
        ),
    ]
