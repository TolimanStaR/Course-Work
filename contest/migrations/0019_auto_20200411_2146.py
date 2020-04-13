# Generated by Django 2.2.9 on 2020-04-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0018_auto_20200411_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestsolutioncase',
            name='task_code',
            field=models.TextField(default='#include <cheats>\nusing namespace hack;\nint main () {\nchar input[];\ncin >> input;\ncout << hack::get_solution(input);\nreturn 0;\n}'),
        ),
        migrations.AlterField(
            model_name='contesttest',
            name='answer',
            field=models.TextField(default=None),
        ),
    ]