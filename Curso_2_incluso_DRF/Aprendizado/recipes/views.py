from django.http import HttpResponse

# 2. Por isso temos o render, que vai renderizar um html, assim não precisamos digitar um html inteiro dentro dessas views
from django.shortcuts import render

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
    return render(request, 'recipes/home.html', context={
        'name': 'Tutu'
    })

def contato(request):
    return HttpResponse('CONTATO')

def sobre(request):
    return HttpResponse('SOBRE')