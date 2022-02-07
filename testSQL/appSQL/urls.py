from django.urls import path

from . import views

urlpatterns = [
    path('advance', views.Teste.as_view(), name='url_teste'),
]

