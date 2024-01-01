"""Coplay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from agent.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/story/create', post_create_story),
    path('api/story', get_story),
    path('api/role/create', post_create_role),
    path('api/role/update', post_update_role),
    path('api/scene/create', post_create_scene),
    path('api/scene/update', post_update_scene),
    path('/api/role/communicate', communicate),
    path('/api/timestep/create', create_timestep),
    path('/api/interaction/create', create_interaction),
    path('/api/interaction/update', update_interaction),
    path('/api/interaction/delete', delete_interaction),
    path('/api/interaction/launch', launch_interaction),
    path('/api/story/init', init_story),
    path('/api/story/generate', generate_story)
]
