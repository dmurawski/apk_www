from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404, HttpResponse
from .models import Task, List, Status,User
from .serializers import TaskSerializer, ListSerializer,UserSerializer
from rest_framework.reverse import reverse
from django.db.models import Q
from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsResposibleReadOnlyTask,IsResposibleReadOnlyList
from django.contrib.auth import get_user_model

@permission_classes([IsAuthenticated, IsResposibleReadOnlyTask])
class task_list(APIView):
    name = 'Zadania'
    def get(self, request, format=None):
        tasks = Task.objects.all()
        if not self.request.user.is_superuser:
            serializer = TaskSerializer(tasks.filter(responsible=request.user), many=True)
            return Response(serializer.data)
        else:
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)

@permission_classes([IsAuthenticated, IsResposibleReadOnlyTask])
class task_list_filter_title(APIView):
    name = 'Zadania filtrowane po tytule'
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

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class task_post(APIView):
    name = 'Dodaj zadanie'
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsResposibleReadOnlyTask])
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

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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

@permission_classes([IsAuthenticated, IsResposibleReadOnlyTask])
class task_list_complete(APIView):
    name = 'Lista ukończonych zadań'
    def get(self, request, format=None):
        tasks = Task.objects.filter(complete_status=Status.DONE)
        print(tasks)
        serializer = TaskSerializer(tasks.filter(responsible=request.user), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated, IsResposibleReadOnlyTask])
class task_list_uncomplete(APIView):
    name = 'Lista nieukończonych zadań'
    def get(self, request, format=None):
        tasks = Task.objects.filter(~Q(complete_status = Status.DONE))
        print(tasks)
        serializer = TaskSerializer(tasks.filter(responsible=request.user), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated, IsResposibleReadOnlyTask])
class view_all_task_from_list(APIView):
    name = 'Wyswietlenia zadań przypisanych do danej listy'

    def get(self, request, format=None):
        if request.query_params.get('list'):
            tasks = Task.objects.filter(list__task__title__icontains=request.query_params.get('list'))
        else:
            tasks = Task.objects.all()
        if not self.request.user.is_superuser:
            serializer = TaskSerializer(tasks.filter(responsible=request.user), many=True)
            return Response(serializer.data)
        else:
            serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

@permission_classes([IsAuthenticated, IsResposibleReadOnlyTask])
class view_all_task_filter_desc(APIView):
    name = 'Wyswietlenia zadań zawierajace dana fraze w opisie'

    def get(self, request, format=None):
        if request.query_params.get('desc'):
            tasks = Task.objects.filter(description__icontains=request.query_params.get('desc'))
        else:
            tasks = Task.objects.all()
        if not self.request.user.is_superuser:
            serializer = TaskSerializer(tasks.filter(responsible=request.user), many=True)
            return Response(serializer.data)
        else:
            serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

@permission_classes([IsAuthenticated, IsResposibleReadOnlyList])
class list_view(APIView):
    name = 'Lista'
    def get(self, request, format=None):
        lists = List.objects.all()
        if not self.request.user.is_superuser:
            serializer = ListSerializer(lists.filter(author=request.user), many=True)
            return Response(serializer.data)
        else:
            serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)

@permission_classes([IsAuthenticated, IsResposibleReadOnlyList])
class list_view_filter_name(APIView):
    name = 'Listy filtrowane po nazwie'
    def get(self, request, format=None):
        if request.query_params.get('name'):
            lists = List.objects.filter(name__icontains=request.query_params.get('name'))
        else:
            lists = List.objects.all()
        if not self.request.user.is_superuser:
            serializer = ListSerializer(lists.filter(author=request.user), many=True)
            return Response(serializer.data)
        else:
            serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class list_post(APIView):
    name = 'Dodaj liste'
    def post(self, request, format=None):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class list_put(APIView):
    name = 'Edycja listy'
    def get_object(self, pk):
        try:
            return List.objects.get(pk=pk)
        except List.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        list = self.get_object(pk)
        serializer = ListSerializer(list)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        list = self.get_object(pk)
        serializer = ListSerializer(list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class list_delete(APIView):
    name = 'Usuń liste'
    def get_object(self, pk):
        try:
            return List.objects.get(pk=pk)
        except List.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        list = self.get_object(pk)
        serializer = ListSerializer(list)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        list = self.get_object(pk)
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes([IsAuthenticated, IsResposibleReadOnlyList])
class view_all_list_date(APIView):
    name = 'Wyswietlenia list po nazwie'

    def get(self, request, format=None):
        if request.query_params.get('date'):
            lists = List.objects.filter(created__icontains=request.query_params.get('date'))
        else:
            lists = List.objects.all()
        if not self.request.user.is_superuser:
            serializer = ListSerializer(lists.filter(author=request.user), many=True)
            return Response(serializer.data)
        else:
            serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)
