from django.urls import path
from . import views


app_name = 'kenchi'


urlpatterns = [
    path('', views.index, name='index'),
]