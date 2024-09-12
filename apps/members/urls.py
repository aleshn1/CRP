from django.urls import path

from apps.members import views

urlpatterns = [
    path('list-members/', views.members, name="list-members"),
    path('member_details/<str:pk>', views.member_details, name='member_details'),
    path('export_pdf/', views.export_pdf, name='export_pdf'),
    path('export_excel/', views.export_excel, name='export_excel'),
]
