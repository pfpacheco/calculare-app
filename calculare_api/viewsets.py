from rest_framework import viewsets
from . import models
from . import serializers


class UsuarioViewset(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

class ReceitaViewset(viewsets.ModelViewSet):
    queryset = models.Receita.objects.all()
    serializer_class = serializers.ReceitaSerializer

class DetalhesViewset(viewsets.ModelViewSet):
    queryset = models.Detalhes.objects.all()
    serializer_class = serializers.DetalhesSerializer

class MateriaisViewset(viewsets.ModelViewSet):
    queryset = models.Materiais.objects.all()
    serializer_class = serializers.MateriaisSerializer


class MeuNegocioViewset(viewsets.ModelViewSet):
    queryset = models.MeuNegocio.objects.all()
    serializer_class = serializers.MeuNegocioSerializer

class FuncionariosViewset(viewsets.ModelViewSet):
    queryset = models.Funcionarios.objects.all()
    serializer_class = serializers.FuncionariosSerializer

class EntregasViewset(viewsets.ModelViewSet):
    queryset = models.Entregas.objects.all()
    serializer_class = serializers.EntregasSerializer

class OutrasDespesasViewset(viewsets.ModelViewSet):
    queryset = models.OutrasDespesas.objects.all()
    serializer_class = serializers.OutrasDespesasSerializer

class DBIngredientesViewset(viewsets.ModelViewSet):
    queryset = models.DBIngredientes.objects.all()
    serializer_class = serializers.DBIngredientesSerializer