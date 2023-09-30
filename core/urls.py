"""
URL configuration for auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logoutuser, name='logout'),
    path('bis', include('bis.urls')),
    path('civil', include('civil.urls')),
    path('cnp', include('cnp.urls')),
    path('ele', include('ele.urls')),
    path('fna', include('fna.urls')),
    path('fns', include('fns.urls')),
    path('gailtel', include('gailtel.urls')),
    path('hr', include('hr.urls')),
    path('inst', include('inst.urls')),
    path('mech', include('mech.urls')),
    path('ops', include('ops.urls')),
    path('pipeline', include('pipeline.urls')),

]