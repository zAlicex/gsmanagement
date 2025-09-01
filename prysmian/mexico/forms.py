from django import forms
from .models import Mexico

class MexicoForm(forms.ModelForm):
    class Meta:
        model = Mexico
        fields = '__all__'
        widgets = {
            'fecha_insercion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'sector': forms.TextInput(attrs={'class': 'form-control'}),
            'transportadora': forms.TextInput(attrs={'class': 'form-control'}),
            'placa_tracto': forms.TextInput(attrs={'class': 'form-control'}),
            'placa_remolque': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'origen': forms.TextInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'id_localizador': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_carga': forms.NumberInput(attrs={'class': 'form-control'}),
            'carga_en_piso': forms.TextInput(attrs={'class': 'form-control'}),
            'oficial': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            value = cleaned_data.get(field)
            
            # Para todos os campos de texto, converte strings para maiúsculas
            if isinstance(value, str):
                cleaned_data[field] = value.upper()

        return cleaned_data
