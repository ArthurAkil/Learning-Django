from django.shortcuts import render
from contact. forms import ContactForm

# Create your views here.



def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }
        return render(
            request,
            'contatc/create.html',
            context
        )
        # request.POST.get('first_name'): basicamente estamos entramos no metodo post do request e pegando (get) o valor que possui name igual a string fornecida, ou seja, first_name
        # print(request.POST.get('first_name'))
        
    # Obs.: Mesmo que tenhamos um form na página não necessariamente está implicito que o metodo é POST, quando acessamos a página o metodo é GET, pois estamos apenas visualizando a página, contudo, quando enviamos algo, o metodo é trocado para POST
    # print(request.method)
    # print()

    context = {
        'form': ContactForm()
    }
    return render(
        request,
        'contatc/create.html',
        context
    )