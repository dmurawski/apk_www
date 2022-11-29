from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import Task, List, Status, LabelsToDoList, TaskPriority
import datetime

def validate_deadline(value):
    if not value > datetime.date.today():
        raise serializers.ValidationError(
            "Deadline nie może być w przeszłości",
        )
    return value

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    complete_status = serializers.ChoiceField(choices=Status, default=Status.NOTSTARTED)
    created = serializers.DateField()
    deadline = serializers.DateTimeField()
    responsible = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    label = serializers.ChoiceField(choices=LabelsToDoList, default=LabelsToDoList.DEFAULT)
    priority = serializers.ChoiceField(choices=TaskPriority, default=TaskPriority.LEVEL5)
    list = serializers.PrimaryKeyRelatedField(queryset=List.objects.all())

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