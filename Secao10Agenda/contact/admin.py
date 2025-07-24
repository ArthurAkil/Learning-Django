from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # Descrição: o listdisplay vai fazer com que o admin organize a tabela de contatc por meio do id de cada, dps firstname, lastname e por fim, phone
    list_display = 'id', 'first_name', 'last_name', 'phone', 'category', 'show',

    # Descrição: ordena em como será mostrado de cima a baixo, podemos deixar o id assim "-id" assim o mais novo fica em cima (pilha)
    ordering = '-id',

    # Descrição: podemos criar uma lista de filtragem também (ideal para categoria que vamos criar no model posteriormente)
    list_filter = 'created_date', 'first_name',

    # Descrição: podemos colocar uma area de pesquisa para procurar algum contact específico
    search_fields = 'id', 'first_name', 'last_name'

    # Descrição: podemos fazer uma paginação pelos contatos já criados
    list_per_page = 10

    # Contexto: existe um botão chamado "mostrar tudo" é bom e ruim, caso tenha uns 50 contatos o botão mostrar tudo é de boa, agora se for 1000 contatos o clique no botão vai dar um hit muito grande na base de dados
    # Descrição: o list_max_show_all então deixa um limite de até quando esse botão fica visível, ou seja, até 50 contatos cadastrados o botão será mostrado, depois fica invisivel
    list_max_show_all = 50

    # Descrição: o list_editable deixa a editação mais prática podendo ser feita pela propria listagem dos contatos, bom e ruim (minha opinião)
    # Error: o list_editable so funciona se o item que você quer deixar editável estiver já sido colocado como opção no list_display
    list_editable = 'first_name', 'category', 'show',

    # Descrição: serve para deixar clicavel a area para acessar aquilo em específico
    # Error: O campo que você quer deixar como link não pode estar no list_editable e como link (o que faz sentido se pode ser editavel tão facil pra que colocar como link)
    list_display_links = 'id', 'phone',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
