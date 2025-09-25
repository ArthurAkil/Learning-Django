from django.http import HttpResponse

# 2. Por isso temos o render, que vai renderizar um html, assim não precisamos digitar um html inteiro dentro dessas views
from django.shortcuts import render

# 6. importamos um código que gera receitas fakes para função de teste
from utils.recipes.factory import make_recipe

from .models import Recipe, Category
# 7. importamos do models a receita

# Create your views here.
def home(request):
    # 1. O recomendado não é assim mas na aula está indo aos poucos para entender que isso deve retornar um html
    # return HttpResponse('''<!DOCTYPE>
    #                     <html>
    #                         <head><title>Olá Mundo!</title></head>
    #                         <body>
    #                             <h1>Olá mundo!</h1>
    #                         </body>
    #                     </html> ''')

    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    # 7.1 fazemos um queryset de todas as receitas existentes no banco de dados (colocamos na ordem invertida, as mais novas primeiro), filtramos a query para apenas as que estão publicadas, e guardamos na variavel recipes 


    return render(request, 'recipes/pages/home.html', context={
    # 3. O render (quando passamos o mouse em cima da função dá pra ver isso) precisa de um request e um "template name", contudo, não é nome em si mas sim o caminho até o template que está localizado em tal arquivo
    # 4. Apertando ctrl e clicando no render vamos na função em si e podemos ver claramente todos os parâmetros, como contexto (variáveis para dentro do template), status http, e por ai vai
        'recipes': recipes,
        # 6.1 'recipes': [make_recipe() for _ in range(10)] se colocassemos apenas a função sem ser em uma lista, ele criaria apenas uma receita, então colocamos uma lista que vai rodar 10 vezes e gerar 10 receitas

        # 7.2 'recipes': recipes nessa forma estamos passando a nossa queryset no contexto
    })

    # {% comment %} Para acessar as variaveis informadas no contexto, usamos duas chaves ex.: {{ variavel }} {% endcomment %}
    # <h1>O nome do contexto é: {{ name }}</h1>

# 5. recebemos um outro argumento como id nessa função para acessar um objeto específico dentre várias outros, então, na recipes/urls.py colocamos na view recipes que ele tem um parâmetro id sendo pedido e precisamos colocar esse parâmetro na função tbm
def recipes(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    # 8. Podemos filtrar a queryset de recipes usando uma ForeignKey (chave estrangeira).
    #    Para isso, usamos o nome do campo que representa a ForeignKey,
    #    seguido de dois underlines (__), e em seguida o nome do atributo
    #    do model relacionado (no caso, Category).
    #       
    # Exemplo:
    #   category__id   → filtra pelo id da categoria
    #   category__name → filtra pelo nome da categoria
    #
    # Aqui usamos category__id=category_id porque recebemos o id da categoria como argumento da função (category_id) e filtramos também pelas que apenas estão com is_published=True
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
    })