from django.db import models
from django.db.models.fields import CharField
from users.models import User

categorias = [
    ('Acompanhamentos', 'Acompanhamentos'),
    ('Bolos', 'Bolos'),
    ('Bebidas', 'Bebidas'),
    ('Caldos e Molhos', 'Caldos e Molhos'),
    ('Doces e Sobremesas', 'Doces e Sobremesas'),
    ('Petisco', 'Petisco'),
    ('Pratos', 'Pratos'),
    ('Salgados', 'Salgados'),
    ('Outra Categoria', 'Outra Categoria'),
]

tempo = [
    ('minutos', 'minutos'),
    ('horas', 'horas'),
]

dose = [
    ('Bandeja (20 ovos)', 'Bandeja (20 ovos)'),
    ('Bandeja (30 ovos)', 'Bandeja (30 ovos)'),
    ('Bandeja (30 unidades)', 'Bandeja (30 unidades)'),
    ('Cabeça M (200 g)', 'Cabeça M (200 g)'),
    ('Cabeça M (539 g)', 'Cabeça M (539 g)'),
    ('Cabeça M (65 g)', 'Cabeça M (65 g)'),
    ('Copo (170 g)', 'Copo (170 g)'),
    ('Dúzia (12 ovos)', 'Dúzia (12 ovos)'),
    ('Embalagem (1 kg)', 'Embalagem (1 kg)'),
    ('Embalagem (1 L)', 'Embalagem (1 L)'),
    ('Embalagem (1,030 kg)', 'Embalagem (1,030 kg)'),
    ('Embalagem (1,2 kg)', 'Embalagem (1,2 kg)'),
    ('Embalagem (1,8 kg)', 'Embalagem (1,8 kg)'),
    ('Embalagem (100 g)', 'Embalagem (100 g)'),
    ('Embalagem (150 g)', 'Embalagem (150 g)'),
    ('Embalagem (170 g)', 'Embalagem (170 g)'),
    ('Embalagem (2 kg)', 'Embalagem (2 kg)'),
    ('Embalagem (2,5 kg)', 'Embalagem (2,5 kg)'),
    ('Embalagem (200 g)', 'Embalagem (200 g)'),
    ('Embalagem (200 ml)', 'Embalagem (200 ml)'),
    ('Embalagem (250 g)', 'Embalagem (250 g)'),
    ('Embalagem (3 L)', 'Embalagem (3 L)'),
    ('Embalagem (300 g)', 'Embalagem (300 g)'),
    ('Embalagem (395 g)', 'Embalagem (395 g)'),
    ('Embalagem (400 g)', 'Embalagem (400 g)'),
    ('Embalagem (5 kg)', 'Embalagem (5 kg)'),
    ('Embalagem (500 g)', 'Embalagem (500 g)'),
    ('Embalagem (500 ml)', 'Embalagem (500 ml)'),
    ('Garrafa (1 L)', 'Garrafa (1 L)'),
    ('Garrafa (330 ml)', 'Garrafa (330 ml)'),
    ('Garrafa (375 ml)', 'Garrafa (375 ml)'),
    ('Garrafa (500 ml)', 'Garrafa (500 ml)'),
    ('Garrafa (600 ml)', 'Garrafa (600 ml)'),
    ('Garrafa (740 ml)', 'Garrafa (740 ml)'),
    ('Garrafa (750 ml)', 'Garrafa (750 ml)'),
    ('Garrafa (965 ml)', 'Garrafa (965 ml)'),
    ('Grama (g)', 'Grama (g)'),
    ('Lata (1,7 kg)', 'Lata (1,7 kg)'),
    ('Lata (125 g)', 'Lata (125 g)'),
    ('Lata (170 g)', 'Lata (170 g)'),
    ('Lata (2 kg)', 'Lata (2 kg)'),
    ('Lata (2,400 kg)', 'Lata (2,400 kg)'),
    ('Lata (2,570 kg)', 'Lata (2,570 kg)'),
    ('Lata (200 g)', 'Lata (200 g)'),
    ('Lata (250 g)', 'Lata (250 g)'),
    ('Lata (250 ml)', 'Lata (250 ml)'),
    ('Lata (300 g)', 'Lata (300 g)'),
    ('Lata (350 ml)', 'Lata (350 ml)'),
    ('Lata (365 g)', 'Lata (365 g)'),
    ('Lata (385 g)', 'Lata (385 g)'),
    ('Lata (390 g)', 'Lata (390 g)'),
    ('Lata (400 g)', 'Lata (400 g)'),
    ('Lata (450 g)', 'Lata (450 g)'),
    ('Lata (473 ml)', 'Lata (473 ml)'),
    ('Lata (850 g)', 'Lata (850 g)'),
    ('Lata (950 g)', 'Lata (950 g)'),
    ('Litro (L)', 'Litro (L)'),
    ('Maço (100 g)', 'Maço (100 g)'),
    ('Maço (300 g)', 'Maço (300 g)'),
    ('Maço (400 g)', 'Maço (400 g)'),
    ('Maço M (20 g)', 'Maço M (20 g)'),
    ('Maço M (450 g)', 'Maço M (450 g)'),
    ('Mililitro (ml)', 'Mililitro (ml)'),
    ('Pacote (1 kg)', 'Pacote (1 kg)'),
    ('Pacote (100 g)', 'Pacote (100 g)'),
    ('Pacote (150 g)', 'Pacote (150 g)'),
    ('Pacote (2 kg)', 'Pacote (2 kg)'),
    ('Pacote (200 g)', 'Pacote (200 g)'),
    ('Pacote (250 g)', 'Pacote (250 g)'),
    ('Pacote (300 g)', 'Pacote (300 g)'),
    ('Pacote (5 kg)', 'Pacote (5 kg)'),
    ('Pacote (50 g)', 'Pacote (50 g)'),
    ('Pacote (500 g)', 'Pacote (500 g)'),
    ('Pacote (600 g)', 'Pacote (600 g)'),
    ('Pacote (750 g)', 'Pacote (750 g)'),
    ('Pacote (800 g)', 'Pacote (800 g)'),
    ('Pacote (950 g)', 'Pacote (950 g)'),
    ('Pote (100 g)', 'Pote (100 g)'),
    ('Pote (100g)', 'Pote (100g)'),
    ('Pote (200 g)', 'Pote (200 g)'),
    ('Pote (4,5 kg)', 'Pote (4,5 kg)'),
    ('Pote (400 g)', 'Pote (400 g)'),
    ('Pote (500 g)', 'Pote (500 g)'),
    ('Pote (800 g)', 'Pote (800 g)'),
    ('Quilo (Kg)', 'Quilo (Kg)'),
    ('Ramo M', 'Ramo M'),
    ('Sachê (10 g)', 'Sachê (10 g)'),
    ('Sachê (24 g)', 'Sachê (24 g)'),
    ('Sachê (50 g)', 'Sachê (50 g)'),
    ('Sachê (90 g)', 'Sachê (90 g)'),
    ('Unidade ', 'Unidade '),
    ('Unidade (1 kg)', 'Unidade (1 kg)'),
    ('Unidade (19 g)', 'Unidade (19 g)'),
    ('Unidade (200 g)', 'Unidade (200 g)'),
    ('Unidade (30 ml)', 'Unidade (30 ml)'),
    ('Unidade (700 g)', 'Unidade (700 g)'),
    ('Unidade (750 g)', 'Unidade (750 g)'),
    ('Unidade (800 g)', 'Unidade (800 g)'),
    ('Unidade G (840 g)', 'Unidade G (840 g)'),
    ('Unidade M', 'Unidade M'),
    ('Unidade M (200 g)', 'Unidade M (200 g)'),
    ('Unidade M (575 g)', 'Unidade M (575 g)'),
    ('Unidade M (89 g)', 'Unidade M (89 g)'),
    ('Unidade P (265 g)', 'Unidade P (265 g)'),
]

