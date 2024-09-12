# -*- encoding: utf-8 -*-

from crp import settings
from django.conf.urls.static import static
from django.urls import path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
