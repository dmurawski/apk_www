# from django.test import TestCase
#
# from ..models import Osoba, Months, Druzyna
# from django.contrib.auth.models import User
# from django.urls import reverse
# import datetime
#
# def today():
#     return datetime.date.today()
#
# class OsobaModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         password = 'mypassword'
#         User.objects.create_superuser('myuser',
#                                       'myemail@test.com',
#                                       password
#                                       )
#         Druzyna.objects.create(nazwa='testdruzyna',
#                                kraj='PL'
#                                )
#         Osoba.objects.create(imie='Jan',
#                              nazwisko='Kowalski',
#                              miesiac_urodzenia=Months.LUTY,
#                              data_dodania= today(),
#                              druzyna=Druzyna.objects.get(id=1),
#                              owner=User.objects.get(id=1)
#                              )
#         Osoba.objects.create(imie='Jan',
#                              nazwisko='Nowak',
#                              miesiac_urodzenia=Months.LUTY,
#                              data_dodania=today(),
#                              druzyna=Druzyna.objects.get(id=1),
#                              owner=User.objects.get(id=1)
#                              )
#
#     def test_first_name_label(self):
#         osoba = Osoba.objects.get(id=1)
#         field_label = osoba._meta.get_field('imie').verbose_name
#         self.assertEqual(field_label, 'imie')
#
#     def test_first_name_max_length(self):
#         osoba = Osoba.objects.get(id=1)
#         max_length = osoba._meta.get_field('imie').max_length
#         self.assertEqual(max_length, 60)
#
#     def test_surname_max_length(self):
#         osoba = Osoba.objects.get(id=1)
#         max_length = osoba._meta.get_field('nazwisko').max_length
#         self.assertEqual(max_length, 60)
#
#     def test_month_of_birth_max_length(self):
#         osoba = Osoba.objects.get(id=1)
#         max_length = osoba._meta.get_field('miesiac_urodzenia').max_length
#         self.assertEqual(max_length, 4)
#
#     def test_date_of_create_dateField_type(self):
#         osoba = Osoba.objects.get(id=1)
#         auto_now = osoba._meta.get_field('data_dodania').auto_now
#         self.assertEqual(auto_now, True)
#
#     def test_team_label(self):
#         druzyna = Osoba.objects.get(id=1)
#         field_label = druzyna._meta.get_field('druzyna').verbose_name
#         self.assertEqual(field_label, 'Drużyna')
#
#     def test_osoba_id(self):
#         osoba = Osoba.objects.get(id=1)
#         id = osoba.id
#         self.assertEqual(id, 1)
#         osoba2 = Osoba.objects.get(id=2)
#         id2 = osoba2.id
#         self.assertEqual(id2, 2)
#
#
# class DruzynaModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         Druzyna.objects.create(nazwa='testdruzyna',
#                                kraj='PL'
#                                )
#         Druzyna.objects.create(nazwa='Real Madryt C.F',
#                                kraj='PL'
#                                )
#     def test_name_label(self):
#         druzyna = Druzyna.objects.get(id=1)
#         field_label = druzyna._meta.get_field('nazwa').verbose_name
#         self.assertEqual(field_label, 'nazwa')
#
#     def test_name_max_length(self):
#         druzyna = Druzyna.objects.get(id=1)
#         max_length = druzyna._meta.get_field('nazwa').max_length
#         self.assertEqual(max_length, 40)
#
#     def test_kraj_max_length(self):
#         druzyna = Druzyna.objects.get(id=1)
#         max_length = druzyna._meta.get_field('kraj').max_length
#         self.assertEqual(max_length, 2)
#
#     def test_kraj_label(self):
#         druzyna = Druzyna.objects.get(id=1)
#         field_label = druzyna._meta.get_field('kraj').verbose_name
#         self.assertEqual(field_label, 'kraj')
#
#     def test_druzyna_id(self):
#         druzyna = Druzyna.objects.get(id=1)
#         id = druzyna.id
#         self.assertEqual(id, 1)
#         druzyna2 = Druzyna.objects.get(id=2)
#         id2 = druzyna2.id
#         self.assertEqual(id2, 2)