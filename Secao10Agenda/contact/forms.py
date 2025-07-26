from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            )
    
    # clean: a função clean serve para verificar os dados enviado e fazer o tratamento de erros caso tenha
    def clean(self):
        # tudo preenchido no form será guardado nessa variável
        # cleaned_data = self.cleaned_data
        
        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )
        return super().clean()

