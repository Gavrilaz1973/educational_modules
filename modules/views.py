from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from modules.models import Module
from modules.serializers import ModuleSerializer, ModuleCreateSerializer


class ModuleCreateView(CreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleCreateSerializer
    permission_classes = [IsAdminUser]


class ModuleListView(ListAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ModuleDestroyView(DestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAdminUser]


class ModuleRetrieveView(RetrieveAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]


class ModuleUpdateView(UpdateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAdminUser]

