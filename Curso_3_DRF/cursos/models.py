# Importa os módulos de modelos do Django
from django.db import models

# Create your models here.

# Classe abstrata que vai servir de modelo para as outras
class Base(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True) 
    # salva automaticamente a data/hora que o registro foi criado

    atualizado_em = models.DateTimeField(auto_now=True) 
    # salva automaticamente a data/hora que o registro foi atualizado

    ativo = models.BooleanField(default=True) 
    # indica se o registro está ativo ou não

    class Meta:
        abstract = True
        #define a classe como abstrata, só pode ser herdada e não cria tabela no banco de dados

class Curso(Base): # herda da classe abstrata os campos
    titulo = models.CharField(max_length=255)
    url = models.URLField(max_length=200, unique=True)
    # unique serve para nenhuma URL pode se repetir no banco de dados

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        # Define como o model aparece no django admin

    def __str__(self):
        return self.titulo
        # define a representação do objeto como string 
        # Ex.: no admin vai aparecer “Python Básico” ao invés de “Curso object (1)”.

class Avaliacao(Base): # herda da classe abstrata os campos
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    # foreingkey: cria relacionamento N->1 com Curso, cada avaliação pertence a um curso
    #related_name: permite acessar avaliações via curso.avaliações.all()
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        # Define como o model aparece no django admin

        unique_together = ['email', 'curso']
        # Um mesmo e-mail não pode avaliar o mesmo curso duas vezes
        # A combinação desses campos não pode se repetir no banco de dados
        # No DRF → gera um erro 400 Bad Request com mensagem de violação de integridade.

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'
    