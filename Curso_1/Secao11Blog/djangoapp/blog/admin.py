from django.contrib import admin
from blog.models import Tag, Category, Page, Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug'
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug'
    list_per_page = 10
    ordering = '-id',
    # significa que o canto de slug vai pegar o canto de name
    prepopulated_fields = {
        "slug": ('name',),
    }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug'
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug'
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('name',),
    }

@admin.register(Page)
class Page(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'title', 'is_published',
    list_display_links = 'title',
    search_fields = 'id', 'title', 'is_published',
    list_per_page = 50
    list_filter = 'is_published',
    list_editable = 'is_published',
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('title',),
    }

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # Podemos saber mais do summernote pesquisando no google, mas no geral ele tem sua propria config no django e serve para a textarea ser mais completa em configurações (B, sublinhado, escolher espaçamento, etc)
    summernote_fields = ('content',)
    list_display = 'id', 'title','is_published','created_by'
    list_display_links = 'title',
    search_fields = 'id', 'title', 'slug', 'excerpt', 'is_published', 'content',
    list_per_page = 20
    list_filter = 'category', 'is_published'
    list_editable = 'is_published',
    ordering = '-id',
    readonly_fields = 'created_at', 'updated_at', 'updated_by', 'created_by',
    prepopulated_fields = {
        "slug": ('title',),
    }
    autocomplete_fields = 'tags', 'category',

    # Desse model save do admin nos queremos o change, pois o change mostra quando algo é alterado (ja existia e foi alterado), se for criado ele retorna false
    def save_model(self, request, obj, form, change):
        if change:
            print(f'Está alterando?{change}')
            obj.updated_by = request.user
        else:
            print(f'Não está alterando, está criando')
            obj.created_by = request.user
        obj.save()