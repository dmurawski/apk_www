# Generated by Django 4.0.3 on 2022-11-28 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class3app', '0009_alter_osoba_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko'], 'permissions': [('change_person_owner', 'Pozwala przypisać inną osobę do obiektu Person.'), ('change_assign_to_team', 'Pozwala przypisać osobę do innej drużyny.')]},
        ),
    ]
