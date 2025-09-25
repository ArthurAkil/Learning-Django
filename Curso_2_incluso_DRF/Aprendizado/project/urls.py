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
# 2. incluir outra urls de outros app no arquivo urls do core do projeto
from django.urls import path, include

from django.conf.urls.static import static
# 3.o static serve para configurar os arquivos staticos nas urls

from django.conf import settings
# 3.1 importante para quando for importar algo do settings do project, fazemos isso
# podia fazer direto from project import settings, mas é recomendado usar o django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # Deixando sem nada '' fica igual um home, mas se deixarmos como 'recipes/' então definimos que essa é a url pai, então as proximas urls serão: 
    # http://127.0.0.1:8000/recipes/x, http://127.0.0.1:8000/recipes/y, http://127.0.0.1:8000/recipes/z
    path('', include('recipes.urls'))
]

# 3.2 += pois vamos concatenar esse arquivo com o outro urlpatterns acima
# Mas arthur qual a função? A função disso é que agora as imagens que são links clicaveis agora abrem a imagem no navegador caso você queira ver de maneira separada, exemplo "abrir imagem em outra aba" parecido com isso
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 3.3 Podemos fazer a mesma coisa para static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# 1. Todo path recebe uma string o nome do caminho e uma função e essa função requer uma http request nela como parâmetro e teronar uma response
#*
# HTTP REQUEST <--> HTTP RESPONSE *#
# O cliente faz uma request e response é o que o servidor responde
# para fazer seria assim:
# from django.http import HttpResponse
# def my_view(request):
#     return HttpResponse("Uma linda string")
# Mas ficaria insustentável deixar todas as funções de view onde está já as urls
# Metodos de requisição:
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Reference/Methods
# Códigos de status:
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Reference/Status