unidade = [
    ('Por Receita', 'Por Receita'),
]

despesas = [
    ('Combustível', 'Combustível'),
    ('Divulgação', 'Divulgação'),
    ('Taxas/Impostos', 'Taxas/Impostos'),
    ('Telefone', 'Telefone'),
    ('Internet', 'Internet'),
    ('Agua', 'Agua'),
    ('Luz', 'Luz'),
    ('Gas', 'Gas'),
    ('Outros', 'Outros'),
]

tipo = [
    ('semanal', 'semanal'),
    ('mensal', 'mensal'),
]

tipo = [
    ('por semana', 'Por semana'),
    ('por mes', 'Por mês'),
]

class Usuario(models.Model):
    Nome = models.CharField(max_length=255, blank=True)
    Email = models.CharField(max_length=255, blank=True)
    Senha = models.CharField(max_length=255, blank=True)

class DBIngredientes(models.Model):
    Entrada_Ingrediente = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.Entrada_Ingrediente

class Ingredientes(models.Model):
    Ingrediente = models.ManyToManyField("DBIngredientes", related_name='+')
    Quantidade = models.CharField(max_length=255, blank=True)
    Tipo = models.CharField(max_length=255, choices=dose, blank=True)
    Receita = models.ManyToManyField("Receita", related_name='+')

    def __str__(self):
        return self.Ingrediente

