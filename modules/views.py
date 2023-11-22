from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView

from modules.models import Module
from modules.serializers import ModuleSerializer


class ModuleCreateView(CreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    # permission_classes = [IsSuperuser]


class ModuleListView(ListAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    # permission_classes = [IsSuperuser]


class ModuleDestroyView(DestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    # permission_classes = [IsSuperuser]


class ModuleRetrieveView(RetrieveAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    # permission_classes = [IsOwnerOrStaff]


class ModuleUpdateView(UpdateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    # permission_classes = [IsOwnerOrStaff]

