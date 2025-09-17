from django.urls import path
from recipes.views import home, contato, sobre

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre)
]

# Caso eu queira um url filha de uma url pai
# Seria assim um exemplo: 
# .../sobre/sobre-equipe-desenvolvedora/
# .../sobre/sobre-a-loja/

# Essa url foi incluida pela urls.py do core do projeto, então o nome que lá estiver na string será o nome da url pai dessas urls, se lá estiver '' significa que não possui nome, então as urls podem ser acessadas assim: 
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/sobre/
# http://127.0.0.1:8000/contato/
# Contudo, se lá estiver com algum outro nome então para acessar essas urls terá que ter essa url pai puxando elas. Exemplo: 'recipes'
# http://127.0.0.1:8000/recipes/           #home
# http://127.0.0.1:8000/recipes/sobre/     #sobre
# http://127.0.0.1:8000/recipes/contato/   #contato