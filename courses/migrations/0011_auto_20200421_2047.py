# Generated by Django 2.2.9 on 2020-04-21 17:47

from django.db import migrations
import management.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20200421_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='order',
            field=management.fields.OrderField(blank=True),
        ),
    ]
