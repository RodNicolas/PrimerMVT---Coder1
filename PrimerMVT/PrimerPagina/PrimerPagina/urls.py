"""PrimerPagina URL Configuration

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
from PrimerPagina.views import familia, miembrosFamilia
from django.template import Template,Context
from PrimerApp.views import estaFamilia, elLimon, laLimita, elPato



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', familia),
    path('miembrosFamilia/', miembrosFamilia),
    path('estaFamilia/', estaFamilia),
    path('elLimon/', elLimon),
    path('laLimita/', laLimita),
    path('elPato/', elPato),
    
]
