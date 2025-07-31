from django.shortcuts import render, redirect
from contact.forms import RegisterForm
# enviar mensagens para o usuario:
from django.contrib import messages

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
            messages.success(request, 'Usuário registrado')
            form.save()
            return redirect('contact:index')
            
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )