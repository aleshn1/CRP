
from django.urls import path
from . import views

urlpatterns = [
    path('historicos/', views.historico, name='historicos'),
]