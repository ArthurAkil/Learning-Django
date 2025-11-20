from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from ..models import Curso
from ..serializers import CursoSerializer

class CursoAPIView(APIView):
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CursoDetailAPIView(APIView):
    def get(self, request, id):
        # é necessário o parâmetro id, ser chamado assim igual na url/cursos/<int:id>, se fosse <int:codigo> o parametro seria código na função
        curso = get_object_or_404(Curso, pk=id)
        serializer = CursoSerializer(curso, many=False)
        # many=False: pois só queremos um argumento
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        curso = get_object_or_404(Curso, pk=id)
        serializer = CursoSerializer(curso, data=request.data)
        # put: tudo é alterado dos atributos, então colocamos o data=request.data depois validamos e salvamos
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, id):
        curso = get_object_or_404(Curso, pk=id)
        serializer = CursoSerializer(curso, data=request.data, partial=True)
        # patch: apenas alguns dados são alterados, então colocamos o data=request.data e partial=True depois validamos e salvamos
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        curso = get_object_or_404(Curso, pk=id)
        curso.delete()
        return Response({"Msg": "Deletado com sucesso"}, status=status.HTTP_200_OK)