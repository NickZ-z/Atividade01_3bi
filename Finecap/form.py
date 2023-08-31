from .models import *

from django import forms
from django.forms import ModelForm

class ReservaForm(ModelForm):

    class Meta: 
        model = Reserva
        fields = '__all__'
        widgets = {
            'cnpj' : forms.TextInput(attrs={'class': 'form-control' }),
            'nome_empresa' : forms.TextInput(attrs={'class': 'form-control' }),
            'categoria_empresa' : forms.TextInput(attrs={'class': 'form-control' }),
            'quitado': forms.CheckboxInput(attrs={'class': 'form-control' }),
            'reserva': forms.Select(attrs={'class': 'form-control' }),
            
        }

