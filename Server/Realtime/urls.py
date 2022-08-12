from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.Storage.as_view(), name='add'),
]