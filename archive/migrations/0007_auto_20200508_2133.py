# Generated by Django 3.0.6 on 2020-05-08 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0006_auto_20200507_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivesolutioncase',
            name='verdict',
            field=models.CharField(default='Ожидается проверка', max_length=150),
        ),
    ]
