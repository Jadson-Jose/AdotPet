from django.shortcuts import render, get_object_or_404, redirect
from .models import Adocao
from .forms import AdocaoForm


def lista_adocoes(request):
    adocoes = Adocao.objects.all()
    return render(request, 'adocoes/lista_adocoes.html', {'adocoes': adocoes})


def detalhe_adocao(request, pk):
    adocao = get_object_or_404(Adocao, pk=pk)
    return render(request, 'adocoes/detalhe_adocao.html', {'adocao': adocao})


def criar_adocao(request):
    if request.method == 'POST':
        form = AdocaoForm(request.POST)
        if form.id_valid():
            form.save()
            return redirect('lista_adocoes')
    else:
        form = AdocaoForm()
    return render(request, 'adocoes/form_adocao.html' < {'form': form})


def editar_adocao(request, pk):
    adocao = get_object_or_404(Adocao, pk=pk)
    if request.method == 'POST':
        form = AdocaoForm(request.POST, instance=adocao)
        if form.is_valid():
            form.save()
            return redirect('lista_adocoes')
    else:
        form = AdocaoForm(instance=adocao)
    return render(request, 'adocoes/form_adocao.html', {'form': form})


def deletar_adocao(request, pk):
    adocao = get_object_or_404(Adocao, pk=pk)
    if request.method == 'POST':
        adocao.delete()
        return redirect('lista_adocoes')
    return render(request, 'adocoes/confirmar_deletar_adocao.html', {'adocao': adocao})
