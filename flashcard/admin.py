from django.contrib import admin
from .models import Categoria, Flashcard, Desafio, FlashcardDesafio
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Flashcard)
admin.site.register(Desafio)
admin.site.register(FlashcardDesafio)