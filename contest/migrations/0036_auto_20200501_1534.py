# Generated by Django 2.2.9 on 2020-05-01 12:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0035_contesttask_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contesttest',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='contesttest',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]