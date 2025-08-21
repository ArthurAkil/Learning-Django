from random import SystemRandom
import string

# server para deixar o texto sem acento e sem espaço: 'olá pessoa' = 'ola-pessoa', 'chame atenção' = 'chame-atencao'
from django.utils.text import slugify

# gerar chaves únicas
def random_letters(k=5):
    # vai tudo se juntar a uma string vazia, um conjunto de letras com números, k é o limite de caracteres, ja definimos na função (começo))
    return ''.join(SystemRandom().choices(
        string.ascii_letters + string.digits,
        k=k
    ))

# agora criamos um novo slugify que pega o resultado do random letters e adiciona ao final do texto
def slugify_new(text, k=5):
    return slugify(text) + '-' + random_letters(k)
