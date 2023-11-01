from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import AlunosSerializer

from .models import Aluno as AlunoModel

import requests
class Alunos(APIView):

    def get(self, request, *args, **kwargs):
        data = AlunosSerializer(Aluno.objects.all(), many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
        
    def post(self, request, *args, **kwargs):
        serializer = AlunosSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response({'status':'aluno cadastrado'}, status=status.HTTP_201_CREATED)
        return Response({'error':'algo deu errado'}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        aluno = AlunoModel.objects.get(id=request.data['id'])
        serializer = AlunosSerializer(instance=aluno, data=request.data)
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
        