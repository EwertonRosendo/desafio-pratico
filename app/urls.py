from django.urls import path
from .views import Alunos, Aluno

from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    
    path('app/', Alunos.as_view()),
    path('app/<int:id>/', Aluno.as_view()),
    
]