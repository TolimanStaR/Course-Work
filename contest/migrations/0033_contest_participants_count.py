# Generated by Django 2.2.9 on 2020-04-28 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0032_contestpastparticipant_contest_rang_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='participants_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
