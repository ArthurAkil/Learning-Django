from django.contrib import admin
from .models import Category

# Register your models here.
# Aqui registraremos o models que já criamos no admin para aparecer no http://127.0.0.1:8000/admin/

# 1. primeiro registramos a qual model a class admin se referencia com @admin.register(nomeDoModel)
@admin.register(Category)
# 1.1 registramos a classe no admin da seguinte forma "nomeDoModelAdmin", fica melhor para leitura, e então referênciamos a admin.ModelAdmin
class CategoryAdmin(admin.ModelAdmin):
    ...


