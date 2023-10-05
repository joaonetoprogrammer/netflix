from django.urls import path, include
from .views import HomePage, HomeFilmes, DetalhesFilme

app_name = 'filme'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('filmes/', HomeFilmes.as_view(), name='homefilme'),
    path('filmes/<int:pk>', DetalhesFilme.as_view(), name='detalhesfilme'),


]