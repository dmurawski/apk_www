# Generated by Django 4.1.2 on 2022-10-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='test',
            field=models.IntegerField(default=0),
        ),
    ]
