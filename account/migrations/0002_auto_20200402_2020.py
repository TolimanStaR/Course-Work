# Generated by Django 2.2.9 on 2020-04-02 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='about',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contest_rang',
            field=models.CharField(default='Начинающий', max_length=45),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contest_rang_color',
            field=models.PositiveIntegerField(default=11184810),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contest_rating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d/'),
        ),
    ]