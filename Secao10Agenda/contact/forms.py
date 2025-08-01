from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
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

class RegisterUpdateForm(forms.ModelForm):
    # configurando cada campo que sobrepoe o campo do models
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Campo obrigatório.',
        error_messages={
            'min_length': 'Texto inválida, adicione mais duas letras',
        }
    )

    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Campo obrigatório'
    )

    email = forms.EmailField(
        required=True
    )

    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label='Password 2',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',}),
        help_text='Use a mesma senha do campo anterior',
        required=False,
    )

    # O meta mostrará os campos que serão vistos na tela
    class Meta:
        model = User
        fields = ('first_name','last_name','email',
                  'username',)
    
    # função que salva as senhas no banco de dados que queremos alterar , até agora apenas mudamos os valores e não salvamos no banco de dados
    # commit=True (manda para o banco de dados)
    # commit=False (não manda para o banco de dados)
    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        # salvamos os valores dentro de user mas não salvamos no banco de dados AINDA
        user = super().save(commit=False) 

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user
    
    # função de VALIDAÇÃO, ela é rodada ANTES de salvar para comparar as duas senhas e confirmar se são iguais antes de salvar
    def clean(self):
        
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                # se forem diferentes lança uma exceção, e o texto referente fica a baixo do campo password2
                self.add_error('password2',
                            ValidationError('As senhas não são iguais', code='invalid'))

        return super().clean()
    

    # função de VALIDAÇÃO com finalidade de comparar o email novo que eu quero trocar com o antigo e verificar se são diferentes, se forem verifica se o email novo ja está cadastrado no banco de dados
    def clean_email(self):
        email = self.cleaned_data["email"]
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este email', code='invalid')
                )

        return email
    
    # função de VALIDAÇÃO para validar a senha para se tornar uma senha forte
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1',
                               ValidationError(errors))
        return password1
            
            

            

        