from django.shortcuts import render, get_list_or_404, redirect
from .models import Animal
from .forms import AnimalForm
from django.contrib.auth.decorators import login_required


def lista_animais(request):
    animais = Animal.objects.all()
    return render(request, 'animais/lista_animais.html', {'animais': animais})


def detalhe_animal(request, pk):
    animal = get_list_or_404(animal, pk=pk)
    return render(request, 'animais/detalhe.html')


@login_required
def criar_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_animais')
        else:
            form = AnimalForm()
        return render(request, 'animais/formulario.html', {'form': form})


def editar_animal(request, pk):
    animal = get_list_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('detalhe_animal.html')
    else:
        form = AnimalForm(instance=animal)
        return render(request, 'animal/formulario.html', {'form': form})


def deletar_animal(request, pk):
    animal = get_list_or_404(Animal, pk=pk)
    if request.method == 'POST':
        animal.delete()
        return redirect('lista_animais')
    return render(request, 'animais/confirmar_delecao.html', {'animal': animal})
