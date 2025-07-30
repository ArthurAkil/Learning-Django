from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models


class ContactForm(forms.ModelForm):
    # 3. Forma criando uma variável dentro
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #         'class': 'class a class b',
    #         'placeholder':'Aqui veio da variavel'                
    #         } 
    #     ),
    #     label='Primeiro nome',
    #     # O help_text deve ser renderizado para aparecer no html (create.html)
    #     help_text='Texto de ajuda para seu usuário', 
    # )


    # 2.Forma criando um init
    # Aqui estamos atualizando o widget que já estava no meu campo
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['first_name'].widget.attrs.update({
    #         'class': 'class a class b',
    #         'placeholder':'Aqui veio do __init__'
    #     })

    # picture: com isso a gente diz ao django que no campo que o usuario clica para adicionar uma imagem só queremos o campo de click para carregar um arquivo e nada mais, além disso, colocamos para aceitar qualquer imagem
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category', 'picture'
            )
        
        # Para modificar os fields podemos fazer de 3 maneiras, assim: você está criando um novo widget para esse input, SÓ PODE UM E NÃO MAIS DE UM
        # 1. os widgets são uma biblioteca do python que dão a possibilidade da gente mudar os tipos dos campos de determinado input, atualmente está o widget de texto em first_name mas agora trocamos para password (esconder o que o usuário digita)
        # widgets = {
        #     'first_name':forms.TextInput(
        #         # atributos: placeholder, classes que quero colocar no input
        #         attrs={
        #             'placeholder':'Escreva aqui'
        #         }
        #     )
        #     # podemos fazer 'last_name': forms.PasswordInput()
        # }
        
    
    # clean: a função clean serve para verificar os dados enviado e fazer o tratamento de erros caso tenha
    # Aqui trabalhamos quando um campo depende do outro, um password e a confirmação de password
    def clean(self):
        # tudo preenchido no form será guardado nessa variável
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'O primeiro nome não pode ser igual ao último nome',
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
    



        return super().clean()
    
    # Aqui retornamos o valor corrigido e tratado de erro
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        print('passei no clean do first_name')

        # tratando exceções
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )

            # existe essa forma com raise ValidationError ou fazendo add.error, a diferença? O validation erro para o código, se tiver mais exceções ele não verifica pois uma ja foi atendida, o add error ve todas que são tratadas
            # raise ValidationError(
            #     'Não digite ABC neste campo',
            #     code='invalid'
            # )
        
        return first_name
    
class RegisterForm(UserCreationForm):
    # Bug: Como estamos utilizando o usercreation, por base ele utiliza como obrigatorio apenas o username e senha como obrigatorio, e a gente adicionou first_name, last_name, email, então os que a gente adiciniou não são obrigatorio, como fazemos para serem obrigatorios?
    # assim:
    first_name = forms.CharField(
        required=True,
        min_length=3,
        # # é possível também fazer um erro personalizado
        # error_messages={
        #     'required': 'Erro bla bla'
        # }
    )

    last_name = forms.CharField(
        required=True,
    )

    email = forms.EmailField(
        required=True,
    )

    # Se adicionamos o meta manual precisamos configurar, caso não utilizamos o padrão do usercreation
    class Meta:
        model = User
        fields=(
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2'
        )

    # verificação de email no banco de dados se já existe ou não
    def clean_email(self):
        email = self.cleaned_data["email"]
        
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este email', code='invalid')
            )

        return email
    