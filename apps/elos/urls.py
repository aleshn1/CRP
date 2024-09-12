from django.urls import path

from apps.elos import views

urlpatterns = [
    path('elos/', views.elos, name="elos"),
]