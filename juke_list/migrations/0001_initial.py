# Generated by Django 4.1.7 on 2023-02-15 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=500)),
                ('thumbnail', models.CharField(max_length=100)),
            ],
        ),
    ]