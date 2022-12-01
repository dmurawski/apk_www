from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Osoba, Druzyna, Months
from django.contrib.auth.models import User
import datetime

def today():
    return datetime.date.today()

class AccountTests(APITestCase):
    def login(self):
        return self.client.login(username='myuser', password='mypassword')
    def setUpTestData():
        password = 'mypassword'
        User.objects.create_superuser('myuser',
                                      'myemail@test.com',
                                      password
                                      )
        Druzyna.objects.create(nazwa='testdruzyna',
                               kraj='PL'
                               )
    def test_create_osoba(self):
        login = self.login()
        url = reverse('osoby_list')
        data = {'imie': 'testtest',
                'nazwisko': 'Kowalski',
                'miesiac_urodzenia':Months.LUTY,
                'data_dodania': today(),
                'druzyna' : Druzyna.objects.get(id=1).id ,
                'owner': User.objects.get(id=1).username
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Osoba.objects.count(), 1)
        self.assertEqual(Osoba.objects.get().imie, 'testtest')