from django.contrib import admin
from .models import Livros, Categoria

admin.site.register(Categoria)
admin.site.register(Livros) # registrando a model Livro na area administrativa. 
