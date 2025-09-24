from django.db import models

# Create your models here.

# 1. para criar um mode primeiro colocamos a class, nome que escolhemos e models.Model, depois adicionamos os atributos da tabela com o respectivo tipo, charfield = varchar e por ai vai
class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    # 1.1 auto_now_add é bom para quando for criar, já o auto_now é bom para quando for atualizar
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    # 1.2 em relação a imagemfield nós temos que decidir onde elas serão salvas e podemos definir o caminho com upload_to, o caminho para a pasta seria %Y uma pasta ano, dentro dela %m uma pasta mês e dentro dela %d uma pasta dias
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')


