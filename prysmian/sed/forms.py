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

    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            value = cleaned_data.get(field)
            
            # Verifica se o campo é um campo booleano e converte o valor
            if field == 'carga_no_chao' and isinstance(value, str):
                if value.upper() == 'TRUE':
                    cleaned_data[field] = True
                elif value.upper() == 'FALSE':
                    cleaned_data[field] = False

            # Para outros campos, converte strings para maiúsculas
            elif isinstance(value, str):
                cleaned_data[field] = value.upper()

        return cleaned_data
