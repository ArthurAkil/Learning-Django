from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from ..models import Avaliacao
from ..serializers import AvaliacaoSerializer

class AvaliacaoAPIView(APIView):
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AvaliacaoDetailAPIView(APIView):
    def get(self, request, id):
        avalicao = get_object_or_404(Avaliacao, pk=id)
        serializer = AvaliacaoSerializer(avalicao, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        avaliacao = get_object_or_404(Avaliacao, pk=id)
        serializer = AvaliacaoSerializer(avaliacao, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, id):
        avalicao = get_object_or_404(Avaliacao, pk=id)
        serializer = AvaliacaoSerializer(avalicao, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        avaliacao = get_object_or_404(Avaliacao, pk=id)
        avaliacao.delete()
        return Response({"Msg": "Avaliação deletada com sucesso."}, status=status.HTTP_200_OK)