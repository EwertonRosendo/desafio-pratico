from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Aluno(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    nota_primeiro_semestre = models.CharField(max_length=5)
    nota_segundo_semestre = models.CharField(max_length=5)
    nome_professor = models.CharField(max_length=50)
    numero_sala = models.CharField(max_length=4)

    def __str__(self) :
        return self.nome