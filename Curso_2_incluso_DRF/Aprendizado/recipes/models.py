from django.db import models

# 5. Para entender mais sobre queryset podemos ler mais sobre na documentação https://docs.djangoproject.com/pt-br/3.2/ref/models/querysets/
# https://docs.djangoproject.com/pt-br/3.2/topics/db/models/
# https://docs.djangoproject.com/pt-br/3.2/topics/db/queries/

# 4. importamos o User para utilizar uma referencia em um campo de recipes
from django.contrib.auth.models import User

# PARA VER MAIS SOBRE OS TIPOS DO MODEL https://docs.djangoproject.com/pt-br/3.2/ref/models/fields/
# Create your models here.



# 2. criamos uma outra tabela de categoria para ser relacionada com as receitas, ela deve ser criadas antes pois recipe utiliza ela (recipe tem dependência mas categoria não)
class Category(models.Model):
    name = models.CharField(max_length=50)

    # 5. criamos a função def __str__(self) para que quando essa categoria for apontada ou mostrada em algum canto não fique um nome padrão do tipo "category (1), category (2), category (3)", em vez disso, quando criamos essa função o retorno dessa função fica da seguinte forma "Jantar, Almoço, Lanche" (diferentes categorias das refeições durante o dia) e o return vai retornar o name a qual definimos
    def __str__(self):
        return self.name

# 1. para criar um mode primeiro colocamos a class, nome que escolhemos e models.Model, depois adicionamos os atributos da tabela com o respectivo tipo, charfield = varchar e por ai vai
class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    # 1.1 auto_now_add é bom para quando for criar, já o auto_now é bom para quando for atualizar
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    # 1.2 em relação a imagemfield nós temos que decidir onde elas serão salvas e podemos definir o caminho com upload_to, o caminho para a pasta seria %Y uma pasta ano, dentro dela %m uma pasta mês e dentro dela %d uma pasta dias
    # 1.3 para usar imagens no python precisamos utilizar o pillow
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')

    # 3. relação que categoria tem com recipe e vice e versa, então uma receita tem uma categoria e uma categoria pode referenciar receitas dentro dela
    # 3.1 o on_delete serve para se algo relacionado for apagado, no tipo se a categoria for apagada, o que acontece com as receitas? definimos se queremos que elas sejam apagadas juntas ou só referencia a categoria que foi apagada agora como null, e para não gerar erros definimos que esse atributo pode ser null com o comando null=True
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    # 4.1 aqui referenciamos que um autor está referenciado a um usuário (padrão do django) e que segue a mesma lógica de categoria no relacional, uma receita só pode ter um autor e um autor pode ter várias receitas
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    