class ListadeCompras(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User, blank=True, null=True)

    Ingrediente = models.ForeignKey("DBIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade = models.CharField(max_length=255, blank=True)
    Tipo = models.CharField(max_length=255, choices=dose, blank=True)

    Ingrediente_2 = models.ForeignKey("DBIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_2 = models.CharField(max_length=255, blank=True)
    Tipo_2 = models.CharField(max_length=255, choices=dose, blank=True)

    Ingrediente_3 = models.ForeignKey("DBIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_3 = models.CharField(max_length=255, blank=True)
    Tipo_3 = models.CharField(max_length=255, choices=dose, blank=True)

    Ingrediente_4 = models.ForeignKey("DBIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_4 = models.CharField(max_length=255, blank=True)
    Tipo_4 = models.CharField(max_length=255, choices=dose, blank=True)

    Ingrediente_5 = models.ForeignKey("DBIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_5 = models.CharField(max_length=255, blank=True)
    Tipo_5 = models.CharField(max_length=255, choices=dose, blank=True)

    Ingrediente_6 = models.ForeignKey("DBIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_6 = models.CharField(max_length=255, blank=True)
    Tipo_6 = models.CharField(max_length=255, choices=dose, blank=True)

    Ingrediente_7 = models.ForeignKey("DBIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_7 = models.CharField(max_length=255, blank=True)
    Tipo_7 = models.CharField(max_length=255, choices=dose, blank=True)

    Ingrediente_8 = models.ForeignKey("DBIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_8 = models.CharField(max_length=255, blank=True)
    Tipo_8 = models.CharField(max_length=255, choices=dose, blank=True)

    Ingrediente_9 = models.ForeignKey("DBIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_9 = models.CharField(max_length=255, blank=True)
    Tipo_9 = models.CharField(max_length=255, choices=dose, blank=True)

    Ingrediente_10 = models.ForeignKey("DBIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_10 = models.CharField(max_length=255, blank=True)
    Tipo_10 = models.CharField(max_length=255, choices=dose, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)

class MeusIngredientes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User, blank=True, null=True)

    Ingrediente = models.ForeignKey("DBIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Tamanho_Embalagem = models.CharField(max_length=255, blank=True)
    Tamanho_Embalagem_Tipo = models.CharField(max_length=255, choices=dose, blank=True)
    Valor_Pago = models.DecimalField(blank=True, decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.Ingrediente)

TEMPO_PREPARO = [
    ('segundo(s)', 'Segundo(s)'),
    ('minuto(s)', 'Minuto(s)'),
    ('hora(s)', 'Hora(s)'),
    ('dia(s)', 'Dia(s)'),
    ('semana(s)', 'Semana(s)'),
    ('mes(es)', 'Mes(es)'),
]

VENDA_MEDIA = [
    ('Por Hora', 'Por Hora'),
    ('Diariamente', 'Diariamente'),
    ('Semanalmente', 'Semanalmente'),
    ('Mensalmente', 'Mensalmente'),
    ('Anualmente', 'Anualmente'),
]

MATERIAL = [
    ('Sacola', 'Sacola'),
    ('Caixa', 'Caixa'),
    ('Isopor', 'Isopor'),
    ('Garrafa', 'Garrafa'),
    ('Pote', 'Pote'),
]

class Receita(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User, blank=True, null=True)
    
    Nome_da_Receita = models.CharField(max_length=255, blank=True)
    categoria = models.CharField(max_length=255, blank=True, choices=categorias)

    Ingrediente = models.ForeignKey("MeusIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade = models.CharField(max_length=255, blank=True)
    Tipo = models.CharField(max_length=255, choices=dose, blank=True)
    Custo_Ingrediente = models.CharField(max_length=50, blank=True, null=True)

    Ingrediente_2 = models.ForeignKey("MeusIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_2 = models.CharField(max_length=255, blank=True)
    Tipo_2 = models.CharField(max_length=255, choices=dose, blank=True)
    Custo_Ingrediente_2 = models.CharField(max_length=50, blank=True, null=True)

    Ingrediente_3 = models.ForeignKey("MeusIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_3 = models.CharField(max_length=255, blank=True)
    Tipo_3 = models.CharField(max_length=255, choices=dose, blank=True)
    Custo_Ingrediente_3 = models.CharField(max_length=50, blank=True, null=True)

    Ingrediente_4 = models.ForeignKey("MeusIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_4 = models.CharField(max_length=255, blank=True)
    Tipo_4 = models.CharField(max_length=255, choices=dose, blank=True)
    Custo_Ingrediente_4 = models.CharField(max_length=50, blank=True, null=True)

    Ingrediente_5 = models.ForeignKey("MeusIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_5 = models.CharField(max_length=255, blank=True)
    Tipo_5 = models.CharField(max_length=255, choices=dose, blank=True)
    Custo_Ingrediente_5 = models.CharField(max_length=50, blank=True, null=True)

    Ingrediente_6 = models.ForeignKey("MeusIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_6 = models.CharField(max_length=255, blank=True)
    Tipo_6 = models.CharField(max_length=255, choices=dose, blank=True)
    Custo_Ingrediente_6 = models.CharField(max_length=50, blank=True, null=True)

    Ingrediente_7 = models.ForeignKey("MeusIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_7 = models.CharField(max_length=255, blank=True)
    Tipo_7 = models.CharField(max_length=255, choices=dose, blank=True)
    Custo_Ingrediente_7 = models.CharField(max_length=50, blank=True, null=True)

    Ingrediente_8 = models.ForeignKey("MeusIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_8 = models.CharField(max_length=255, blank=True)
    Tipo_8 = models.CharField(max_length=255, choices=dose, blank=True)
    Custo_Ingrediente_8 = models.CharField(max_length=50, blank=True, null=True)

    Ingrediente_9 = models.ForeignKey("MeusIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_9 = models.CharField(max_length=255, blank=True)
    Tipo_9 = models.CharField(max_length=255, choices=dose, blank=True)
    Custo_Ingrediente_9 = models.CharField(max_length=50, blank=True, null=True)

    Ingrediente_10 = models.ForeignKey("MeusIngredientes", on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    Quantidade_10 = models.CharField(max_length=255, blank=True)
    Tipo_10 = models.CharField(max_length=255, choices=dose, blank=True)
    Custo_Ingrediente_10 = models.CharField(max_length=50, blank=True, null=True)

    Custo_Total_Ingredientes = models.CharField(max_length=50, blank=True, null=True)
    Porc_Custo_Total_Ingredientes = models.CharField(max_length=50, blank=True, null=True)

    Tempo_de_Preparo = models.CharField(max_length=50, blank=True, null=True)
    Tempo_de_Preparo_tipo = models.CharField(choices=TEMPO_PREPARO, max_length=50, blank=True, null=True)

    Forno = models.BooleanField(default=False)
    Forno_Tempo = models.CharField(max_length=50, blank=True, null=True)
    Forno_Tempo_Unidade = models.CharField(choices=TEMPO_PREPARO, max_length=50, blank=True, null=True)

    Fogao = models.BooleanField(default=False)
    Fogao_Tempo = models.CharField(max_length=50, blank=True, null=True)
    Fogao_Tempo_Unidade = models.CharField(choices=TEMPO_PREPARO, max_length=50, blank=True, null=True)

    Fritadeira = models.BooleanField(default=False)
    Fritadeira_Tempo = models.CharField(max_length=50, blank=True, null=True)
    Fritadeira_Tempo_Unidade = models.CharField(choices=TEMPO_PREPARO, max_length=50, blank=True, null=True)

    Microondas = models.BooleanField(default=False)
    Microondas_Tempo = models.CharField(max_length=50, blank=True, null=True)
    Microondas_Tempo_Unidade = models.CharField(choices=TEMPO_PREPARO, max_length=50, blank=True, null=True)

    Rendimento = models.CharField(max_length=50, blank=True, null=True)
    Rendimento_Unidade = models.CharField(choices=dose, max_length=50, blank=True, null=True)

    Valor_Venda = models.CharField(max_length=50, blank=True, null=True)

    Venda_Media = models.CharField(max_length=50, blank=True, null=True)
    Venda_Media_Unidade = models.CharField(choices=VENDA_MEDIA, max_length=50, blank=True, null=True)

    Total_Valor_Venda = models.CharField(max_length=50, blank=True, null=True)

    Nome_do_Material = models.CharField(max_length=50, blank=True, null=True)
    Tipo_Material = models.CharField(choices=MATERIAL, max_length=255, blank=True, null=True)
    Quantidade_Tipo_Material = models.CharField(max_length=50, blank=True, null=True)
    Unidades_Tipo_Material = models.CharField(choices=dose, max_length=50, blank=True, null=True)
    Valor_Material = models.CharField(max_length=50, blank=True, null=True)
    Quantas_Unidades = models.CharField(max_length=50, blank=True, null=True)
    Quantas_Unidades_Usa = models.CharField(choices=unidade, max_length=50, blank=True, null=True)

    Custo_Material = models.CharField(max_length=50, blank=True, null=True)
    Porc_Custo_Material = models.CharField(max_length=50, blank=True, null=True)

    Custo_Total_Geral = models.CharField(max_length=50, blank=True, null=True)
    Porc_Custo_Total_Geral = models.CharField(max_length=50, blank=True, null=True)

    Lucro_Bruto = models.CharField(max_length=50, blank=True, null=True)
    Porc_Lucro_Bruto = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.Nome_da_Receita

class Detalhes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User, blank=True, null=True)
    
    Tempo_de_Trabalho = models.CharField(max_length=255, blank=True)
    Tempo_de_Trabalho_Tipo = models.CharField(max_length=255, choices=tempo, blank=True)
    Forno = models.BooleanField(default=False)
    Fogão = models.BooleanField(default=False)
    Fritadeira = models.BooleanField(default=False)
    Microondas = models.BooleanField(default=False)
    Equipamento_Forno_Tempo = models.CharField(max_length=255, blank=True)
    Equipamento_Fogão_Tempo = models.CharField(max_length=255, blank=True)
    Equipamento_Fritadeira_Tempo = models.CharField(max_length=255, blank=True)
    Equipamento_Microondas_Tempo = models.CharField(max_length=255, blank=True)
    Equipamento_Forno_Tipo = models.CharField(max_length=255, choices=tempo, blank=True)
    Equipamento_Fogão_Tipo = models.CharField(max_length=255, choices=tempo, blank=True)
    Equipamento_Fritadeira_Tipo = models.CharField(max_length=255, choices=tempo, blank=True)
    Equipamento_Microondas_Tipo= models.CharField(max_length=255, choices=tempo, blank=True)
    Rendimento_n = models.CharField(max_length=255, blank=True)
    Rendimento_Tipo = models.CharField(max_length=255, blank=True)
    Valor_Venda = models.CharField(max_length=255, blank=True)
    Media_Unidade_Vendida = models.CharField(max_length=255, blank=True)
    Receita = models.ForeignKey("Receita", on_delete=models.CASCADE, related_name='+')

class Materiais(models.Model):
    Nome_Material = models.CharField(max_length=255, blank=True)
    Tipo = models.CharField(max_length=255, blank=True)
    Quantidade = models.CharField(max_length=255, blank=True)
    Medida_Unidades = models.CharField(max_length=255, blank=True)
    Unidade_por_Produto = models.CharField(max_length=255, blank=True)
    Unidade_por_Produto_Tipo = models.CharField(max_length=255, choices=unidade, blank=True)
    Receita = models.ForeignKey("Receita", on_delete=models.CASCADE, related_name='+')

class MeuNegocio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User, blank=True, null=True)
    
    Nome_do_Negocio = models.CharField(max_length=255, blank=True)
    Dono_do_Negocio = models.CharField(max_length=255, blank=True)
    Salario_Fixo = models.CharField(max_length=255, blank=True)
    Horas_por_Semana = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.pk)

class Funcionarios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User, blank=True, null=True)
    
    Nome_Funcionario = models.CharField(max_length=255, blank=True)
    Salario_Funcionario = models.CharField(max_length=255, blank=True)
    Tipo = models.CharField(max_length=255, choices=tipo, blank=True)

    Nome_Funcionario_2 = models.CharField(max_length=255, blank=True)
    Salario_Funcionario_2 = models.CharField(max_length=255, blank=True)
    Tipo_2 = models.CharField(max_length=255, choices=tipo, blank=True)

    Nome_Funcionario_3 = models.CharField(max_length=255, blank=True)
    Salario_Funcionario_3 = models.CharField(max_length=255, blank=True)
    Tipo_3 = models.CharField(max_length=255, choices=tipo, blank=True)

    Nome_Funcionario_4 = models.CharField(max_length=255, blank=True)
    Salario_Funcionario_4 = models.CharField(max_length=255, blank=True)
    Tipo_4 = models.CharField(max_length=255, choices=tipo, blank=True)

    Nome_Funcionario_5 = models.CharField(max_length=255, blank=True)
    Salario_Funcionario_5 = models.CharField(max_length=255, blank=True)
    Tipo_5 = models.CharField(max_length=255, choices=tipo, blank=True)

    def __str__(self):
        return str(self.pk)    

class Entregas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User, blank=True, null=True)
    
    Entregamos = models.BooleanField(default=False)
    Contratamos = models.BooleanField(default=False)
    Cliente_Busca = models.BooleanField(default=False)

    Tempo_Medio_Entrega = models.CharField(max_length=255, blank=True)
    Tempo_Medio_Entrega_Tipo = models.CharField(max_length=255, choices=tipo, blank=True)
    Valor_Medio_Entrega = models.CharField(max_length=255, blank=True)
    Valor_Medio_Entrega_Tipo = models.CharField(max_length=255, choices=tipo, blank=True)

    Valor_Medio_Contrata = models.CharField(max_length=255, blank=True)
    Tempo_Medio_Contrata_Tipo = models.CharField(max_length=255, choices=tipo, blank=True)

class OutrasDespesas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User, blank=True, null=True)
    
    Combustivel = models.BooleanField(default=False)
    Divulgacao = models.BooleanField(default=False)
    Taxas_Impostos = models.BooleanField(default=False)
    Telefone = models.BooleanField(default=False)
    Internet = models.BooleanField(default=False)
    Agua = models.BooleanField(default=False)
    Luz = models.BooleanField(default=False)
    Gas = models.BooleanField(default=False)
    Outro = models.BooleanField(default=False)
    Combustivel_Valor = models.CharField(max_length=255, blank=True)
    Combustivel_Tipo = models.CharField(max_length=255, choices=tipo, blank=True)
    Divulgacao_Valor = models.CharField(max_length=255, blank=True)
    Divulgacao_Tipo = models.CharField(max_length=255, choices=tipo, blank=True)
    Impostos_Valor = models.CharField(max_length=255, blank=True)
    Impostos_Tipo = models.CharField(max_length=255, choices=tipo, blank=True)
    Telefone_Valor = models.CharField(max_length=255, blank=True)
    Telefone_Tipo = models.CharField(max_length=255, choices=tipo, blank=True)
    Internet_Valor = models.CharField(max_length=255, blank=True)
    Internet_Tipo = models.CharField(max_length=255, choices=tipo, blank=True)
    Agua_Valor = models.CharField(max_length=255, blank=True)
    Agua_Tipo = models.CharField(max_length=255, choices=tipo, blank=True)
    Luz_Valor = models.CharField(max_length=255, blank=True)
    Luz_Tipo = models.CharField(max_length=255, choices=tipo, blank=True)
    Gas_Valor = models.CharField(max_length=255, blank=True)
    Gas_Tipo = models.CharField(max_length=255, choices=tipo, blank=True)
    Outro_Descricao = models.CharField(max_length=255, blank=True)
    Outro_Valor = models.CharField(max_length=255, blank=True)
    Outro_Tipo = models.CharField(max_length=255, choices=tipo, blank=True)