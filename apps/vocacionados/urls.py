
from django.urls import path
from apps.vocacionados import views

urlpatterns = [
    path('list_vocacionados/', views.vocacionados, name="list_vocacionados"),
    path('detalhes_vocacionados/<str:pk>', views.vocacinado_detalhes, name='detalhes_vocacionados'),
    path('export_vocacionados_pdf/', views.export_pdf, name='export_vocacionados_pdf'),
    path('export_vocacionados_excel/', views.export_excel, name='export_vocacionados_excel'),

]

