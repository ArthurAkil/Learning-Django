from django.shortcuts import render

# Create your views here.
def index(request):

    context ={}

    return render(request, 'blog/pages/index.html', context)

def page(request):

    context ={}

    return render(request, 'blog/pages/page.html', context)

def post(request):

    context ={}

    return render(request, 'blog/pages/post.html', context)