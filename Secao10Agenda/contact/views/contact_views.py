from django.shortcuts import render, get_object_or_404
from django.http import Http404
from contact.models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects \
    .filter(show=True) \
    .order_by('-id') [:10]

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contatc/index.html',
        context
    )

def contact(request, contact_id):
    # podemos utilizar o get = Contact.objects.get(pk=contact_id), contudo se a pessoa digitar no http um id que não existe vai dar erro
    # nesse caso então podemos optar por filter (ué mas filter retorna uma lista (queryset), vai der erro pq queremos um unico valor, exatamente por isso que utilizar o first() pra pegar o primeiro valor que é o contato e o segundo sera none, dai trataremos o erro)

    # single_contact = Contact.objects.filter(pk=contact_id).first()

    # tratamento:
    # if single_contact is None:
    #     raise Http404()

    # O django já sabe que fazer isso é normal e por isso criou a função get_list_or_404, e fica dessa forma agora:
    # Agora podemos falar que o tipo do objeto é Contact, com determinada pk, e que deva possuir o show=True, assim ninguem pode acessar se tiver False (invisível)
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title,
    }

    return render(
        request,
        'contatc/contact.html',
        context
    )