from django.http import HttpResponse

# 2. Por isso temos o render, que vai renderizar um html, assim não precisamos digitar um html inteiro dentro dessas views
from django.shortcuts import render

# 6. importamos um código que gera receitas fakes para função de teste
from utils.recipes.factory import make_recipe

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

    # 3. O render (quando passamos o mouse em cima da função dá pra ver isso) precisa de um request e um "template name", contudo, não é nome em si mas sim o caminho até o template que está localizado em tal arquivo
    # 4. Apertando ctrl e clicando no render vamos na função em si e podemos ver claramente todos os parâmetros, como contexto (variáveis para dentro do template), status http, e por ai vai
    return render(request, 'recipes/pages/home.html', context={
        # 6.1 se colocassemos apenas a função sem ser em uma lista, ele criaria apenas uma receita, então colocamos uma lista que vai rodar 10 vezes e gerar 10 receitas
        'recipes': [make_recipe() for _ in range(10)],
    })

    # {% comment %} Para acessar as variaveis informadas no contexto, usamos duas chaves ex.: {{ variavel }} {% endcomment %}
    # <h1>O nome do contexto é: {{ name }}</h1>

# 5. recebemos um outro argumento como id nessa função para acessar um objeto específico dentre várias outros, então, na recipes/urls.py colocamos na view recipes que ele tem um parâmetro id sendo pedido e precisamos colocar esse parâmetro na função tbm
def recipes(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
    })