from django.urls import path, include
from . import views


app_name = "search"

urlpatterns = [
    path('', views.index, name='index'),
    path('word', views.word, name='word'),
]
