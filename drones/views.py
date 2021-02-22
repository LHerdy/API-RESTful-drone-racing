from django.urls import reverse
from rest_framework import generics
from rest_framework.response import Response

from drones.models import DroneCategoria, Drone, Piloto, Competicao
from drones.serializers import DroneCategoriaSerializer, DroneSerializer, PilotoSerializer, CompeticaoSerializer


class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategoria.objects.all()
    serializer_class = DroneCategoriaSerializer
    name = 'dronecategory-list'


class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneCategoria.objects.all()
    serializer_class = DroneCategoriaSerializer
    name = 'dronecategory-detail'


class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'


class PilotList(generics.ListCreateAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    name = 'pilot-list'


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    name = 'pilot-detail'


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competicao.objects.all()
    serializer_class = CompeticaoSerializer
    name = 'competition-list'


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competicao.objects.all()
    serializer_class = CompeticaoSerializer
    name = 'competition-detail'


