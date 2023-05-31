"""
URL configuration for recetas project.

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
from django.contrib import admin
from django.urls import path
from apprecetas.views import crear_receta, actualizar_receta, detalle_receta, lista_recetas

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('recetas/', pantalla_inicial)
    path('recetas/', crear_receta),
    path('recetas/', actualizar_receta, name = 'actualizar_receta'),
    path('recetas/', detalle_receta, name = 'detalle_receta'),
    path('recetas/', lista_recetas, name = 'lista_recetas')
]
