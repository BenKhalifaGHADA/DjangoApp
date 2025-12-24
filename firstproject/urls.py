"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include


from rest_framework import routers
from firstApp.views import TaskViewSet
router=routers.DefaultRouter()
router.register('tasks', TaskViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstapp/',include('firstApp.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('api/', include(router.urls)) #ici je veux utiliser le route d'un projet pour cela nous avons ajouté les configurations nécessaires au dessus 
   
    
]
