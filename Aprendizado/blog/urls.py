from django.urls import path
from . import views

#Http trabalha de forma REQUEST <---> RESPONSE
#O django trabalha de forma MODEL VIEW TEMPLATE (MVT) (variação do MODEL VIEW CONTROLER MVC)

# Podemos definir um nome do app, assim caso tenhamos varias paginas dentro do blog e quisermos diferenciar (ex.: temos o home do blog, temos a pagina de posts do blog, a pagina exemplo do blog):

app_name = 'blog'

# blog/
# Django URLs:
# https://docs.djangoproject.com/en/4.2/topics/http/urls/
urlpatterns = [
    path('', views.blog, name='home'),
    path('post/<int:id>/',views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo')
]