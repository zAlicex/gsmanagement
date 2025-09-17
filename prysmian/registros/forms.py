from django import forms
from .models import Carga

class CargaForm(forms.ModelForm):
    SIM_NAO = [
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    ]

    carga_no_chao = forms.ChoiceField(
        choices=SIM_NAO,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Carga no chão"
    )

    krona_ok = forms.ChoiceField(
        choices=[(True, 'Sim'), (False, 'Não')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Krona"
    )

    golden_ok = forms.ChoiceField(
        choices=[(True, 'Sim'), (False, 'Não')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Golden"
    )

    contrato = forms.ChoiceField(
        choices=[('', 'Seleccione...'), ('Retornável', 'Retornável'), ('Descartável', 'Descartável')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Contrato"
    )

    class Meta:
        model = Carga
        fields = '__all__'
        widgets = {
            'data_insercao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'valor_carga': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            value = cleaned_data.get(field)
            
            # Para os campos de "Sim/Não", converte para True ou False
            if field in ['krona_ok', 'golden_ok'] and isinstance(value, str):
                if value == 'Sim':
                    cleaned_data[field] = True
                elif value == 'Não':
                    cleaned_data[field] = False

            # Para outros campos de texto, converte para maiúsculas
            elif isinstance(value, str):
                cleaned_data[field] = value.upper()

        return cleaned_data
