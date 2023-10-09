from typing import Any
from django.db.models.query import QuerySet
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

    # adicionando visualizacao no campo visualizacao
    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes +=1
        filme.save()

        return super().get(request, *args, **kwargs)

    # retornando os filmes relacionados dentro do array context
    def get_context_data(self, **kwargs):
        context = super(DetalhesFilme, self).get_context_data(**kwargs)
        filmes_relacionados = self.model.objects.filter(categoria=self.get_object().categoria)
        context['filmes_relacionados'] = filmes_relacionados
        return context

class PesquisaFilme(ListView):
    template_name = "pesquisa.html"
    model = Filme 

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            # verificando se contém aquele termo
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None
