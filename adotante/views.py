from django.shortcuts import render, get_object_or_404, redirect
from .models import Adotante
from .forms import AdotanteForm

def lista_adotantes(request):
    ...