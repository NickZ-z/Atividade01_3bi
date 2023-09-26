import django_filters
from .models import Reserva
from django import forms

class ReservaFilter(django_filters.FilterSet):
    nome_empresa = django_filters.CharFilter(lookup_expr='icontains', label='Nome da Empresa')
    quitado = django_filters.BooleanFilter(label='Quitado?')
    valor_stand = django_filters.NumberFilter(field_name='reserva__valor',lookup_expr='gte', label='Valor do Stand (R$)')
    data_reserva = django_filters.DateFilter(label='Data da Reserva', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Reserva
        fields = ['nome_empresa','quitado','reserva','cnpj','categoria_empresa','data_reserva','valor_stand']