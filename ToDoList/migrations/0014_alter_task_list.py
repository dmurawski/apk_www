# Generated by Django 4.1.3 on 2022-12-07 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0013_alter_list_options_list_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ToDoList.list'),
        ),
    ]
