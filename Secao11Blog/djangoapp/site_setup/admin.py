from django.contrib import admin
from site_setup.models import MenuLink, SiteSetup

# Register your models here.

# Explicação: Como fizemos o menulink por meio do inline, ele será apresentado dentro do setup em uma linha para ser preenchida e adicionada pelo setup
 
# @admin.register(MenuLink)
# class MenuLinkAdmin(admin.ModelAdmin):
#     list_display = 'id','text', 'url_or_path'
#     list_display_links = 'id','text', 'url_or_path'
#     search_fields = 'id','text', 'url_or_path'

# Inline (tabularInline): a classe criada e não adicionada a nenhuma não causa tanta impacto mas quando adicionada a outra classe do admin vira uma tabela onde determinada classe que está inline possa ser adicionada por meio de outra classe.
# Ex.: SiteSetup possui menulinks, mas eu tinha que criar os menulinks por fora e depois ir para sitesetup, com o inline dentro do site setup: agora pode-se adicionar quantos menulinks quiser e tudo isso pela classe sitesetup
class MenuLinkInline(admin.TabularInline):
    # modelo a ser adicionada no inline:
    model = MenuLink
    # quantas tabelas extras fica para ser preenchidas
    extra = 1

@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title','description'
    inlines = MenuLinkInline,

    # função do botão de adicionar algo naquele model do admin
    def has_add_permission(self, request):
        return not SiteSetup.objects.exists()