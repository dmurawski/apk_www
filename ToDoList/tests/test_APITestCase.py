from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Task, List, LabelsToDoList, TaskPriority, Status
from django.contrib.auth.models import User
from datetime import datetime
import datetime

def today():
    return datetime.date.today()
def tomorrow():
    return datetime.date.today() + datetime.timedelta(days=1)

class TaskTest(APITestCase):
    def login(self):
        return self.client.login(username='myuser', password='mypassword')
    def setUpTestData():
        password = 'mypassword'
        User.objects.create_superuser('myuser',
                                      'myemail@test.com',
                                      password
                                      )
        List.objects.create(name='testLista',
                            created=today()
                            )
    def test_create_task(self):
        print(today())
        print(tomorrow())
        login = self.login()
        url = reverse('task_post')
        data = {'author': 'myuser',
                'title': 'Title',
                'description': 'Kowalski',
                'complete_status':" Status.NOTSTARTED",
                'created': today(),
                'deadline': tomorrow(),
                'responsible': User.objects.get(id=1).username,
                'label': LabelsToDoList.DEFAULT,
                'priority' : TaskPriority.LEVEL5 ,
                }
        print(data)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Title')