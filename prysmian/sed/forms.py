from django import forms
from .models import Sed

class SedForm(forms.ModelForm):
    class Meta:
        model = Sed
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'numero_equipamento': forms.TextInput(attrs={'class': 'form-control'}),
            'setor_insercao': forms.TextInput(attrs={'class': 'form-control'}),
            'modalidade': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'origem': forms.TextInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'transportadora': forms.TextInput(attrs={'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'agente': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_carga': forms.NumberInput(attrs={'class': 'form-control'}),
            'carga_no_chao': forms.Select(attrs={'class': 'form-control'}),
        }
