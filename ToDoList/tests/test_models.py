from django.test import TestCase
from ..models import Task, List, LabelsToDoList, TaskPriority, Status
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

def today():
    return datetime.date.today()
def tomorrow():
    return datetime.date.today() + datetime.timedelta(days=1)
class TaskModelTest(TestCase):
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
        Task.objects.create(author=User.objects.get(id=1),
                            title='Title',
                            description='Kowalski',
                            complete_status=" Status.NOTSTARTED",
                            created=today(),
                            deadline=tomorrow(),
                            responsible=User.objects.get(id=1),
                            label=LabelsToDoList.DEFAULT,
                            priority=TaskPriority.LEVEL5,
                            list=List.objects.get(id=1),
                            )
        Task.objects.create(author=User.objects.get(id=1),
                            title='Title2',
                            description='Kowalski',
                            complete_status=" Status.NOTSTARTED",
                            created=today(),
                            deadline=tomorrow(),
                            responsible=User.objects.get(id=1),
                            label=LabelsToDoList.DEFAULT,
                            priority=TaskPriority.LEVEL5,
                            list=List.objects.get(id=1),
                            )

    def test_title_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        task = Task.objects.get(id=1)
        max_length = task._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_complete_max_length(self):
        task = Task.objects.get(id=1)
        max_length = task._meta.get_field('complete_status').max_length
        self.assertEqual(max_length, 3)

    def test_task_id(self):
        task = Task.objects.get(id=1)
        id = task.id
        self.assertEqual(id, 1)
        task2 = Task.objects.get(id=2)
        id2 = task2.id
        self.assertEqual(id2, 2)


class ListModelTest(TestCase):
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
        List.objects.create(name='testdruzyna2',
                            created=today(),
                            author=User.objects.get(id=1),
                            )
    def test_name_label(self):
        list = List.objects.get(id=1)
        field_label = list._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        list = List.objects.get(id=1)
        max_length = list._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_druzyna_id(self):
        list = List.objects.get(id=1)
        id = list.id
        self.assertEqual(id, 1)
        list2 = List.objects.get(id=2)
        id2 = list2.id
        self.assertEqual(id2, 2)