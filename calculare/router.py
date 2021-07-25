from calculare_api.viewsets import ReceitaViewset, DetalhesViewset, MateriaisViewset, MeuNegocioViewset, FuncionariosViewset, EntregasViewset, OutrasDespesasViewset, DBIngredientesViewset
from rest_framework import routers
from users.viewsets import UserViewset

router = routers.DefaultRouter()
router.register('usuario', UserViewset)
router.register('receita', ReceitaViewset)
router.register('detalhes', DetalhesViewset)
router.register('materiais', MateriaisViewset)
router.register('meunegocio', MeuNegocioViewset)
router.register('funcionarios', FuncionariosViewset)
router.register('entregas', EntregasViewset)
router.register('outrasdespesas', OutrasDespesasViewset)
router.register('dbingredientes', DBIngredientesViewset)