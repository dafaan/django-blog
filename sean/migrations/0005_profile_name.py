# Generated by Django 3.2.11 on 2022-01-21 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sean', '0004_auto_20220121_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='unknown', max_length=200),
        ),
    ]
