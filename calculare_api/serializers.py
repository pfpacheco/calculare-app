from rest_framework import serializers
from .models import *

        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'

class DetalhesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalhes
        fields = '__all__'

class MateriaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materiais
        fields = '__all__'

class MeuNegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeuNegocio
        fields = '__all__'

class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = '__all__'

class EntregasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entregas
        fields = '__all__'

class OutrasDespesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutrasDespesas
        fields = '__all__'

class DBIngredientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DBIngredientes
        fields = '__all__'