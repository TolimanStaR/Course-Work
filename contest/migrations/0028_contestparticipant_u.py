# Generated by Django 2.2.9 on 2020-04-15 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0027_auto_20200415_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestparticipant',
            name='u',
            field=models.CharField(default=models.OneToOneField(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='member', to='account.UserProfile'), max_length=50),
        ),
    ]
