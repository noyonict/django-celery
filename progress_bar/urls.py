from django.urls import path
from .views import index, status

urlpatterns = [
    path('', index, name='index'),
    path('api/status/', status, name='status'),
]