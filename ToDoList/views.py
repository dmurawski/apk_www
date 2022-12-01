from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404, HttpResponse
from .models import Task, List, Status
from .serializers import TaskSerializer
from rest_framework.reverse import reverse
from django.db.models import Q


class task_list(APIView):
    name = 'Zadania'
    def get(self, request, format=None):
        if request.query_params.get('title'):
            tasks = Task.objects.filter(title__icontains=request.query_params.get('title'))
        else:
            tasks = Task.objects.all()
        if not self.request.user.is_superuser:
            serializer = TaskSerializer(tasks.filter(responsible=request.user), many=True)
            return Response(serializer.data)
        else:
            serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class task_post(APIView):
    name = 'Dodaj zadanie'
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class task_detail(APIView):
    name = 'Zadanie'
    def get_object(self,pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

class task_put(APIView):
    name = 'Edycja zadania'
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class task_delete(APIView):
    name = 'Usuń zadanie'
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class task_list_complete(APIView):
    name = 'Lista ukończonych zadań'
    def get(self, request, format=None):
        tasks = Task.objects.filter(complete_status=Status.DONE)
        print(tasks)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class task_list_uncomplete(APIView):
    name = 'Lista nieukończonych zadań'
    def get(self, request, format=None):
        tasks = Task.objects.filter(~Q(complete_status = Status.DONE))
        print(tasks)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)