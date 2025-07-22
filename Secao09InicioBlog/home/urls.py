from django.urls import path
from . import views

#Http trabalha de forma REQUEST <---> RESPONSE
#O django trabalha de forma MODEL VIEW TEMPLATE (MVT) (variação do MODEL VIEW CONTROLER MVC)

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
]