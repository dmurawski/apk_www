from django.db import models
from django.db.models import ForeignKey
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
# Create your models here.
class Druzyna(models.Model):
    nazwa = models.CharField(max_length=40)
    kraj = models.CharField(max_length=2, blank=True, null=True)
    def __str__(self):
        return self.nazwa+" "+"("+self.kraj+")"

class Months(models.TextChoices):
    STYCZEN = 'I', _('Styczeń')
    LUTY = 'II', _('Luty')
    MARZEC = 'III', _('Marzec')
    KWIECIEN = 'IV', _('Kwiecień')
    MAJ = 'V', _('Maj')
    CZERWIEC = 'VI', _('Czerwiec')
    LIPIEC = 'VII', _('Lipiec')
    SIERPIEN = 'VIII', _('Sierpień')
    WRZESIEN = 'IX', _('Wrzesień')
    PAZDZIERNIK = 'X', _('Październik')
    LISTOPAD = 'XI', _('Listopad')
    GRUDZIEN = 'XII', _('Grudzień')
class Osoba(models.Model):
    imie = models.CharField(max_length=60 ,blank=False)
    nazwisko = models.CharField(max_length=60, blank=False)
    miesiac_urodzenia = models.CharField(max_length=4,choices=Months.choices, default=Months.LUTY)
    data_dodania = models.DateField(auto_now=True)
    druzyna = models.ForeignKey(Druzyna, on_delete=models.SET_NULL,null=True,verbose_name="Drużyna")
    owner: ForeignKey = models.ForeignKey('auth.User', null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.imie+" "+self.nazwisko


    class Meta:
        ordering = ["nazwisko"]
        permissions = [
            ("can_view_other_osoba", "Pozwala przypisać inną osobę do obiektu Person."),
        ]