"""
URL configuration for projeto project.

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
from django.urls import path, include
from django.http import HttpResponse
from home import views as home_views
from blog import views as blog_views

#Http trabalha de forma REQUEST <---> RESPONSE
#O django trabalha de forma MODEL VIEW TEMPLATE (MVT) (variação do MODEL VIEW CONTROLER MVC)


#A url funciona dessa forma:
# http://127.0.0.1:8000 (padrão home)
# http://127.0.0.1:8000/blog (home do blog ou blog)
# http://127.0.0.1:8000/blog/articles 
# http://127.0.0.1:8000/blog/articles/comments
# http://127.0.0.1:8000/blog/articles/categories
# http://127.0.0.1:8000/blog/articles/authors
# seguimos uma linha de páginas, o proprio django nos ajuda a fazer isso
# utilizamos o INCLUDE

# está sendo chamado FBV
urlpatterns = [
    path('',include('home.urls')),
    path('blog/',include('blog.urls')),
    path('admin/', admin.site.urls),
]
