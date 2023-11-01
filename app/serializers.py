from rest_framework import serializers
from .models import Aluno



class AlunosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aluno
        fields = ['nome', 'idade', 'nota_primeiro_semestre', 'nota_segundo_semestre', 'nome_professor', 'numero_sala']

    
    