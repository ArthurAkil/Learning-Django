"""
URL configuration for project project.

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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Todo path recebe uma string o nome do caminho e uma função e essa função requer uma http request nela como parâmetro e teronar uma response
#*
# HTTP REQUEST <--> HTTP RESPONSE *#
# O cliente faz uma request e response é o que o servidor responde

# para fazer seria assim:
# from django.http import HttpResponse
# def my_view(request):
#     return HttpResponse("Uma linda string")


# Metodos de requisição:
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Reference/Methods

# Códigos de status:
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Reference/Status