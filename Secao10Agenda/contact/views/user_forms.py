from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
# messages: enviar mensagens para o usuario (pop up)
from django.contrib import auth, messages

# fazemos esse import para pegar a ferramenta para requerer que o usuario esteja logado
from django.contrib.auth.decorators import login_required


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

# view para fazer o login
def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        # criamos o form para ser preenchido, utilizando um form específico de autenticação
        form = AuthenticationForm(request, data=request.POST)

        # verificamos se o form é valido com os dados preenchidos
        if form.is_valid():
            # procuramos o usuario referente ao form
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            print(user)
            return redirect('contact:index')
        
        # tratamento de erro caso o form não seja valido
        messages.error(request, 'Usuário ou senha incorreto.')
    
    # retorno de o metodo não for POST
    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )

@login_required(login_url='contact:login')
# view para fazer o logout da conta logada
def logout_view(request):
    auth.logout(request)
    messages.error(request, 'Você deslogou de sua conta.')

    return redirect('contact:login')

# requeremos que o usuario esteja logado para acessar essa view e caso não esteja será direcionado para contact:login
@login_required(login_url='contact:login')
# view para alterar os dados do usuário
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
    print(request.method)

    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            auth.login(request, request.user)
            messages.success(request, 'Update concluído')
            return redirect('contact:user_update')

    return render(request,
                  'contact/user_update.html',
                  {'form': form})


