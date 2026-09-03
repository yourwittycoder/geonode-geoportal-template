# -*- coding: utf-8 -*-

from django.urls import path
from django.shortcuts import render

from geonode.urls import urlpatterns, handler500


def sustain_homepage(request):
    return render(request, 'sustain_home.html')


urlpatterns = [
    path('', sustain_homepage, name='home'),
] + urlpatterns
