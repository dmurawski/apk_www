from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
# Register your models here.

from .models import Osoba
from .models import Druzyna
class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko','miesiac_urodzenia','data_dodania','druzyna']
    list_filter = ('druzyna','data_dodania' )
# ten obiekt też trzeba zarejestrować w module admin
admin.site.register(Osoba, OsobaAdmin)

class DruzynaAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'kraj']
    list_filter = ('kraj',)

# ten obiekt też trzeba zarejestrować w module admin
admin.site.register(Druzyna, DruzynaAdmin)

TokenAdmin.raw_id_fields = ['user']