from rest_framework import serializers
from .models import Curso, Avaliacao

# Serializer? É uma classe do DRF que: 
# transforma modelos em JSON (saída)
# valida dados recebidos (entrada)

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__' # serialize todos os campos do model Curso

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
            # ➡ O campo email pode ser enviado na entrada (POST/PUT), (Quando alguem faz um cadastro e envia no json os dados)
            # mas NÃO aparece na resposta JSON. (nos dados ou seja solicitou os dados de um perfil o email não vai)
        }
        model = Avaliacao
        fields = [
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criado_em',
            'atualizado_em',
            'ativo'
        ]