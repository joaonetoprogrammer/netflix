from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

#def homepage(request):
#    return render(request,"homepage.html")

class HomePage(TemplateView):
    template_name = "homepage.html"

#def homefilmes(request):
#    context = {}
#    lista_filmes = Filme.objects.all()
#    context['lista_filmes'] = lista_filmes
#    return render(request,"homefilmes.html", context)

class HomeFilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme

class DetalhesFilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme