from django.shortcuts import render, redirect, get_object_or_404
from contact. forms import ContactForm
from contact.models import Contact

# consegue passar dados para que ele consiga retornar dados 
from django.urls import reverse


# Create your views here.

def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form,
            'form_action': form_action,
        }

        # verifica se há algum erro no formulario é valido
        if form.is_valid():
            print('formulário é valido')
            # podemos fazer isso antes de salvar no banco de dados caso queira alterar algo do contato antes de salvar
            # estamos salvando os dados dentro de contatc, contudo não estamos salvando ele no banco de dados commit=False
            # ex.: commit=False
            contact = form.save()
            
            # alteramos algo dentro dele
            # contact.show = False
            
            # envia o formulario para o banco de dados do contato alterado
            # form.save()

            return redirect('contact:update', contact_id=contact.pk)

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
        'form': ContactForm(),
        'form_action': form_action,
    }
    return render(
        request,
        'contatc/create.html',
        context
    )

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,
        }
        print('post')

        if form.is_valid():
            print('formulário é valido')
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contatc/create.html',
            context
        )

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }
    print('get')
    return render(
        request,
        'contatc/create.html',
        context
    )