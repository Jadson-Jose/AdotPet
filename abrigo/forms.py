from django import forms

from abrigo.models import Abrigo

class AbrigoForm(forms.ModelForm):
    class Meta:
        model = Abrigo
        fields = '__all__'