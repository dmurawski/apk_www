from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import Osoba, Druzyna, Months
import datetime


def validate_imie(value):
    if not value.isalpha():
        raise serializers.ValidationError(
            "Imie powinno zawierać tylko litery",
        )
    return value


def validate_data_dodania(value):
    if value > datetime.date.today():
        raise serializers.ValidationError(
            "Data nie może być z przyszłości",
        )
    return value
class OsobaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True, validators=[validate_imie])
    nazwisko = serializers.CharField(required=True)
    miesiac_urodzenia = serializers.ChoiceField(choices=Months, default=Months.LUTY)
    data_dodania = serializers.DateField(initial=datetime.date.today,validators=[validate_data_dodania])
    druzyna = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all(),allow_null=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    # przesłonięcie metody create() z klasy serializers.Serializer

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    # przesłonięcie metody update() z klasy serializers.Serializer
    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.data_dodania = validated_data.get('data_dodania', instance.data_dodania)
        instance.miesiac_urodzenia = validated_data.get('miesiac_urodzenia', instance.miesiac_urodzenia)
        instance.druzyna = validated_data.get('druzyna', instance.druzyna)
        instance.save()
        return instance


class DruzynaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(required=True)
    kraj = serializers.CharField(required=True)

    def create(self, validated_data):
        return Druzyna.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.kraj = validated_data.get('kraj', instance.kraj)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    owners = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = User
        fields = ['__all__']