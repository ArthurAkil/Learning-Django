from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# Id (primary key - automatico pelo django)
# first_name (string), last_name(string), phone(string)
# email (email), created_date(date), description(text)

# picture (image)
# category (foreign key), show (boolean), 
# owner (foreign key)

class Category(models.Model):
    # A classe meta serve para ajustar a palavra que é mostrada, muitas vezes o django não interpreta bem o singular e plural das palavras, então podemos ajudar isso
    class Meta:
        # Nome singular:
        verbose_name = 'Category'
        
        # Nome plural:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/', blank=True)

    # cascade = resulta que todos os contatos que possuem essa categoria sejam apagados junto a categoria apagada (CUIDADO - PERIGOSO)
    # SET_NULL = após a categoria ser apagada, os contatos que possuiam essa categoria terão como categoria NULA
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    owner = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    


    