# Generated by Django 2.2.9 on 2020-04-11 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0017_contestsolutioncase_task_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestparticipant',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='member', to='account.UserProfile'),
        ),
    ]
