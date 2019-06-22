from django.urls import path

from .views import index, get_response

urlpatterns = [
    path('', index, name='index'),
    path('get-response/', get_response, name='get_response'),
]
