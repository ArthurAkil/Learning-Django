from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Function based views != Class Based views

# Function based views:
def home(request):
    print('isso deve aparecer no cmd, HOME')

    context = {
        'text': 'Estamos na home, texto que veio do text (view) e adicionado como valor de variável no base.html',
        'apresentation': 'Home'
    }

    return render(
        request, 
        'home/index.html', 
        context
    )
