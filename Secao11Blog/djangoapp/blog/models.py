from django.db import models
from utils.rands import slugify_new

# Create your models here.

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
        max_length=150,
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
    
