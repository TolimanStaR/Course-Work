# Generated by Django 2.2.9 on 2020-04-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200413_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='contest_rang',
            field=models.CharField(choices=[('Новичек', 'Новичек'), ('Лиманадек', 'Лиманадек'), ('Черниговский батон', 'Черниговский батон'), ('Сыр косичка', 'Сыр косичка'), ('Масленок', 'Масленок'), ("Советский for'ик", "Советский for'ик"), ('Живой огурец', 'Живой огурец'), ('Мафиозник', 'Мафиозник'), ('Олимпиадник', 'Олимпиадник'), ('Sempai', 'Sempai'), ('Sensei', 'Sensei'), ('Галактический кодер', 'Галактический кодер')], default='Новичек', max_length=45),
        ),
    ]