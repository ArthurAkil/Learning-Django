from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    # 3. Forma criando uma variável dentro
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class': 'class a class b',
            'placeholder':'Aqui veio da variavel'                
            } 
        ),
        label='Primeiro nome',
        # O help_text deve ser renderizado para aparecer no html (create.html)
        help_text='Texto de ajuda para seu usuário', 
    )


    # 2.Forma criando um init
    # Aqui estamos atualizando o widget que já estava no meu campo
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    #     self.fields['first_name'].widget.attrs.update({
    #         'class': 'class a class b',
    #         'placeholder':'Aqui veio do __init__'
    #     })


    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
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
    

