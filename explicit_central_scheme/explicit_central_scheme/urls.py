from django.urls import path

from . import views

urlpatterns = [
    path('plot/', views.plotECS),
]
