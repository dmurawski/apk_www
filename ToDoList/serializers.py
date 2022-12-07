from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import Task, Status, LabelsToDoList, TaskPriority
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
    deadline = serializers.DateField(validators=[validate_deadline], required = True)
    responsible = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    label = serializers.ChoiceField(choices=LabelsToDoList, default=LabelsToDoList.DEFAULT)
    priority = serializers.ChoiceField(choices=TaskPriority, default=TaskPriority.LEVEL5)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.complete_status = validated_data.get('complete_status', instance.complete_status)
        instance.created = validated_data.get('created', instance.created)
        instance.deadline = validated_data.get('deadline', instance.deadline)
        instance.responsible = validated_data.get('responsible', instance.responsible)
        instance.label = validated_data.get('label', instance.label)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = User
        fields = ['__all__']