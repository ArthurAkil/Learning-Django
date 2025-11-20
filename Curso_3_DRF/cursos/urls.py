# Define as rotas (URLs) da sua API e liga cada rota à view correspondente

from django.urls import path 
# from .views import CursoAPIView, AvaliacaoAPIView
from .views.curso_views import CursoAPIView, CursoDetailAPIView
from .views.avaliacao_views import AvaliacaoAPIView, AvaliacaoDetailAPIView 

urlpatterns = [
    # Cursos:
    path('cursos/', CursoAPIView.as_view(), name='cursos'), 
    path('cursos/<int:id>/', CursoDetailAPIView.as_view(), name='curso'), 
    path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:id>/', AvaliacaoDetailAPIView.as_view(), name="avaliacao")
]

# as_view(): Converte a classe CursoAPIView em uma view “funcional”.
# Name: Nome da rota. Útil para redirecionamentos, reverses, etc.
# No django DRF o front não utiliza o name, contudo, de maneira interna o back-end usa em redirecionamentos, testes, gerar URLs dinamicamente dentro do backend, organizar rotas