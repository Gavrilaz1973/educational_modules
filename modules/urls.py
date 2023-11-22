from django.urls import path
from modules.apps import ModulesConfig
from modules.views import ModuleListView, ModuleCreateView, ModuleUpdateView, ModuleRetrieveView, ModuleDestroyView

app_name = ModulesConfig.name

urlpatterns = [
    path('', ModuleListView.as_view(), name='module_list'),
    path('create/', ModuleCreateView.as_view(), name='module_create'),
    path('update/<int:pk>/', ModuleUpdateView.as_view(), name='module_update'),
    path('retrieve/<int:pk>/', ModuleRetrieveView.as_view(), name='module_retrieve'),
    path('destroy/<int:pk>/', ModuleDestroyView.as_view(), name='module_destroy'),
]