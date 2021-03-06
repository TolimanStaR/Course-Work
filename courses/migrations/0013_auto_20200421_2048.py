# Generated by Django 2.2.9 on 2020-04-21 17:48

from django.db import migrations
import management.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20200421_2048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=management.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
