# Generated by Django 4.1.7 on 2023-02-15 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juke_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
