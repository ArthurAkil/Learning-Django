# Define as rotas (URLs) da sua API e liga cada rota à view correspondente

from django.urls import path 
from .views import CursoAPIView, AvaliacaoAPIView

urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'), 
    path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes')
]

# as_view(): Converte a classe CursoAPIView em uma view “funcional”.
# Name: Nome da rota. Útil para redirecionamentos, reverses, etc.
# No django DRF o front não utiliza o name, contudo, de maneira interna o back-end usa em redirecionamentos, testes, gerar URLs dinamicamente dentro do backend, organizar rotas