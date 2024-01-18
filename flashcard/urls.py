from django.urls import path
from . import views

urlpatterns = [
    path('novo_flashcard/', views.novo_flashcard, name='novo_flashcard'),
    path('deleta_flashcard/<int:id>', views.deletar_flashcard, name= 'deleta_flashcard'),
    path('iniciar_desafio/', views.iniciar_desafio, name='iniciar_desafio'),
]