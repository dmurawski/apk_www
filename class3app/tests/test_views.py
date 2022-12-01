from django.test import TestCase
from django.urls import reverse

from ..models import Osoba, Months, Druzyna
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

def today():
    return datetime.date.today()

class OsobaListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        password = 'mypassword'
        User.objects.create_superuser('myuser',
                                      'myemail@test.com',
                                      password
                                      )
        Druzyna.objects.create(nazwa='testdruzyna',
                               kraj='PL'
                               )
        number_of_authors = 13
        for osoba_id in range(number_of_authors):
            Osoba.objects.create(imie=f'Jan{osoba_id}',
                                 nazwisko=f'Kowalski{osoba_id}',
                                 miesiac_urodzenia=Months.LUTY,
                                 data_dodania= today(),
                                 druzyna=Druzyna.objects.get(id=1),
                                 owner=User.objects.get(id=1)
                                 )

    def login(self):
        return self.client.login(username='myuser', password='mypassword')
    def test_view_url_exists_at_desired_location(self):
        login= self.login()
        self.assertTrue(login)
        response = self.client.get('/app/osoby/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.login()
        response = self.client.get(reverse('osoby_list'))
        self.assertEqual(response.status_code, 200)

    # def test_view_uses_correct_template(self):
    #     response = self.client.get(reverse('osoby'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'catalog/author_list.html')

    # def test_pagination_is_ten(self):
    #     response = self.client.get(reverse('authors'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertEqual(len(response.context['author_list']), 10)
    #
    # def test_lists_all_authors(self):
    #     # Get second page and confirm it has (exactly) remaining 3 items
    #     response = self.client.get(reverse('authors')+'?page=2')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertEqual(len(response.context['author_list']), 3)