from rest_framework.views import APIView 
# Classe base para criar views manuais
# APIView deixa você controlar tudo manualmente.
# Você define explicitamente cada método HTTP.
# Não utiliza o routers, cria manualmente cada rota em urls

from rest_framework.response import Response
from rest_framework import status
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

# Create your views here.

class CursoAPIView(APIView):
    def get(self, request):
        cursos = Curso.objects.all() # Busca todos os cursos do banco (QuerySet (Lista))
        serializer = CursoSerializer(cursos, many=True) # Converte p/ JSON, many=True: converter TODOS os dados. Sem o many, pega apenas um (server para parametros de get específico)
        return Response(serializer.data) # Retorna a lista como resposta ja transformada em JSON

class AvaliacaoAPIView(APIView):
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)