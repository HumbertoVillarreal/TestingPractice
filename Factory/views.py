from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Factory, Line, Machine
from .serializers import FactorySerializer, LineSerializer, MachineSerializer


def mock_factory():
    print("MOCKUP TEST")
    


# Create your views here.
class FactoryViewSet(ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        mock_factory()
        serializer.save(created_by=self.request.user)


class LineViewSet(ModelViewSet):
    queryset = Line.objects.all()
    serializer_class = LineSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class MachineViewSet(ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

