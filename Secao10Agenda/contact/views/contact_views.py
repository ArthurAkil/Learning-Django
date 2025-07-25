from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
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

def search(request):
    # Request.GET: basicamente pegamos o que o search informa com o request.GET, o valor será um query dict, um dicionario, no qual o valor pesquisado será guardado no valor q (definido no _header.html)
    # Request.GET.get('q', ''):  basicamente faz com que puxamos uma função do python para pegar o valor q, só que, se ele não achar valor nenhum (alguém apagar a parte do http que mostra o q), ele retorna um valor vazio ''
    # Request.GET.get('q', '').strip(): uma pessoa pode digitar vários espaços na pesquisa, ex.: '    tutu      ' e colocar para pesquisar, o strip() retira isso
    search_value = request.GET.get('q', '').strip()
    
    # Condicional: se o valor for vázio (mesmo que tenha muitos espaços o strip() já deixou filé pra gente) ele vai redirecionar para o index, tirando assim o valor pesquisado e voltando a url padrão index
    if search_value == '':
        return redirect('contact:index')

    # Filtragem com trecho do nome: Imagine que colocamos nico (de nicole, nicolas), queremos que mostre todos os resultados que possuem "nico", utilizando o filter e o __icontains=XY fazemos isso
    #  Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value): Mas arthur como fariamos para pesquisa nico nos dois nomes? Não simultaneamente tipo Nico (first name) and Nico (last name) como se fosse uma filtragem disso nos dois, mas pesquisasse se tivesse nico em um OU no outro, importamos a ferramenta Q do django que faz a gente utilizar o | (pipe), fazemos a semântica de colocar o Q antes de cada tópico que será verificado e podemos substituir onde seria uma virgula por um | (pipe)
    contacts = Contact.objects \
    .filter(show=True) \
    .filter(
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value)
        ) \
    .order_by('-id')

    context = {
        'contacts': contacts,
        'site_title': 'Search - ',
        'search_value': search_value,
    }

    return render(
        request,
        'contatc/index.html',
        context
    )