# Generated by Django 2.2.9 on 2020-04-21 17:46

from django.db import migrations
import management.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20200421_2046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=management.fields.OrderField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=management.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
