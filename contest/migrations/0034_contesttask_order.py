# Generated by Django 2.2.9 on 2020-04-30 08:54

from django.db import migrations
import management.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0033_contest_participants_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='contesttask',
            name='order',
            field=management.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]