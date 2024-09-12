from django.urls import path

from apps.voluntarios import views

urlpatterns = [
    path('list_voluntarios/', views.voluntarios, name="list_voluntarios"),
    path('export_voluntarios_pdf/', views.export_pdf, name='export_voluntarios_pdf'),
    path('export_voluntarios_excel/', views.export_excel, name='export_voluntarios_excel'),

]
