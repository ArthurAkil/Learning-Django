from django.db import models
from utils.rands import slugify_new
from django.contrib.auth.models import User
from utils.images import resize_image
from django_summernote.models import AbstractAttachment

# Create your models here.
class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name

        current_file = str(self.file.name)
        super_save = super().save(*args, **kwargs)
        file_changed = False
        if self.file:
            file_changed = current_file != self.file.name

        if file_changed:
            resize_image(self.file, 900, True, 70)
        return super_save

class Tag(models.Model):
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tag"
    
    name = models.CharField(max_length=150)
    # slug vai servir como chave primária ou ID
    slug = models.SlugField(
        # unico pois queremos como chave primária
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 5)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=150)

    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 5)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name
    
class Page(models.Model):
    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default="",
        null=False, blank=True, max_length=255
    )
    is_published= models.BooleanField(default=False,
                                      help_text='Este campo precisará estar marcado para a página estar visível publicamente')
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title
    
class Post(models.Model):
    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default="", null=False, blank=True, max_length=255
    )
    # Breve resumo
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(default=False, help_text="Este campo deverá estar marcado para ser visível publicamente")
    content = models.TextField()

    # Imagens
    cover = models.ImageField(upload_to='posts/%Y/%m', blank=True, default='')
    cover_in_post_content = models.BooleanField(default=True, help_text='Exibe a imagem de capa também dentro do post')

    # Data e usuário
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        blank=True, null=True,
        # Para que serve o related_name? O related_name serve para não dar conflito na queryset puxada
        # Quando queremos ver todos os postes que o user criou colocamos user.post_set.all(), contudo isso da conflito pois é o nome padrão, então se tivermos duas que puxam (uma quando criou e outra quando atualizou) da um conflito e erro, por isso mudamos o nome
        # Agora com o related_name podemos fazer o seguinte se quisermos APENAS os posts criados = user.post_created_by.all
        related_name='post_created_by')

    updated_at = models.DateTimeField(auto_now=True)
    updated_by =  models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        blank= True, null=True, 
        # user.post_update_by.all
        related_name="post_update_by")

    # Outras relações
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    tags = models.ManyToManyField(Tag, blank=True, default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title,4)

        current_cover = str(self.cover.name)
        
        super_save = super().save(*args, **kwargs)
        
        cover_changed = False

        if self.cover:
            cover_changed = current_cover != self.cover.name

        if cover_changed:
            resize_image(self.cover, 900, True, 70)
        return super_save

    def __str__(self):
        return self.title

