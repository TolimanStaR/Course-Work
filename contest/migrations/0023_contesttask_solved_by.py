# Generated by Django 2.2.9 on 2020-04-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0022_remove_contesttest_judge_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='contesttask',
            name='solved_by',
            field=models.IntegerField(default=0),
        ),
    ]
