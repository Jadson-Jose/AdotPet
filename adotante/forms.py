from django import forms

from adotante.models import Adotante


class AdotanteForm(forms.ModelForm):
    class Meta:
        model = Adotante
        fields = '__all__'
