from django.urls import path

from . import views

urlpatterns = [
    path('advance', views.Portal.as_view(), name='url_portal'),
]

