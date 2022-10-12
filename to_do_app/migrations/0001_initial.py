# Generated by Django 4.1.2 on 2022-10-12 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=200)),
                ('dateCreate', models.DateTimeField(verbose_name='Stworzono')),
                ('dateToFinish', models.DateTimeField(verbose_name='Deadline')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(max_length=200)),
                ('taskDescription', models.CharField(max_length=200)),
                ('order', models.IntegerField(default=0)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='to_do_app.list')),
            ],
        ),
    ]
