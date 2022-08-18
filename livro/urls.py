from django.urls import path
from . import views # o ponto referencia a propria pasta em que o arquivo está. (livro)

urlpatterns = [
    path('cadastrar/', views.cadastrar),
]
