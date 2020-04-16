# Generated by Django 2.2.9 on 2020-04-15 15:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0029_auto_20200415_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contestpastparticipant',
            name='place',
        ),
        migrations.AlterField(
            model_name='contestpastparticipant',
            name='stats',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), blank=True, size=16),
        ),
    ]