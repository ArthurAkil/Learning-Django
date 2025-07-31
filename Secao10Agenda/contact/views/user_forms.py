from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
# messages: enviar mensagens para o usuario (pop up)
from django.contrib import auth, messages


def register(request):

    form = RegisterForm()

    # mostrar mensagens para o usuário
    # messages.info(request, 'Um texto qualquer')
    # messages.success(request, 'Um texto qualquer')
    # messages.error(request, 'Um texto qualquer')
    # messages.warning(request, 'Um texto qualquer')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:login')
            
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            print(user)
            return redirect('contact:index')
        messages.error(request, 'Usuário ou senha incorreto.')


    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )

def logout_view(request):
    auth.logout(request)
    messages.error(request, 'Você deslogou de sua conta.')

    return redirect('contact:login')