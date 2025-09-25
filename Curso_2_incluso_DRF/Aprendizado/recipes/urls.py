from django.urls import path

from . import views


# 3. colocando o app_name dizemos que a rota dessas urls é recipe, por tanto que usamos a tag url no html django temos que referencia o app_name, ficando recipes:home, recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),

    path('recipes/category/<int:category_id>/', views.category, name="category"),
    # 4. criamos a url de categoria para o usuário poder clicar no link da categoria e acessar

    path('recipes/<int:id>/', views.recipes, name="recipe"),
    #3. no django, quando queremos pegar uma receita específica dinâmicamente colocando o sinal de <> e dentro o nome desse parâmetro, então ficara <id> ou <numero> ou <valor> o django entende automaticamente que esse valor é algo relacionado a isso
    #3.1 Esse parâmetro chamado de id vai vir como parâmetro para a view recipes e deve ser requerido como parâmetro junto ao request
    #3.2 para saber mais no tipos que podemos usar os converters podemos procurar no google path converters do django
]

# 1.
# Caso eu queira um url filha de uma url pai
# Seria assim um exemplo: 
# .../sobre/sobre-equipe-desenvolvedora/
# .../sobre/sobre-a-loja/

# 2.
# Essa url foi incluida pela urls.py do core do projeto, então o nome que lá estiver na string será o nome da url pai dessas urls, se lá estiver '' significa que não possui nome, então as urls podem ser acessadas assim: 
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/sobre/
# http://127.0.0.1:8000/contato/
# Contudo, se lá estiver com algum outro nome então para acessar essas urls terá que ter essa url pai puxando elas. Exemplo: 'recipes'
# http://127.0.0.1:8000/recipes/           #home
# http://127.0.0.1:8000/recipes/sobre/     #sobre
# http://127.0.0.1:8000/recipes/contato/   #contato

