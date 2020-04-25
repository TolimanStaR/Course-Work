# Generated by Django 2.2.9 on 2020-04-24 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_userprofile_is_staff'),
        ('courses', '0013_auto_20200421_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='difficulty',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('b1', 'B1'), ('b2', 'B2'), ('c', 'C'), ('c1', 'C1'), ('c2', 'C2'), ('d', 'D'), ('d1', 'D1'), ('d2', 'D2'), ('e', 'E'), ('e1', 'E1'), ('e2', 'E2'), ('f', 'F'), ('f1', 'F1'), ('f2', 'F2'), ('g', 'G'), ('h', 'H'), ('i', 'I'), ('j', 'J'), ('k', 'K'), ('l', 'L'), ('', '')], default='a', max_length=3),
        ),
        migrations.CreateModel(
            name='TaskTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('answer', models.TextField(blank=True, default=None)),
                ('item_title', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasktest_related', to='account.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
