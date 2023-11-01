from django.urls import path
from .views import Alunos, Aluno

urlpatterns = [
    
    path('app/', Alunos.as_view()),
    path('app/<int:id>/', Aluno.as_view())
    
]