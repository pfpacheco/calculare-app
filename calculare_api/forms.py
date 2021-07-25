from django import forms


from .models import *

TEMPO_PREPARO = [
    ('', '----------'),
    ('segundo(s)', 'Segundo(s)'),
    ('minuto(s)', 'Minuto(s)'),
    ('hora(s)', 'Hora(s)'),
    ('dia(s)', 'Dia(s)'),
    ('semana(s)', 'Semana(s)'),
    ('mes(es)', 'Mes(es)'),
]

dose = [
    ('', '----------'),
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
VENDA_MEDIA = [
    ('', '----------'),
    ('Por Hora', 'Por Hora'),
    ('Diariamente', 'Diariamente'),
    ('Semanalmente', 'Semanalmente'),
    ('Mensalmente', 'Mensalmente'),
    ('Anualmente', 'Anualmente'),
]

class ReceitaForm(forms.ModelForm):
    Forno_Tempo = forms.CharField(label="", required=False)
    Forno_Tempo_Unidade = forms.ChoiceField(label="", choices=TEMPO_PREPARO, required=False)
    Fogao_Tempo = forms.CharField(label="", required=False)
    Fogao_Tempo_Unidade = forms.ChoiceField(label="", choices=TEMPO_PREPARO, required=False)
    Fritadeira_Tempo = forms.CharField(label="", required=False)
    Fritadeira_Tempo_Unidade = forms.ChoiceField(label="", choices=TEMPO_PREPARO, required=False)
    Microondas_Tempo = forms.CharField(label="", required=False)
    Microondas_Tempo_Unidade = forms.ChoiceField(label="", choices=TEMPO_PREPARO, required=False)
    Rendimento = forms.CharField(label="", required=False)
    Rendimento_Unidade = forms.ChoiceField(label="", choices=dose, required=False)
    Valor_Venda = forms.CharField(label="", required=False)
    Venda_Media = forms.CharField(label="", required=False)
    Venda_Media_Unidade = forms.ChoiceField(label="", choices=VENDA_MEDIA, required=False)
    Nome_do_Material = forms.CharField(label="", required=False)
    Tipo_Material = forms.ChoiceField(label="", choices=MATERIAL, required=False)
    Quantidade_Tipo_Material = forms.CharField(label="", required=False)
    Unidades_Tipo_Material = forms.ChoiceField(label="", choices=dose, required=False)
    Valor_Material = forms.CharField(label="", required=False)
    Quantas_Unidades = forms.CharField(label="", required=False)
    Quantas_Unidades_Usa = forms.ChoiceField(label="", choices=unidade, required=False)

    class Meta:
        model = Receita
        fields = '__all__' 

        widgets = {
            'categoria': forms.RadioSelect(),
            'Nome_da_Receita': forms.TextInput(attrs={'placeholder': 'Digite o nome da sua receita'}),
        }
        

class DBIngredientesForm(forms.ModelForm):
    
    class Meta:
        model = DBIngredientes
        fields = '__all__' 

class IngredientesForm(forms.ModelForm):
    
    class Meta:
        model = Ingredientes
        fields = '__all__' 

class MeuNegocioForm(forms.ModelForm):
    Nome_do_Negocio = forms.CharField(label="Qual o nome do negócio?", required=False)
    Dono_do_Negocio = forms.CharField(label="Qual o nome do dono do negócio?", required=False)
    Salario_Fixo = forms.CharField(label="Se você retira algum salário fixo desse negócio, digite abaixo o valor:", required=False)
    Horas_por_Semana = forms.CharField(label="Quantas horas por semana em média você trabalha?", required=False)

    class Meta:
        model = MeuNegocio
        fields = '__all__' 

tipo = [
    ('', '----------'),
    ('por semana', 'Por semana'),
    ('por mes', 'Por mês'),
]

class FuncionariosForm(forms.ModelForm):
    Nome_Funcionario = forms.CharField(label="Qual o nome do seu funcionário?", required=False)
    Salario_Funcionario = forms.CharField(label="", required=False)
    Tipo = forms.ChoiceField(label="", choices=tipo, required=False)

    Nome_Funcionario_2 = forms.CharField(label="Qual o nome do seu funcionário?", required=False)
    Salario_Funcionario_2 = forms.CharField(label="", required=False)
    Tipo_2 = forms.ChoiceField(label="", choices=tipo, required=False)

    Nome_Funcionario_3 = forms.CharField(label="Qual o nome do seu funcionário?", required=False)
    Salario_Funcionario_3 = forms.CharField(label="", required=False)
    Tipo_3 = forms.ChoiceField(label="", choices=tipo, required=False)

    Nome_Funcionario_4 = forms.CharField(label="Qual o nome do seu funcionário?", required=False)
    Salario_Funcionario_4 = forms.CharField(label="", required=False)
    Tipo_4 = forms.ChoiceField(label="", choices=tipo, required=False)

    Nome_Funcionario_5 = forms.CharField(label="Qual o nome do seu funcionário?", required=False)
    Salario_Funcionario_5 = forms.CharField(label="", required=False)
    Tipo_5 = forms.ChoiceField(label="", choices=tipo, required=False)
    
    class Meta:
        model = Funcionarios
        fields = '__all__' 

class EntregasForm(forms.ModelForm):
    Tempo_Medio_Entrega = forms.CharField(label="", required=False)
    Tempo_Medio_Entrega_Tipo = forms.ChoiceField(label="", choices=tipo, required=False)
    Valor_Medio_Entrega = forms.CharField(label="", required=False)
    Valor_Medio_Entrega_Tipo = forms.ChoiceField(label="", choices=tipo, required=False)
    Valor_Medio_Contrata = forms.CharField(label="", required=False)
    Tempo_Medio_Contrata_Tipo = forms.ChoiceField(label="", choices=tipo, required=False)

    class Meta:
        model = Entregas
        fields = '__all__' 

class OutrasDespesasForm(forms.ModelForm):
    Combustivel_Valor = forms.CharField(label="", required=False)
    Combustivel_Tipo = forms.ChoiceField(label="", choices=tipo, required=False)
    Divulgacao_Valor = forms.CharField(label="", required=False)
    Divulgacao_Tipo = forms.ChoiceField(label="", choices=tipo, required=False)
    Impostos_Valor = forms.CharField(label="", required=False)
    Impostos_Tipo = forms.ChoiceField(label="", choices=tipo, required=False)
    Telefone_Valor = forms.CharField(label="", required=False)
    Telefone_Tipo = forms.ChoiceField(label="", choices=tipo, required=False)
    Internet_Valor = forms.CharField(label="", required=False)
    Internet_Tipo = forms.ChoiceField(label="", choices=tipo, required=False)
    Agua_Valor = forms.CharField(label="", required=False)
    Agua_Tipo = forms.ChoiceField(label="", choices=tipo, required=False)
    Luz_Valor = forms.CharField(label="", required=False)
    Luz_Tipo = forms.ChoiceField(label="", choices=tipo, required=False)
    Gas_Valor = forms.CharField(label="", required=False)
    Gas_Tipo = forms.ChoiceField(label="", choices=tipo, required=False)
    Outro_Valor = forms.CharField(label="", required=False)
    Outro_Tipo = forms.ChoiceField(label="", choices=tipo, required=False)
    Outro_Descricao= forms.CharField(label="Insira a descrição", required=False)

    class Meta:
        model = OutrasDespesas
        fields = '__all__' 

class MeusIngredientesForm(forms.ModelForm):
    Tamanho_Embalagem = forms.CharField(label="", required=False)
    Tamanho_Embalagem_Tipo = forms.ChoiceField(label="", choices=dose, required=False)
    Valor_Pago = forms.CharField(label="", required=False)

    class Meta:
        model = MeusIngredientes
        fields = '__all__' 

class ListadeComprasForm(forms.ModelForm):
    Quantidade = forms.CharField(label="", required=False)
    Tipo = forms.ChoiceField(label="", choices=dose, required=False)

    Quantidade_2 = forms.CharField(label="", required=False)
    Tipo_2 = forms.ChoiceField(label="", choices=dose, required=False)

    Quantidade_3 = forms.CharField(label="", required=False)
    Tipo_3 = forms.ChoiceField(label="", choices=dose, required=False)

    Quantidade_4 = forms.CharField(label="", required=False)
    Tipo_4 = forms.ChoiceField(label="", choices=dose, required=False)

    Quantidade_5 = forms.CharField(label="", required=False)
    Tipo_5 = forms.ChoiceField(label="", choices=dose, required=False)

    Quantidade_6 = forms.CharField(label="", required=False)
    Tipo_6 = forms.ChoiceField(label="", choices=dose, required=False)

    Quantidade_7 = forms.CharField(label="", required=False)
    Tipo_7 = forms.ChoiceField(label="", choices=dose, required=False)

    Quantidade_8 = forms.CharField(label="", required=False)
    Tipo_8 = forms.ChoiceField(label="", choices=dose, required=False)

    Quantidade_9 = forms.CharField(label="", required=False)
    Tipo_9 = forms.ChoiceField(label="", choices=dose, required=False)

    Quantidade_10 = forms.CharField(label="", required=False)
    Tipo_10 = forms.ChoiceField(label="", choices=dose, required=False)

    class Meta:
        model = ListadeCompras
        fields = '__all__' 