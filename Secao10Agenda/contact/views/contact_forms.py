from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.http import Http404
from contact.models import Contact
from django.core.paginator import Paginator

# Create your views here.

def create(request):
    if request.method == 'POST':
        print(request.method)
        print()

        # request.POST.get('first_name'): basicamente estamos entramos no metodo post do request e pegando (get) o valor que possui name igual a string fornecida, ou seja, first_name
        print(request.POST.get('first_name'))
        

    context = {

    }

    # Obs.: Mesmo que tenhamos um form na página não necessariamente está implicito que o metodo é POST, quando acessamos a página o metodo é GET, pois estamos apenas visualizando a página, contudo, quando enviamos algo, o metodo é trocado para POST
    print(request.method)
    print()

    return render(
        request,
        'contatc/create.html',
        context
    )