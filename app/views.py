from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import AlunosSerializer

from .models import Aluno as AlunoModel


class Alunos(APIView):
    @swagger_auto_schema(manual_parameters=[
    openapi.Parameter('id', openapi.IN_QUERY, description="ID do aluno", type=openapi.TYPE_INTEGER),
    openapi.Parameter('nome', openapi.IN_QUERY, description="Nome do aluno", type=openapi.TYPE_STRING)
])

    def get(self, request, *args, **kwargs):
        data = AlunosSerializer(AlunoModel.objects.all(), many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
        
    def post(self, request, *args, **kwargs):
        if request.data:
            data = request.data
        else:
            data = {
                    "nome":"rosendo",
                    "idade":18,
                    "nota_primeiro_semestre":"9.98",
                    "nota_segundo_semestre":"10.00",
                    "nome_professor":"carlos henrique",
                    "numero_sala":"223"
                    }

        serializer = AlunosSerializer(data=data)
        if serializer.is_valid() :
            serializer.save()
            return Response({'status':'aluno cadastrado'}, status=status.HTTP_201_CREATED)
        return Response({'error':'algo deu errado'}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        if request.data:
            data = request.data
        else:
            data = {
                    "id":3,
                    "nome":"rosendo",
                    "idade":7,
                    "nota_primeiro_semestre":"9.98",
                    "nota_segundo_semestre":"10.00",
                    "nome_professor":"carlos henrique",
                    "numero_sala":"223"
                    }
        aluno = AlunoModel.objects.get(id=data['id'])
        serializer = AlunosSerializer(instance=aluno, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'deu bom'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Aluno(APIView):
    def delete(self, request, id, *args, **kwargs):
        data = AlunoModel.objects.get(id=id)
        data.delete()
        return Response({'status':'deletado com sucesso'}, status=status.HTTP_202_ACCEPTED)
    
    def get(self, request, id, *args, **kwargs):
        data = AlunosSerializer(AlunoModel.objects.get(id=id)).data
        return Response(data, status=status.HTTP_202_ACCEPTED)
        