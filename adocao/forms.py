from django import forms

from adocao.models import Adocao


class AdocaoForm(forms.ModelForm):
    class Meta:
        model = Adocao
        fields = '__all__'
