"""capsdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from material.frontend import urls as frontend_urls
from caps.views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(frontend_urls)),
    url(r'^gerarFicha/(?P<id>[0-9]+)/$', gerarFicha),


    url(r"^$", home, name="index.htm"),


    url(r"^sair/", sair, name="sair"),
    url(r"^loginform.htm", loginform, name="loginform.htm"),

    url(r"^pacientecad.htm", pacientecad, name="pacientecad"),

    url(r"^cadastrapaciente", cadastrapaciente, name="cadastrapaciente"),


    # Material Design
    url(r"^home2", home2, name="home2"),
    url(r"^pacienteman", pacienteman, name="pacienteman"),
    url(r"^pacientelist$", pacientelist, name="pacientecad"),

    # Controle de usuarios
    url(r"^login/", logar, name="logar"),

    # Profissionais
    url(r"^horarioMaker", horarioMaker, name="horarioMaker"),
    url(r"^newhorario", newhorario, name="newhorario"),
    url(r"^horariolist", horariolist, name="horariolist"),
    url(r"^cadprofissionais", profissionaislist, name="cadprofissionais"),
    url(r"^profissionais", profissionais, name="profissionais"),


    # Consulta dos profissionais
    url(r"^consultas", consultas, name="consultas"),
    url(r"^cadconsulta", cadconsulta, name="cadconsulta"),
    url(r"^marcarconsulta", marcarconsulta, name="marcarconsulta"),
    url(r"^remConsulta", remConsulta, name="remConsulta"),
    # Visão dos profissionais
    url(r"^minhasconsultas", minhasconsultas, name="minhasconsultas"),



    # Evolução dos pacientes
    url(r"^evolucaopacientes", evolucaopacientes, name="evolucaopacientes"),



    url(r"^relatorio", gerarRelatorio, name="relatorio"),





    url(r"^teste", teste, name="teste"),
    url(r"^jsont", jsont, name="jsont"),


    url(r"^login/", logar, name="logar"),
    # url(r"^userMan/", userMan, name="userMan"),


    url(r"^paci/", paci, name="paci"),


    # Dias disponíveis de um profissional
    url(r"^diasDisponiveis/", diasDisponiveis, name="diasDisponiveis"),

    # Muda o status da consulta
    url(r"^changeStatus", changeStatus, name="changeStatus"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
