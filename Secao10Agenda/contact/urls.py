from django.urls import path
from contact import views

app_name = 'contatc'

urlpatterns = [
    path('', views.index, name='index'),
]