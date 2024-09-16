from django import forms

from adotante.models import Adotante


class AdotanteForm(forms.ModelForm):
    class Meta:
        model = Adotante
        fields = ['nome', 'email', 'telefone', 'endereco', 'data_nascimento']
