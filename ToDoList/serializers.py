from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import Task, List, Status, LabelsToDoList, TaskPriority
import datetime

def validate_deadline(value):
    if value == None:
        raise serializers.ValidationError("Data Końca Zadania nie może być pusta")
    return value


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.ReadOnlyField(source='author.username', read_only=True)
    title = serializers.CharField(required=True, max_length = 200)
    description = serializers.CharField(required=False)
    complete_status = serializers.ChoiceField(choices=Status, default=Status.NOTSTARTED)
    created = serializers.DateField(read_only=True)
    deadline = serializers.DateTimeField(validators=[validate_deadline], required = True)
    responsible = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    label = serializers.ChoiceField(choices=LabelsToDoList, default=LabelsToDoList.DEFAULT)
    priority = serializers.ChoiceField(choices=TaskPriority, default=TaskPriority.LEVEL5)
    list = serializers.PrimaryKeyRelatedField(queryset=List.objects.all(), required=False, allow_null=True)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('imie', instance.imie)
        instance.title = validated_data.get('nazwisko', instance.nazwisko)
        instance.description = validated_data.get('data_dodania', instance.data_dodania)
        instance.complete_status = validated_data.get('miesiac_urodzenia', instance.miesiac_urodzenia)
        instance.created = validated_data.get('druzyna', instance.druzyna)
        instance.deadline = validated_data.get('druzyna', instance.druzyna)
        instance.responsible = validated_data.get('druzyna', instance.druzyna)
        instance.label = validated_data.get('druzyna', instance.druzyna)
        instance.priority = validated_data.get('druzyna', instance.druzyna)
        instance.list = validated_data.get('druzyna', instance.druzyna)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = User
        fields = ['__all__']