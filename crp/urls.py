# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),  
    path("", include("apps.authentication.urls")),  # Auth routes - login / register

    # ADD NEW Routes HERE
    path("", include("apps.vocacionados.urls")),
    path("", include('apps.members.urls')),
    path("", include("apps.home.urls")),
    path("", include("apps.voluntarios.urls")),
    path("", include("apps.pastorais.urls")),
    path("", include("apps.elos.urls")),
    path("", include("apps.historico.urls")),
]
