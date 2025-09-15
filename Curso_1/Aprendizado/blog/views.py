from django.shortcuts import render
from django.http import HttpResponse
from blog.data import posts
from django.http import Http404

# Create your views here.

# Function based views != Class Based views

# Function based views:
def blog(request):
    print('isso deve aparecer no cmd, BLOG')

    context ={
        'text': 'Estamos no blog, texto que veio do text (view) e adicionado como valor de variável no base.html',
        'apresentation': 'Blog',
        'posts': posts
    }

    return render(request, 'blog/index.html', context)

def post(request, id):
    print('isso deve aparecer no cmd, post id', id)

    post_exists = "Post não encontrado"
    post_found = None

    for post in posts:
        if post['id'] == id:
            post_exists = "Post encontrado"
            post_found = post
            break
    
    # exceção 
    if post_found is None:
        raise Http404('Esse post não existe')

    context ={
        'text': 'Estamos no blog/Post, texto que veio do text (view) e adicionado como valor de variável no base.html',
        'apresentation': 'Blog/Post',
        'post': post_found,
        'exists': post_exists
    }

    return render(request, 'blog/post.html', context)

def exemplo(request):
    print('isso deve aparecer no cmd, BLOG/exemplo/')

    context ={
        'text': 'Estamos no blog/exemplo, texto que veio do text (view) e adicionado como valor de variável no base.html',
        'apresentation': 'Blog/Exemplo'
    }

    return render(request, 'blog/exemplo.html', context)