# Generated by Django 2.2.9 on 2020-04-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0025_contestpastparticipant'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestparticipant',
            name='username',
            field=models.CharField(default='<django.db.models.fields.related.OneToOneField>', max_length=50),
        ),
    ]
