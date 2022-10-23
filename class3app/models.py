from django.db import models

# Create your models here.
class Druzyna(models.Model):
    nazwa = models.CharField(max_length=40)
    kraj = models.CharField(max_length=2, blank=True, null=True)
    def __str__(self):
        return self.nazwa+" "+self.kraj


class Osoba(models.Model):
    imie = models.CharField(max_length=60 ,blank=False)
    nazwisko = models.CharField(max_length=60, blank=False)
    MONTHS = (
        ('I','styczeń'),
        ('II','luty'),
        ('III','marzec'),
        ('IV','kwiecień'),
        ('V','maj'),
        ('VI','czerwiec'),
        ('VII','lipiec'),
        ('VIII','sierpień'),
        ('XI','wrzesień'),
        ('X','październik'),
        ('XI','listopad'),
        ('XII','grudzień'),
    )
    miesiac_urodzenia = models.CharField(max_length=4, choices=MONTHS, default=MONTHS[0])
    data_dodania = models.DateField(auto_now=True)
    druzyna = models.ForeignKey(Druzyna, on_delete=models.SET_NULL,null=True,verbose_name="Drużyna")

    def __str__(self):
        return self.imie+" "+self.nazwisko

    class Meta:
        ordering = ["nazwisko"]

