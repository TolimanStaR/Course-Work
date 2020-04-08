# Generated by Django 2.2.9 on 2020-04-08 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0010_auto_20200409_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contesttask',
            name='difficulty',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('b1', 'B1'), ('b2', 'B2'), ('c', 'C'), ('c1', 'C1'), ('c2', 'C2'), ('d', 'D'), ('d1', 'D1'), ('d2', 'D2'), ('e', 'E'), ('e1', 'E1'), ('e2', 'E2'), ('f', 'F'), ('f1', 'F1'), ('f2', 'F2'), ('g', 'G'), ('h', 'H'), ('i', 'I'), ('j', 'J'), ('k', 'K'), ('l', 'L')], default='a', max_length=3),
        ),
    ]