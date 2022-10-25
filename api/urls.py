from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes/', views.GetNotes, name="notes"),
    path('notes/<str:pk>/', views.GetNote, name="note"),
]