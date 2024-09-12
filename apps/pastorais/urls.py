from django.urls import path

from apps.pastorais import views

urlpatterns = [
    path('pastorais/', views.pastorais, name="pastorais"),
]
