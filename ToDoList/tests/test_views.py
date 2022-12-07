from django.test import TestCase
from django.urls import reverse
from ..models import Task, List, LabelsToDoList, TaskPriority, Status
from django.contrib.auth.models import User
from datetime import datetime
import datetime

def today():
    return datetime.date.today()
def tomorrow():
    return datetime.date.today() + datetime.timedelta(days=1)
class TaskListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        password = 'mypassword'
        User.objects.create_superuser('myuser',
                                      'myemail@test.com',
                                      password
                                      )
        List.objects.create(name='testdruzyna',
                            created=today(),
                            author=User.objects.get(id=1),
                               )
        Task.objects.create(author= User.objects.get(id=1),
                            title= 'Title',
                            description= 'Kowalski',
                            complete_status=" Status.NOTSTARTED",
                            created= today(),
                            deadline= tomorrow(),
                            responsible= User.objects.get(id=1),
                            label= LabelsToDoList.DEFAULT,
                            priority = TaskPriority.LEVEL5,
                            list = List.objects.get(id=1),
                             )
    def login(self):
        return self.client.login(username='myuser', password='mypassword')
    def test_view_url_exists_at_desired_location(self):
        login= self.login()
        self.assertTrue(login)
        response = self.client.get('/todolist/task/')
        self.assertEqual(response.status_code, 200)