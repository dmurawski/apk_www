from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class List(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now=True)
    author = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return  self.name + ' ' + self.author.username

    class Meta:
        ordering = ['created']
        verbose_name_plural = "Listy"

class LabelsToDoList(models.TextChoices):
    WORK = 'WK', _('Work')
    EVENT = 'EVE', _('Event')
    HOUSEWORK = 'HW', _('HouseWork')
    BILLS = 'BIL', _('Bills')
    PERSONAL = 'PER', _('Personal')
    GROUP = 'GR', _('Group')
    STUDIES = 'STU', _('Studies')
    HEALTH = 'HEA', _('Health')
    DEFAULT = 'DEF', _('General')

class TaskPriority(models.IntegerChoices):
    LEVEL1 = 1, _('Important and urgent')
    LEVEL2 = 2, _('Not urgent but important')
    LEVEL3 = 3, _('Urgent but not important')
    LEVEL4 = 4, _('Not urgent and not important')
    LEVEL5 = 5, _('Neither')

class Status(models.TextChoices):
    IDEAS = 'IDE', _('Ideas')
    TODO = 'TD', _('To do')
    DONE = 'DN', _('Done')
    NOTSTARTED = 'NS', _('Not started yet')

class Task(models.Model):
    author = models.ForeignKey('auth.User', null = True, on_delete = models.CASCADE, blank = True)
    title = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    complete_status = models.CharField(
        max_length=3,
        choices=Status.choices,
        default=Status.NOTSTARTED,
    )
    created = models.DateField(auto_now = True)
    deadline = models.DateField(blank = False, null = False)
    responsible = models.ForeignKey('auth.User', related_name='author', null=False, on_delete=models.CASCADE)
    label = models.CharField(
        max_length=3,
        choices=LabelsToDoList.choices,
        default=LabelsToDoList.DEFAULT,
    )
    priority = models.IntegerField(
        choices=TaskPriority.choices,
        default=TaskPriority.LEVEL5)
    list = models.ForeignKey(List, null=False, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return  self.responsible.username+' '+self.title

    class Meta:
        ordering = ['deadline','priority']
        verbose_name_plural = "Zadania"


