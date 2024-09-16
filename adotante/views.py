from django.shortcuts import render, get_object_or_404, redirect
from .models import Adotante
from .forms import AdotanteForm


def lista_adotantes(request):
    adotantes = Adotante.objects.all()
    return render(request, 'adotantes/lista_adotantes.html', {'adotantes': adotantes})


def detalhe_adotante(request, pk):
    adotante = get_object_or_404(Adotante, pk=pk)
    return render(request, 'adotantes/detalhe_adotante.html', {'adotante': adotante})


def criar_adotante(request):
    if request.method == 'POST':
        form = AdotanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_adotantes')
    else:
        form = AdotanteForm()
    return render(request, 'adotantes/form_adotante.html', {'form': form})


def editar_adotante(request, pk):
    adotante = get_object_or_404(Adotante, pk=pk)
    if request.method == 'POST':
        form = AdotanteForm(request.POST, instance=adotante)
        if form.is_valid():
            form.save()
            return redirect('lista_adotantes')
    else:
        form = AdotanteForm(instance=adotante)
    return render(request, 'adotantes/form_adotante.html', {'form': form})


def deletar_adotante(request, pk):
    adotante = get_object_or_404(Adotante, pk=pk)
    if request.method == 'POST':
        adotante.delete()
        return redirect('lista_adotantes')
    return render(request, 'adotantes/confirmar_deletar_adotante.html', {'adotante': adotante})
