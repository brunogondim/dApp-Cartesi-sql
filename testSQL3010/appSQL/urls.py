from django.urls import path

from . import views

urlpatterns = [
    path('advance', views.Advance.as_view(), name='url_advance'),
    path('inspect/<whatHex>', views.Inspect.as_view(), name='url_inspect'),
]

