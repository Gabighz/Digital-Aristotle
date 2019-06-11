from django.urls import path

from . import views
from .views import get_response

urlpatterns = [
    path('', views.index, name='index'),
    path('get-response/', get_response),
]
