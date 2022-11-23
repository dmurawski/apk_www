from django.contrib.auth.decorators import permission_required
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404, HttpResponse
from .models import Osoba, Druzyna
from .serializers import DruzynaSerializer, OsobaSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated,IsAuthenticatedOrReadOnly])
class osoba_list(APIView):
    def get(self, request, format=None):
        if request.query_params.get('imie'):
            osoby = Osoba.objects.filter(imie__icontains=request.query_params.get('imie'))
        else:
            osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby.filter(owner=request.user), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated,IsAuthenticatedOrReadOnly])
class osoba_detail(APIView):
    def get_object(self,pk):
        try:
            return Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        osoba = self.get_object(pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

class osoba_put(APIView):
    def get_object(self, pk):
        try:
            return Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        osoba = self.get_object(pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        osoba = self.get_object(pk)
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class osoba_delete(APIView):
    def get_object(self, pk):
        try:
            return Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        osoba = self.get_object(pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        osoba = self.get_object(pk)
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def druzyna_list(request):
    if request.method == 'GET':
        druzyny = Druzyna.objects.all()
        serializer = DruzynaSerializer(druzyny, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DruzynaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def druzyna_detail(request, pk):
    try:
        druzyna = Druzyna.objects.get(pk=pk)
    except Druzyna.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        druzyna = Druzyna.objects.get(pk=pk)
        serializer = DruzynaSerializer(druzyna)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DruzynaSerializer(druzyna, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        druzyna.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def CustomAuthToken(request):
    return Response({
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  #
        })

def person_view(request, pk):
    if not request.user.has_perm('class3app.view_osoba'):
        raise PermissionDenied()
    try:
        osoba = Osoba.objects.get(pk=pk)
        return HttpResponse(f"Ten użytkownik nazywa się {osoba.imie}")
    except Osoba.DoesNotExist:
        return HttpResponse(f"W bazie nie ma użytkownika o id={pk}.")