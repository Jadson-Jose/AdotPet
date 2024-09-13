from django.shortcuts import render, get_list_or_404, redirect
from .models import Abrigo
from .forms import AbrigoForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def lista_abrigo(request):
    abrigos = Abrigo.objects.all()
    return render(request, 'abrigo/lista_abrigo.html', {'abrigos': abrigos})


def detalhe_abrigo(request, pk):
    abrigo = get_list_or_404(abrigo, pk=pk)
    return render(request, 'abrigo/detalhe_abrigo.html', {'abrigo': abrigo})


@login_required
def criar_abrigo(request):
    if (request.method == 'POST'):
        form = AbrigoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_abrigos')
        else:
            form = AbrigoForm()
        return render(request, 'abrigos/form_abrigo.html.', {'form': form})


def editar_abrigo(request, pk):
    abrigo = get_list_or_404(Abrigo, pk=pk)
    if request.method == 'POST':
        form = AbrigoForm(request.POST, instance=abrigo)
        if form.is_valid():
            form.save()
            return redirect('lista_abrigos')
    else:
        form = AbrigoForm(instance=abrigo)
        return render(request, 'abrigos/form_abrigo.html', {'form': form})


def deletar_abrigo(request, pk):
    abrigo = get_list_or_404(Abrigo, pk=pk)
    if request.method == 'POST':
        abrigo.delete()
        return redirect('lista_abrigos')
    return render(request, 'abrigos/confirmar_deletar_abrigo.html', {'abrigo': abrigo})
