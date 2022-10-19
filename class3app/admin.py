from django.contrib import admin

# Register your models here.

from .models import Osoba

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko','miesiac_urodzenia','data_dodania']

# ten obiekt też trzeba zarejestrować w module admin
admin.site.register(Osoba, OsobaAdmin)