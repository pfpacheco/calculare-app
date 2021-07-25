import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class DBIngredientesFilter(django_filters.FilterSet):
    # Nome = CharFilter(field_name='Nome', lookup_expr='icontains')

    class Meta:
        model = DBIngredientes
        fields = '__all__'

class MeusIngredientesFilter(django_filters.FilterSet):

    class Meta:
        model = MeusIngredientes
        fields = '__all__'

class ReceitaFilter(django_filters.FilterSet):

    class Meta:
        model = Receita
        fields = ('id', 'Nome_da_Receita', 'categoria')