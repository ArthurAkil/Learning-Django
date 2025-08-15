from django.db import models
from utils.model_validators import validate_png
from utils.images import resize_image
# Create your models here.

class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'
    
    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)

    site_setup = models.ForeignKey('SiteSetup', on_delete=models.CASCADE, blank=True, null=True, default=None)

    def __str__(self):
        return self.text
    

class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'
    
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)

    # shows:
    show_header = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)

    # icone do site
    favicon = models.ImageField(
        upload_to='assets/favicon/%Y/%m',
        blank=True,
        default='',
        validators=[validate_png],
    )

    # com isso estamos sobrescrevendo o metodo save original do django, se não puxarmos o super nele teriamos que escrever tudo que ele faz manualmente
    def save(self, *args, **kwargs):
        # pegamos o nome do favicon já existente
        current_fav_icon_name = str(self.favicon.name)
        
        super().save(*args, **kwargs)
        
        # definimos como falso porque nenhuma imagem foi alterada ainda
        changed_favicon = False

        # se existir favicon faça isso
        if self.favicon:
            # verificação, o nome do favicon antigo (current) é diferente do novo (self.favicon), se sim foi trocado o favicon (True), se não (False)
            changed_favicon = current_fav_icon_name != self.favicon.name

        # se o favicon foi trocado, vamos redimensionar
        if changed_favicon:
            resize_image(self.favicon, 32)

    
    def __str__(self):
        return self.title
    