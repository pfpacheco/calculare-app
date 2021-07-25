from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
import requests
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.http import Http404
from django.core.paginator import Paginator
import datetime

from .forms import *
from .models import *
from .filters import *

from users.models import *
from users.forms import *

def splash(request):
    return render(request, 'front/splash.html')

def explicativa(request):
    return render(request, 'front/tela_explicativa_1.html')

def explicativatwo(request):
    return render(request, 'front/tela_explicativa_2.html')

def explicativathree(request):
    return render(request, 'front/tela_explicativa_3.html')

@login_required
def home(request):
    Total_Lucro = Receita.objects.all()
    Total_Vendas = Receita.objects.all()
    Total_Despesas = Receita.objects.all()

    url_avatar = 'https://calculareapi.herokuapp.com/api/usuario/' + str(request.user.id)
    response_avatar = requests.get(url_avatar)
    avatar = json.loads(response_avatar.text)
    avatar = avatar

    try:
        Total_Lucro = Receita.objects.all().aggregate(Total_Lucro=Sum('Lucro_Bruto'))
        Total_Vendas = Receita.objects.all().aggregate(Total_Valor_Venda=Sum('Total_Valor_Venda'))
        Total_Despesas = Receita.objects.all().aggregate(Custo_Total_Geral=Sum('Custo_Total_Geral'))

        if Total_Lucro['Total_Lucro'] is None:
            Total_Lucro['Total_Lucro'] = 0

        if Total_Vendas['Total_Valor_Venda'] is None:
            Total_Vendas['Total_Valor_Venda'] = 0

        if Total_Despesas['Custo_Total_Geral'] is None:
            Total_Despesas['Custo_Total_Geral'] = 0

        return render(request, 'front/home.html', {
        'Total_Lucro': Total_Lucro['Total_Lucro'],
        'Total_Vendas': Total_Vendas['Total_Valor_Venda'],
        'Total_Despesas': Total_Despesas['Custo_Total_Geral'],
        'avatar': avatar
    })
    except:
        url_avatar = 'https://calculareapi.herokuapp.com/api/usuario/' + str(request.user.id)
        response_avatar = requests.get(url_avatar)
        avatar = json.loads(response_avatar.text)
        avatar = avatar
        
        return render(request, 'front/home.html', {'avatar': avatar})

@login_required
def resultados(request):
    Total_Lucro = Receita.objects.all()
    Total_Vendas = Receita.objects.all()
    Total_Despesas = Receita.objects.all()
    Material = Receita.objects.all()
    Mao_de_Obra = Funcionarios.objects.all()
    Mao_de_Obra_2 = Funcionarios.objects.all()
    Mao_de_Obra_3 = Funcionarios.objects.all()
    Mao_de_Obra_4 = Funcionarios.objects.all()
    Mao_de_Obra_5 = Funcionarios.objects.all()
    Valor_Medio_Entrega = Entregas.objects.all()
    Valor_Medio_Contrata = Entregas.objects.all()
    Combustivel = OutrasDespesas.objects.all()
    Divulgacao = OutrasDespesas.objects.all()
    Taxas_Impostos = OutrasDespesas.objects.all()
    Telefone = OutrasDespesas.objects.all()
    Internet = OutrasDespesas.objects.all()
    Agua = OutrasDespesas.objects.all()
    Luz = OutrasDespesas.objects.all()
    Gas = OutrasDespesas.objects.all()
    Outro = OutrasDespesas.objects.all()

    Meu_Negocio = MeuNegocio.objects.all()
    for dado in Meu_Negocio:
        Salario_Fixo = dado.Salario_Fixo

    try:
        Total_Lucro = Receita.objects.all().aggregate(Total_Lucro=Sum('Lucro_Bruto'))
        Total_Vendas = Receita.objects.all().aggregate(Total_Valor_Venda=Sum('Total_Valor_Venda'))
        Total_Despesas = Receita.objects.all().aggregate(Custo_Total_Geral=Sum('Custo_Total_Geral'))
        Material = Receita.objects.all().aggregate(Custo_Material=Sum('Custo_Material'))
        Mao_de_Obra = Funcionarios.objects.all().aggregate(Salario_Funcionario=Sum('Salario_Funcionario'))
        Mao_de_Obra_2 = Funcionarios.objects.all().aggregate(Salario_Funcionario_2=Sum('Salario_Funcionario_2'))
        Mao_de_Obra_3 = Funcionarios.objects.all().aggregate(Salario_Funcionario_3=Sum('Salario_Funcionario_3'))
        Mao_de_Obra_4 = Funcionarios.objects.all().aggregate(Salario_Funcionario_4=Sum('Salario_Funcionario_4'))
        Mao_de_Obra_5 = Funcionarios.objects.all().aggregate(Salario_Funcionario_5=Sum('Salario_Funcionario_5'))
        Valor_Medio_Entrega = Entregas.objects.all().aggregate(Valor_Medio_Entrega=Sum('Valor_Medio_Entrega'))
        Valor_Medio_Contrata = Entregas.objects.all().aggregate(Valor_Medio_Contrata=Sum('Valor_Medio_Contrata'))

        Combustivel = OutrasDespesas.objects.all().aggregate(Combustivel=Sum('Combustivel_Valor'))
        Divulgacao = OutrasDespesas.objects.all().aggregate(Divulgacao=Sum('Divulgacao_Valor'))
        Taxas_Impostos = OutrasDespesas.objects.all().aggregate(Taxas_Impostos=Sum('Impostos_Valor'))
        Telefone = OutrasDespesas.objects.all().aggregate(Telefone=Sum('Telefone_Valor'))
        Internet = OutrasDespesas.objects.all().aggregate(Internet=Sum('Internet_Valor'))
        Agua = OutrasDespesas.objects.all().aggregate(Agua=Sum('Agua_Valor'))
        Luz = OutrasDespesas.objects.all().aggregate(Luz=Sum('Luz_Valor'))
        Gas = OutrasDespesas.objects.all().aggregate(Gas=Sum('Gas_Valor'))
        Outro = OutrasDespesas.objects.all().aggregate(Outro=Sum('Outro_Valor'))

        if Material['Custo_Material'] is None:
            Material['Custo_Material'] = 0

        if Mao_de_Obra['Salario_Funcionario'] is None:
            Mao_de_Obra['Salario_Funcionario'] = 0

        if Mao_de_Obra_2['Salario_Funcionario_2'] is None:
            Mao_de_Obra_2['Salario_Funcionario_2'] = 0


        if Mao_de_Obra_3['Salario_Funcionario_3'] is None:
            Mao_de_Obra_3['Salario_Funcionario_3'] = 0

        if Mao_de_Obra_4['Salario_Funcionario_4'] is None:
            Mao_de_Obra_4['Salario_Funcionario_4'] = 0

        if Mao_de_Obra_5['Salario_Funcionario_5'] is None:
            Mao_de_Obra_5['Salario_Funcionario_5'] = 0

        Total_Mao_de_Obra = Mao_de_Obra['Salario_Funcionario'] + Mao_de_Obra_2['Salario_Funcionario_2'] + Mao_de_Obra_3['Salario_Funcionario_3'] + Mao_de_Obra_4['Salario_Funcionario_4'] + Mao_de_Obra_5['Salario_Funcionario_5']

        if Total_Lucro['Total_Lucro'] is None:
            Total_Lucro['Total_Lucro'] = 0

        if Total_Vendas['Total_Valor_Venda'] is None:
            Total_Vendas['Total_Valor_Venda'] = 0

        if Total_Despesas['Custo_Total_Geral'] is None:
            Total_Despesas['Custo_Total_Geral'] = 0

        Total_Custo_Produtos = Total_Despesas['Custo_Total_Geral'] + Total_Mao_de_Obra

        Total_Lucro = Total_Lucro['Total_Lucro'] - Total_Custo_Produtos

        if Valor_Medio_Entrega['Valor_Medio_Entrega'] is None:
            Valor_Medio_Entrega['Valor_Medio_Entrega'] = 0

        if Valor_Medio_Contrata['Valor_Medio_Contrata'] is None:
            Valor_Medio_Contrata['Valor_Medio_Contrata'] = 0

        if Combustivel['Combustivel'] is None:
            Combustivel['Combustivel'] = 0

        if Divulgacao['Divulgacao'] is None:
            Divulgacao['Divulgacao'] = 0

        if Taxas_Impostos['Taxas_Impostos'] is None:
            Taxas_Impostos['Taxas_Impostos'] = 0

        if Telefone['Telefone'] is None:
            Telefone['Telefone'] = 0

        if Internet['Internet'] is None:
            Internet['Internet'] = 0

        if Agua['Agua'] is None:
            Agua['Agua'] = 0

        if Luz['Luz'] is None:
            Luz['Luz'] = 0

        if Gas['Gas'] is None:
            Gas['Gas'] = 0

        if Outro['Outro'] is None:
            Outro['Outro'] = 0

        Total_Entregas = Valor_Medio_Entrega['Valor_Medio_Entrega'] + Valor_Medio_Contrata['Valor_Medio_Contrata']
        Total_Combustivel = Combustivel['Combustivel']
        Total_Divulgacao = Divulgacao['Divulgacao']
        Total_Taxas_Impostos = Taxas_Impostos['Taxas_Impostos']
        Total_Telefone = Telefone['Telefone'] 
        Total_Internet = Internet['Internet']
        Total_Agua = Agua['Agua']
        Total_Luz = Luz['Luz']
        Total_Gas = Gas['Gas']
        Total_Outro = Outro['Outro']

        Total_Outras_Despesas = Combustivel['Combustivel'] + Divulgacao['Divulgacao'] + Taxas_Impostos['Taxas_Impostos'] + Telefone['Telefone'] + Internet['Internet'] + Agua['Agua'] + Luz['Luz'] + Gas['Gas'] + Outro['Outro']
        Total_Despesas = Total_Outras_Despesas + Total_Entregas

        Lucro_Liquido = Total_Lucro - Total_Despesas

        # Ganho_Mes = float(Lucro_Liquido) + float(Salario_Fixo)

        Porc_Custo_Produtos = int((round(Total_Custo_Produtos/Total_Vendas['Total_Valor_Venda'], 2)) * 100)

        Porc_Material = int((round(Material['Custo_Material']/Total_Custo_Produtos, 2)) * 100)
        Porc_Mao_de_Obra = int((round(Total_Mao_de_Obra/Total_Custo_Produtos, 2)) * 100)

        Porc_Total_Despesas = int((round(Total_Despesas/Total_Vendas['Total_Valor_Venda'], 2)) * 100)
        Porc_Lucro_Liquido = int((round(Lucro_Liquido/Total_Vendas['Total_Valor_Venda'], 2)) * 100)
        Porc_Lucro_Bruto = int((round(Total_Lucro/Total_Vendas['Total_Valor_Venda'], 2)) * 100)

        # Porc_Ganho_Mes = round(Ganho_Mes/Total_Vendas['Total_Valor_Venda'], 2)
        Porc_Entregas = int((round(Total_Entregas/Total_Despesas, 2)) * 100)
        Porc_Combustivel = int((round(Total_Combustivel/Total_Despesas, 2)) * 100)
        Porc_Divulgacao = int((round(Total_Divulgacao/Total_Despesas, 2)) * 100)
        Porc_Taxas_Impostos = int((round(Total_Taxas_Impostos/Total_Despesas, 2)) * 100)
        Porc_Telefone = int((round(Total_Telefone/Total_Despesas, 2)) * 100)
        Porc_Internet = int((round(Total_Internet/Total_Despesas, 2)) * 100)
        Porc_Agua = int((round(Total_Agua/Total_Despesas, 2)) * 100)
        Porc_Luz = int((round(Total_Luz/Total_Despesas, 2)) * 100)
        Porc_Gas = int((round(Total_Gas/Total_Despesas, 2)) * 100)
        Porc_Outro = int((round(Total_Outro/Total_Despesas, 2)) * 100)

        return render(request, 'front/resultados.html', {
        'Total_Lucro': Total_Lucro,
        'Porc_Lucro_Bruto': Porc_Lucro_Bruto,
        'Total_Vendas': Total_Vendas['Total_Valor_Venda'],
        'Total_Despesas': Total_Despesas,
        'Porc_Custo_Produtos': Porc_Custo_Produtos,
        'Porc_Total_Despesas': Porc_Total_Despesas,
        'Salario_Fixo': Salario_Fixo,
        'Material': Material['Custo_Material'],
        'Porc_Material': Porc_Material,
        'Total_Mao_de_Obra': Total_Mao_de_Obra,
        'Porc_Mao_de_Obra': Porc_Mao_de_Obra,
        'Total_Entregas': Total_Entregas,
        'Total_Combustivel': Total_Combustivel,
        'Total_Divulgacao': Total_Divulgacao,
        'Total_Taxas_Impostos': Total_Taxas_Impostos,
        'Total_Telefone': Total_Telefone,
        'Total_Internet': Total_Internet,
        'Total_Agua': Total_Agua,
        'Total_Luz': Total_Luz,
        'Total_Gas': Total_Gas,
        'Total_Outro': Total_Outro,
        'Total_Custo_Produtos': Total_Custo_Produtos,
        'Lucro_Liquido': Lucro_Liquido,
        'Porc_Lucro_Liquido': Porc_Lucro_Liquido,
        # 'Ganho_Mes': Ganho_Mes,
        # 'Porc_Ganho_Mes': Porc_Ganho_Mes,
        'Porc_Combustivel': Porc_Combustivel,
        'Porc_Divulgacao': Porc_Divulgacao,
        'Porc_Taxas_Impostos': Porc_Taxas_Impostos,
        'Porc_Telefone': Porc_Telefone,
        'Porc_Internet': Porc_Internet,
        'Porc_Agua': Porc_Agua,
        'Porc_Luz': Porc_Luz,
        'Porc_Gas': Porc_Gas,
        'Porc_Outro': Porc_Outro,
        'Porc_Entregas': Porc_Entregas,
    })
    except:
        pass
    return render(request, 'front/resultados.html')

@login_required
def resultados_info(request):
    return render(request, 'front/resultados_info.html')

@login_required
def receita(request):

    form = ReceitaForm
    if request.method == 'POST':
        form = ReceitaForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
        return redirect('ingredientes')
    
    return render(request, 'front/receita.html', {'form': form})

@login_required
def ingrediente(request):

    form = IngredientesForm()
    if request.method == 'POST':
        form = IngredientesForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
        return redirect('sucesso')
    
    return render(request, 'front/ingredientes.html', {'form': form})

@login_required
def edit_ingrediente(request, id):
    Id = get_object_or_404(Ingredientes, pk=id)
    form = IngredientesForm(instance=Id)

    if(request.method == 'POST'):
        form = IngredientesForm(request.POST, instance=Id)

        if(form.is_valid()):
            Id = form.save(commit=False)
            Id.user = request.user 
            Id.save()
        else:
            return render(request, 'front/edit_ingredientes.html', {'form': form, 'Id': Id})
    else:
        return render(request, 'front/edit_ingredientes.html', {'form': form, 'Id': Id})

@login_required
def configuracoes(request):
    return render(request, 'front/configuracoes.html')

@login_required
def dadospessoais(request, id):
    id_ = get_object_or_404(User, pk=id)
    
    form = UserChangeForm(instance=id_)

    usuario = User.objects.filter(pk=id)

    url_avatar = 'https://calculareapi.herokuapp.com/api/usuario/' + str(id)
    response_avatar = requests.get(url_avatar)
    avatar = json.loads(response_avatar.text)
    avatar = avatar

    if request.method == 'POST':
        form = UserChangeForm(request.POST, request.FILES, instance=id_)
        if form.is_valid():
            form.save()
            return redirect('/home')
    context = {
        'form':form,
        'usuario': usuario,
        'avatar': avatar,
    }
    #return redirect('/')

    return render(request, 'front/dadospessoais.html', context,)

@login_required
def sobrenos(request):
    return render(request, 'front/sobrenos.html')

@login_required
def suporte(request):
    return render(request, 'front/suporte.html')

@login_required
def minhalistadecompras(request):
    listas = ListadeCompras.objects.all().count()
    if listas <= 0:
        return render(request, 'front/minhalistadecompras.html')
    else:
        listas = ListadeCompras.objects.all()
        return render(request, 'front/minhaslistasdecompras.html', {'listas': listas})

@login_required
def delete_minhalistadecompras(request, id):
    Id = get_object_or_404(ListadeCompras, pk=id)
    Id.delete()

    return redirect('/minhalistadecompras')

@login_required
def meusnegocios(request):
    return render(request, 'front/meunegocio.html')

@login_required
def meunegocio(request):
    meunegocio = MeuNegocio.objects.all().count()
    if meunegocio <= 0:
        return render(request, 'front/meunegocio1.html')
    elif meunegocio >= 1:
        meunegocio = MeuNegocio.objects.all()
        return render(request, 'front/meunegociodetalhes.html', {'meunegocio': meunegocio})
    else:
        return render(request, 'front/meunegocio.html')

def edit_meunegocio(request, id):
    id_ = get_object_or_404(MeuNegocio, pk=id)

    form = MeuNegocioForm(instance=id_)
    if request.method == 'POST':
        form = MeuNegocioForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            negocios = MeuNegocio.objects.latest('id')
        return redirect('/cadastrarinformacoes2/'+str(negocios.id)+'')
        
    return render(request, 'front/edit_meunegocio.html', {'form': form})

@login_required
def add_receita(request):
    receitas = Receita.objects.all().count()

    if receitas <= 0:
        form = ReceitaForm()
        if request.method == 'POST':
            form = ReceitaForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user 
                form.save()
                receitas = Receita.objects.latest('id')
            return redirect('/add_receita1/'+str(receitas.id)+'')
        
        return render(request, 'front/add_receita.html', {'form': form})
    else:
        receitas = Receita.objects.all()

        filtro = Receita.objects.all()
        myFilter = ReceitaFilter(request.GET, queryset=filtro)
        receitas = myFilter.qs

        acompanhamentos = Receita.objects.filter(categoria='Acompanhamentos').count()
        bolos = Receita.objects.filter(categoria='Bolos').count()
        bebidas = Receita.objects.filter(categoria='Bebidas').count()
        caldos_molhos = Receita.objects.filter(categoria='Caldos e Molhos').count()
        doces_sobremesas = Receita.objects.filter(categoria='Doces e Sobremesas').count()
        petisco = Receita.objects.filter(categoria='Petisco').count()
        pratos = Receita.objects.filter(categoria='Pratos').count()
        salgados = Receita.objects.filter(categoria='Salgados').count()
        outra = Receita.objects.filter(categoria='Outra Categoria').count()

        return render(request, 'front/receitadetalhes.html', {'receitas': receitas, 'acompanhamentos': acompanhamentos, 'bolos': bolos, 'bebidas': bebidas,
        'caldos_molhos': caldos_molhos, 'doces_sobremesas': doces_sobremesas, 'petisco': petisco, 'pratos': pratos, 'salgados': salgados, 'outra': outra,
        'myFilter': myFilter})

@login_required
def detalhes_receita(request, id):
    receitas = Receita.objects.all().count()

    if receitas <= 0:
        form = ReceitaForm()
        if request.method == 'POST':
            form = ReceitaForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user 
                form.save()
                receitas = Receita.objects.latest('id')
            return redirect('/add_receita1/'+str(receitas.id)+'')
        
        return render(request, 'front/add_receita.html', {'form': form})
    else:
        receitas = Receita.objects.all()

        filtro = Receita.objects.all()
        myFilter = ReceitaFilter(request.GET, queryset=filtro)
        receitas = myFilter.qs

        acompanhamentos = Receita.objects.filter(categoria='Acompanhamentos').count()
        bolos = Receita.objects.filter(categoria='Bolos').count()
        bebidas = Receita.objects.filter(categoria='Bebidas').count()
        caldos_molhos = Receita.objects.filter(categoria='Caldos e Molhos').count()
        doces_sobremesas = Receita.objects.filter(categoria='Doces e Sobremesas').count()
        petisco = Receita.objects.filter(categoria='Petisco').count()
        pratos = Receita.objects.filter(categoria='Pratos').count()
        salgados = Receita.objects.filter(categoria='Salgados').count()
        outra = Receita.objects.filter(categoria='Outra Categoria').count()

        return render(request, 'front/detalhes_receita.html', {'receitas': receitas, 'acompanhamentos': acompanhamentos, 'bolos': bolos, 'bebidas': bebidas,
        'caldos_molhos': caldos_molhos, 'doces_sobremesas': doces_sobremesas, 'petisco': petisco, 'pratos': pratos, 'salgados': salgados, 'outra': outra,
        'myFilter': myFilter})

def add_receita_dps(request):
    receitas = Receita.objects.all().count()

    form = ReceitaForm()
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.latest('id')
        return redirect('/add_receita1/'+str(receitas.id)+'')
    
    return render(request, 'front/add_receita_dps.html', {'form': form})

@login_required
def edit_receita_dps(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)
        return redirect('/edit_receita1/'+str(receitas.id)+'')
    
    return render(request, 'front/edit_receita_dps.html', {'form': form})

@login_required
def add_receita1(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    # voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.latest('id')         
            # if voltar == "Sim":
            #     return redirect('/add_receita2/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/add_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/add_receita2/'+str(receitas.id)+'')

    return render(request, 'front/add_receita1.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def add_receita2(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.latest('id')

            if voltar == "Sim":
                return redirect('/add_receita1/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/add_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/add_receita3/'+str(receitas.id)+'')

    return render(request, 'front/add_receita2.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def add_receita3(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.latest('id')

            if voltar == "Sim":
                return redirect('/add_receita2/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/add_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/add_receita4/'+str(receitas.id)+'')

    return render(request, 'front/add_receita3.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def add_receita4(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.latest('id')

            if voltar == "Sim":
                return redirect('/add_receita3/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/add_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/add_receita5/'+str(receitas.id)+'')

    return render(request, 'front/add_receita4.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def add_receita5(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.latest('id')

            if voltar == "Sim":
                return redirect('/add_receita4/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/add_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/add_receita6/'+str(receitas.id)+'')

    return render(request, 'front/add_receita5.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def add_receita6(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.latest('id')

            if voltar == "Sim":
                return redirect('/add_receita5/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/add_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/add_receita7/'+str(receitas.id)+'')

    return render(request, 'front/add_receita6.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def add_receita7(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.latest('id')

            if voltar == "Sim":
                return redirect('/add_receita6/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/add_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/add_receita8/'+str(receitas.id)+'')

    return render(request, 'front/add_receita7.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def add_receita8(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.latest('id')

            if voltar == "Sim":
                return redirect('/add_receita7/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/add_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/add_receita9/'+str(receitas.id)+'')

    return render(request, 'front/add_receita8.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def add_receita9(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.latest('id')

            if voltar == "Sim":
                return redirect('/add_receita8/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/add_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/add_receita10/'+str(receitas.id)+'')

    return render(request, 'front/add_receita9.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def add_receita10(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.latest('id')

            if voltar == "Sim":
                return redirect('/add_receita9/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/add_receitadetalhes/'+str(receitas.id)+'')

    return render(request, 'front/add_receita10.html', {'form': form, 'ingredientes': ingredientes})
    

@login_required
def edit_receita1(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    # voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)

            # if voltar == "Sim":
            #     return redirect('/edit_receita2/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/edit_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/edit_receita2/'+str(receitas.id)+'')

    return render(request, 'front/edit_receita1.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def edit_receita2(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)

            if voltar == "Sim":
                return redirect('/edit_receita1/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/edit_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/edit_receita3/'+str(receitas.id)+'')

    return render(request, 'front/edit_receita2.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def edit_receita3(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)

            if voltar == "Sim":
                return redirect('/edit_receita2/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/edit_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/edit_receita4/'+str(receitas.id)+'')

    return render(request, 'front/edit_receita3.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def edit_receita4(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)

            if voltar == "Sim":
                return redirect('/edit_receita3/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/edit_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/edit_receita5/'+str(receitas.id)+'')

    return render(request, 'front/edit_receita4.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def edit_receita5(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)

            if voltar == "Sim":
                return redirect('/edit_receita4/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/edit_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/edit_receita6/'+str(receitas.id)+'')

    return render(request, 'front/edit_receita5.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def edit_receita6(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)

            if voltar == "Sim":
                return redirect('/edit_receita5/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/edit_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/edit_receita7/'+str(receitas.id)+'')

    return render(request, 'front/edit_receita6.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def edit_receita7(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)

            if voltar == "Sim":
                return redirect('/edit_receita6/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/edit_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/edit_receita8/'+str(receitas.id)+'')

    return render(request, 'front/edit_receita7.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def edit_receita8(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)

            if voltar == "Sim":
                return redirect('/edit_receita7/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/edit_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/edit_receita9/'+str(receitas.id)+'')

    return render(request, 'front/edit_receita8.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def edit_receita9(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)

            if voltar == "Sim":
                return redirect('/edit_receita8/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/edit_receitadetalhes/'+str(receitas.id)+'')
            elif prox == "Sim":
                return redirect('/edit_receita10/'+str(receitas.id)+'')

    return render(request, 'front/edit_receita9.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def edit_receita10(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    ingredientes = MeusIngredientes.objects.all()

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)

            if voltar == "Sim":
                return redirect('/edit_receita9/'+str(receitas.id)+'')
            if salvar == "Sim":
                return redirect('/add_receita?id='+str(receitas.id)+'')

    return render(request, 'front/edit_receita10.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def add_receitadetalhes(request, id):
    ingredientes = DBIngredientes.objects.all()

    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    voltar = request.POST.get('voltar')

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)
            try:
                receitas.Custo_Ingrediente = float(receitas.Ingrediente.Valor_Pago) * float(receitas.Quantidade)
                receitas.Custo_Ingrediente_2 = float(receitas.Ingrediente_2.Valor_Pago) * float(receitas.Quantidade_2)
                receitas.Custo_Ingrediente_3 = float(receitas.Ingrediente_3.Valor_Pago) * float(receitas.Quantidade_3)
                receitas.Custo_Ingrediente_4 = float(receitas.Ingrediente_4.Valor_Pago) * float(receitas.Quantidade_4)
                receitas.Custo_Ingrediente_5 = float(receitas.Ingrediente_5.Valor_Pago) * float(receitas.Quantidade_5)
                receitas.Custo_Ingrediente_6 = float(receitas.Ingrediente_6.Valor_Pago) * float(receitas.Quantidade_6)
                receitas.Custo_Ingrediente_7 = float(receitas.Ingrediente_7.Valor_Pago) * float(receitas.Quantidade_7)
                receitas.Custo_Ingrediente_8 = float(receitas.Ingrediente_8.Valor_Pago) * float(receitas.Quantidade_8)
                receitas.Custo_Ingrediente_9 = float(receitas.Ingrediente_9.Valor_Pago) * float(receitas.Quantidade_9)
                receitas.Custo_Ingrediente_10 = float(receitas.Ingrediente_10.Valor_Pago) * float(receitas.Quantidade_10)
            except:
                pass

            print(receitas.Ingrediente_2)

            if receitas.Ingrediente_2 is None:
                receitas.Custo_Ingrediente_2 = 0

            if receitas.Ingrediente_3 is None:
                receitas.Custo_Ingrediente_3 = 0

            if receitas.Ingrediente_4 is None:
                receitas.Custo_Ingrediente_4 = 0

            if receitas.Ingrediente_5 is None:
                receitas.Custo_Ingrediente_5 = 0

            if receitas.Ingrediente_6 is None:
                receitas.Custo_Ingrediente_6 = 0

            if receitas.Ingrediente_7 is None:
                receitas.Custo_Ingrediente_7 = 0

            if receitas.Ingrediente_8 is None:
                receitas.Custo_Ingrediente_8 = 0
            
            if receitas.Ingrediente_9 is None:
                receitas.Custo_Ingrediente_9 = 0

            if receitas.Ingrediente_10 is None:
                receitas.Custo_Ingrediente_10 = 0

            receitas.Custo_Total_Ingredientes = receitas.Custo_Ingrediente + receitas.Custo_Ingrediente_2 + receitas.Custo_Ingrediente_3 + receitas.Custo_Ingrediente_4 + receitas.Custo_Ingrediente_5 + receitas.Custo_Ingrediente_6 + receitas.Custo_Ingrediente_7 + receitas.Custo_Ingrediente_8 + receitas.Custo_Ingrediente_9 + receitas.Custo_Ingrediente_10
            receitas.save()

            lista = Receita.objects.latest('id')
            if voltar == "Sim":
                return redirect('/add_receita10/'+str(lista.id)+'')
            else:
                return redirect('sucesso')

    lista = Receita.objects.latest('id')

    return render(request, 'front/add_receitadetalhes.html', {'form': form, 'ingredientes': ingredientes, 'lista': lista })

@login_required
def edit_receitadetalhes(request, id):
    ingredientes = DBIngredientes.objects.all()

    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)

    voltar = request.POST.get('voltar')

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)
            try:
                receitas.Custo_Ingrediente = float(receitas.Ingrediente.Valor_Pago) * float(receitas.Quantidade)
                receitas.Custo_Ingrediente_2 = float(receitas.Ingrediente_2.Valor_Pago) * float(receitas.Quantidade_2)
                receitas.Custo_Ingrediente_3 = float(receitas.Ingrediente_3.Valor_Pago) * float(receitas.Quantidade_3)
                receitas.Custo_Ingrediente_4 = float(receitas.Ingrediente_4.Valor_Pago) * float(receitas.Quantidade_4)
                receitas.Custo_Ingrediente_5 = float(receitas.Ingrediente_5.Valor_Pago) * float(receitas.Quantidade_5)
                receitas.Custo_Ingrediente_6 = float(receitas.Ingrediente_6.Valor_Pago) * float(receitas.Quantidade_6)
                receitas.Custo_Ingrediente_7 = float(receitas.Ingrediente_7.Valor_Pago) * float(receitas.Quantidade_7)
                receitas.Custo_Ingrediente_8 = float(receitas.Ingrediente_8.Valor_Pago) * float(receitas.Quantidade_8)
                receitas.Custo_Ingrediente_9 = float(receitas.Ingrediente_9.Valor_Pago) * float(receitas.Quantidade_9)
                receitas.Custo_Ingrediente_10 = float(receitas.Ingrediente_10.Valor_Pago) * float(receitas.Quantidade_10)
            except:
                pass

            print(receitas.Ingrediente_2)

            if receitas.Ingrediente_2 is None:
                receitas.Custo_Ingrediente_2 = 0

            if receitas.Ingrediente_3 is None:
                receitas.Custo_Ingrediente_3 = 0

            if receitas.Ingrediente_4 is None:
                receitas.Custo_Ingrediente_4 = 0

            if receitas.Ingrediente_5 is None:
                receitas.Custo_Ingrediente_5 = 0

            if receitas.Ingrediente_6 is None:
                receitas.Custo_Ingrediente_6 = 0

            if receitas.Ingrediente_7 is None:
                receitas.Custo_Ingrediente_7 = 0

            if receitas.Ingrediente_8 is None:
                receitas.Custo_Ingrediente_8 = 0
            
            if receitas.Ingrediente_9 is None:
                receitas.Custo_Ingrediente_9 = 0

            if receitas.Ingrediente_10 is None:
                receitas.Custo_Ingrediente_10 = 0

            receitas.Custo_Total_Ingredientes = receitas.Custo_Ingrediente + receitas.Custo_Ingrediente_2 + receitas.Custo_Ingrediente_3 + receitas.Custo_Ingrediente_4 + receitas.Custo_Ingrediente_5 + receitas.Custo_Ingrediente_6 + receitas.Custo_Ingrediente_7 + receitas.Custo_Ingrediente_8 + receitas.Custo_Ingrediente_9 + receitas.Custo_Ingrediente_10
            receitas.save()

            lista = Receita.objects.get(pk=id)
            if voltar == "Sim":
                return redirect('/edit_receita10/'+str(lista.id)+'')
            else:
                return redirect('sucesso')

    lista = Receita.objects.get(pk=id)

    return render(request, 'front/edit_receitadetalhes.html', {'form': form, 'ingredientes': ingredientes, 'lista': lista })

@login_required
def delete_receita(request, id):
    Id = get_object_or_404(Receita, pk=id)
    Id.delete()

    return redirect('/add_receita')

@login_required
def informacoesnegocio(request):

    form = MeuNegocioForm
    if request.method == 'POST':
        form = MeuNegocioForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            negocios = MeuNegocio.objects.latest('id')
        return redirect('/cadastrarinformacoes2/'+str(negocios.id)+'')
        
    return render(request, 'front/cadastrarinformacoes.html', {'form': form})

@login_required
def informacoesnegocio2(request, id):
    id_ = get_object_or_404(MeuNegocio, pk=id)

    form = MeuNegocioForm(instance=id_)
    if request.method == 'POST':
        form = MeuNegocioForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
        return redirect('sucesso')
        
    return render(request, 'front/cadastrarinformacoes2.html', {'form': form})

@login_required
def delete_meunegocio(request, id):
    Id = get_object_or_404(MeuNegocio, pk=id)
    Id.delete()

    return redirect('/meusnegocios')

@login_required
def sucesso(request):
    return render(request, 'front/sucesso.html')

@login_required
def meusnfuncionarios(request):
    funcionarios = Funcionarios.objects.all().count()
    if funcionarios <= 0:
        return render(request, 'front/funcionarios1.html')
    else:
        return redirect('/funcionarios')

@login_required
def funcionarios(request):

    funcionarios = Funcionarios.objects.all().count()

    form = FuncionariosForm
    if request.method == 'POST':
        form = FuncionariosForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
        return redirect('sucesso')

    if funcionarios <= 0:
        return render(request, 'front/funcionarios.html', {'form': form})

    funcionarios = Funcionarios.objects.all()
    
    return render(request, 'front/funcionariosdetalhes.html', {'funcionarios': funcionarios})

@login_required
def edit_funcionarios(request, id):
    id_ = get_object_or_404(Funcionarios, pk=id)
    form = FuncionariosForm(instance=id_)

    if request.method == 'POST':
        form = FuncionariosForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
        return redirect('sucesso')

    return render(request, 'front/edit_funcionarios.html', {'form': form})

@login_required
def delete_funcionarios(request, id):
    Id = get_object_or_404(Funcionarios, pk=id)
    Id.delete()

    return redirect('/meusnegocios')

@login_required
def minhasentregas(request):
    entregas = Entregas.objects.all().count()
    if entregas <= 0:
        return render(request, 'front/entregas1.html')
    else:
        return redirect('/entregas')

@login_required
def entregas(request):

    form = EntregasForm
    if request.method == 'POST':
        form = EntregasForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            entregas = Entregas.objects.latest('id')
            return redirect('/entregas2/'+str(entregas.id)+'')

    entregas = Entregas.objects.all().count()

    if entregas <= 0:
        return render(request, 'front/entregas.html')
        
    entregas = Entregas.objects.all()
    
    return render(request, 'front/entregasdetalhes.html', {'entregas': entregas})
              
                
@login_required
def entregas2(request, id):
    id_ = get_object_or_404(Entregas, pk=id)

    form = EntregasForm(instance=id_)

    entregas = Entregas.objects.all()

    if request.method == 'POST':
        form = EntregasForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            return redirect('/sucesso')
        
    return render(request, 'front/entregas2.html', {'form': form, 'entregas': entregas})

@login_required
def edit_entregas(request, id):
    id_ = get_object_or_404(Entregas, pk=id)
    form = EntregasForm(instance=id_)

    if request.method == 'POST':
        form = EntregasForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
        return redirect('sucesso')

    return render(request, 'front/edit_entregas.html', {'form': form})

@login_required
def delete_entregas(request, id):
    Id = get_object_or_404(Entregas, pk=id)
    Id.delete()

    return redirect('/meusnegocios')

@login_required
def minhasdespesas(request):
    despesas = OutrasDespesas.objects.all().count()
    if despesas <= 0:
        return render(request, 'front/despesas1.html')
    else:
        return redirect('/despesas')

@login_required
def despesas(request):

    form = OutrasDespesasForm
    if request.method == 'POST':
        form = OutrasDespesasForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            despesas = OutrasDespesas.objects.latest('id')
            return redirect('/despesas2/'+str(despesas.id)+'')
                
    despesas = OutrasDespesas.objects.all().count()
    
    if despesas <= 0:
        return render(request, 'front/despesas.html', {'despesas': despesas})

    despesas = OutrasDespesas.objects.all()

    return render(request, 'front/despesasdetalhes.html', {'despesas': despesas})
    

@login_required
def despesas2(request, id):
    id_ = get_object_or_404(OutrasDespesas, pk=id)

    form = OutrasDespesasForm(instance=id_)

    despesas = OutrasDespesas.objects.all()

    if request.method == 'POST':
        form = OutrasDespesasForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            return redirect('/sucesso')
        
    return render(request, 'front/despesas2.html', {'form': form, 'despesas': despesas})

@login_required
def edit_despesas(request, id):
    id_ = get_object_or_404(OutrasDespesas, pk=id)
    form = OutrasDespesasForm(instance=id_)

    if request.method == 'POST':
        form = OutrasDespesasForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
        return redirect('sucesso')

    return render(request, 'front/edit_despesas.html', {'form': form})

@login_required
def delete_despesas(request, id):
    Id = get_object_or_404(OutrasDespesas, pk=id)
    Id.delete()

    return redirect('/meusnegocios')

@login_required
def meusingredientes(request):
    try:
        letra = request.GET.get('letra').upper()
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente").filter(Entrada_Ingrediente__icontains=''+letra+'')
    except:
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente")
        # teste = MeusIngredientes.objects.all()

    return render(request, 'front/meusingredientes.html', {'ingredientes': ingredientes})

@login_required
def meusingredientes2(request):

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    filtro = MeusIngredientes.objects.all()
    myFilter = MeusIngredientesFilter(request.GET, queryset=filtro)
    ingredientes = myFilter.qs

    return render(request, 'front/meusingredientes2.html', {'ingredientes': ingredientes, 'myFilter': myFilter})

@login_required
def meusingredientes3(request):

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente").filter(Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = MeusIngredientes.objects.order_by("Ingrediente")

    filtro = MeusIngredientes.objects.all()
    myFilter = MeusIngredientesFilter(request.GET, queryset=filtro)
    ingredientes = myFilter.qs

    return render(request, 'front/meusingredientes3.html', {'ingredientes': ingredientes, 'myFilter': myFilter})

@login_required
def meusingredientesdetalhes(request, id):
    ingredientes = DBIngredientes.objects.filter(pk=id)

    detalhes_ingredientes = MeusIngredientes.objects.all()

    form = MeusIngredientesForm

    if request.method == 'POST':
        form = MeusIngredientesForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
        return redirect('sucesso')

    return render(request, 'front/meusingredientesdetalhes.html', {'form': form, 'ingredientes': ingredientes, 'detalhes_ingredientes': detalhes_ingredientes})

@login_required
def edit_meusingredientesdetalhes(request, id):
    ingredientes = DBIngredientes.objects.filter(pk=id)

    detalhes_ingredientes = MeusIngredientes.objects.all()

    id_ = get_object_or_404(MeusIngredientes, pk=id)

    form = MeusIngredientesForm(instance=id_)

    if request.method == 'POST':
        form = MeusIngredientesForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
        return redirect('sucesso')

    return render(request, 'front/edit_meusingredientesdetalhes.html', {'form': form, 'ingredientes': ingredientes, 'detalhes_ingredientes': detalhes_ingredientes})

@login_required
def meusingredientesedit(request, id):
    ingredientes = DBIngredientes.objects.filter(pk=id)

    detalhes_ingredientes = MeusIngredientes.objects.all()

    id_ = get_object_or_404(MeusIngredientes, pk=id)

    form = MeusIngredientesForm(instance=id_)

    if request.method == 'POST':
        form = MeusIngredientesForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
        return redirect('sucesso')

    return render(request, 'front/meusingredientesedit.html', {'form': form, 'ingredientes': ingredientes, 'detalhes_ingredientes': detalhes_ingredientes})

@login_required
def listadecompras(request):
    ingredientes = DBIngredientes.objects.all()

    form = ListadeComprasForm

    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente").filter(Entrada_Ingrediente__icontains=''+letra+'')
    except:
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente")

    if request.method == 'POST':
        form = ListadeComprasForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            lista = ListadeCompras.objects.latest('id')
            if salvar == "Sim":
                return redirect('/quantidade/'+str(lista.id)+'')
            elif prox == "Sim":
                return redirect('/listadecompras2/'+str(lista.id)+'')

    return render(request, 'front/listadecompras.html', {'form': form, 'ingredientes': ingredientes})

@login_required
def listadecompras1(request, id):
    ingredientes = DBIngredientes.objects.all()

    id_ = get_object_or_404(ListadeCompras, pk=id)

    form = ListadeComprasForm(instance=id_)

    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente").filter(Entrada_Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente")

    if request.method == 'POST':
        form = ListadeComprasForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            lista = ListadeCompras.objects.latest('id')

            if salvar == "Sim":
                return redirect('/quantidade/'+str(lista.id)+'')
            elif prox == "Sim":
                return redirect('/listadecompras2/'+str(lista.id)+'')
            
    return render(request, 'front/listadecompras1.html', {'form': form, 'ingredientes': ingredientes })

@login_required
def listadecompras2(request, id):
    ingredientes = DBIngredientes.objects.all()

    id_ = get_object_or_404(ListadeCompras, pk=id)

    form = ListadeComprasForm(instance=id_)

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente").filter(Entrada_Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente")

    if request.method == 'POST':
        form = ListadeComprasForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            lista = ListadeCompras.objects.latest('id')

            if voltar == "Sim":
                return redirect('/listadecompras1/'+str(lista.id)+'')
            elif salvar == "Sim":
                return redirect('/quantidade/'+str(lista.id)+'')
            elif prox == "Sim":
                return redirect('/listadecompras3/'+str(lista.id)+'')
            
    return render(request, 'front/listadecompras2.html', {'form': form, 'ingredientes': ingredientes })

@login_required
def listadecompras3(request, id):
    ingredientes = DBIngredientes.objects.all()

    id_ = get_object_or_404(ListadeCompras, pk=id)

    form = ListadeComprasForm(instance=id_)

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente").filter(Entrada_Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente")

    if request.method == 'POST':
        form = ListadeComprasForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            lista = ListadeCompras.objects.latest('id')

            if voltar == "Sim":
                return redirect('/listadecompras2/'+str(lista.id)+'')
            elif salvar == "Sim":
                return redirect('/quantidade/'+str(lista.id)+'')
            elif prox == "Sim":
                return redirect('/listadecompras4/'+str(lista.id)+'')
            
    return render(request, 'front/listadecompras3.html', {'form': form, 'ingredientes': ingredientes })

@login_required
def listadecompras4(request, id):
    ingredientes = DBIngredientes.objects.all()

    id_ = get_object_or_404(ListadeCompras, pk=id)

    form = ListadeComprasForm(instance=id_)

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente").filter(Entrada_Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente")
 
    if request.method == 'POST':
        form = ListadeComprasForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            lista = ListadeCompras.objects.latest('id')

            if voltar == "Sim":
                return redirect('/listadecompras3/'+str(lista.id)+'')
            elif salvar == "Sim":
                return redirect('/quantidade/'+str(lista.id)+'')
            elif prox == "Sim":
                return redirect('/listadecompras5/'+str(lista.id)+'')
            
    return render(request, 'front/listadecompras4.html', {'form': form, 'ingredientes': ingredientes })

@login_required
def listadecompras5(request, id):
    ingredientes = DBIngredientes.objects.all()

    id_ = get_object_or_404(ListadeCompras, pk=id)

    form = ListadeComprasForm(instance=id_)

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente").filter(Entrada_Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente")
 
    if request.method == 'POST':
        form = ListadeComprasForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            lista = ListadeCompras.objects.latest('id')

            if voltar == "Sim":
                return redirect('/listadecompras4/'+str(lista.id)+'')
            elif salvar == "Sim":
                return redirect('/quantidade/'+str(lista.id)+'')
            elif prox == "Sim":
                return redirect('/listadecompras6/'+str(lista.id)+'')
            
    return render(request, 'front/listadecompras5.html', {'form': form, 'ingredientes': ingredientes })

@login_required
def listadecompras6(request, id):
    ingredientes = DBIngredientes.objects.all()

    id_ = get_object_or_404(ListadeCompras, pk=id)

    form = ListadeComprasForm(instance=id_)

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente").filter(Entrada_Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente")
 
    if request.method == 'POST':
        form = ListadeComprasForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            lista = ListadeCompras.objects.latest('id')

            if voltar == "Sim":
                return redirect('/listadecompras5/'+str(lista.id)+'')
            elif salvar == "Sim":
                return redirect('/quantidade/'+str(lista.id)+'')
            elif prox == "Sim":
                return redirect('/listadecompras7/'+str(lista.id)+'')
            
    return render(request, 'front/listadecompras6.html', {'form': form, 'ingredientes': ingredientes })

@login_required
def listadecompras7(request, id):
    ingredientes = DBIngredientes.objects.all()

    id_ = get_object_or_404(ListadeCompras, pk=id)

    form = ListadeComprasForm(instance=id_)

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente").filter(Entrada_Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente")
 
    if request.method == 'POST':
        form = ListadeComprasForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            lista = ListadeCompras.objects.latest('id')

            if voltar == "Sim":
                return redirect('/listadecompras6/'+str(lista.id)+'')
            elif salvar == "Sim":
                return redirect('/quantidade/'+str(lista.id)+'')
            elif prox == "Sim":
                return redirect('/listadecompras8/'+str(lista.id)+'')
            
    return render(request, 'front/listadecompras7.html', {'form': form, 'ingredientes': ingredientes })

@login_required
def listadecompras8(request, id):
    ingredientes = DBIngredientes.objects.all()

    id_ = get_object_or_404(ListadeCompras, pk=id)

    form = ListadeComprasForm(instance=id_)

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente").filter(Entrada_Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente")
 
    if request.method == 'POST':
        form = ListadeComprasForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            lista = ListadeCompras.objects.latest('id')

            if voltar == "Sim":
                return redirect('/listadecompras7/'+str(lista.id)+'')
            elif salvar == "Sim":
                return redirect('/quantidade/'+str(lista.id)+'')
            elif prox == "Sim":
                return redirect('/listadecompras9/'+str(lista.id)+'')
            
    return render(request, 'front/listadecompras8.html', {'form': form, 'ingredientes': ingredientes })

@login_required
def listadecompras9(request, id):
    ingredientes = DBIngredientes.objects.all()

    id_ = get_object_or_404(ListadeCompras, pk=id)

    form = ListadeComprasForm(instance=id_)

    voltar = request.POST.get('voltar')
    prox = request.POST.get('prox')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente").filter(Entrada_Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente")
 
    if request.method == 'POST':
        form = ListadeComprasForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            lista = ListadeCompras.objects.latest('id')

            if voltar == "Sim":
                return redirect('/listadecompras8/'+str(lista.id)+'')
            elif salvar == "Sim":
                return redirect('/quantidade/'+str(lista.id)+'')
            elif prox == "Sim":
                return redirect('/listadecompras10/'+str(lista.id)+'')
            
    return render(request, 'front/listadecompras9.html', {'form': form, 'ingredientes': ingredientes })

@login_required
def listadecompras10(request, id):
    ingredientes = DBIngredientes.objects.all()

    id_ = get_object_or_404(ListadeCompras, pk=id)

    form = ListadeComprasForm(instance=id_)

    voltar = request.POST.get('voltar')
    salvar = request.POST.get('salvar')

    try:
        letra = request.GET.get('letra').upper()
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente").filter(Entrada_Ingrediente__startswith=''+letra+'')
    except:
        ingredientes = DBIngredientes.objects.order_by("Entrada_Ingrediente")
 
    if request.method == 'POST':
        form = ListadeComprasForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            lista = ListadeCompras.objects.latest('id')

            if voltar == "Sim":
                return redirect('/listadecompras9/'+str(lista.id)+'')
            elif salvar == "Sim":
                return redirect('/quantidade/'+str(lista.id)+'')
            
    return render(request, 'front/listadecompras10.html', {'form': form, 'ingredientes': ingredientes })

@login_required
def quantidade(request, id):
    ingredientes = DBIngredientes.objects.all()

    id_ = get_object_or_404(ListadeCompras, pk=id)

    form = ListadeComprasForm(instance=id_)

    voltar = request.POST.get('voltar')

    if request.method == 'POST':
        form = ListadeComprasForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()

            lista = ListadeCompras.objects.latest('id')
            if voltar == "Sim":
                return redirect('/listadecompras10/'+str(lista.id)+'')
            else:
                return redirect('sucesso')

    lista = ListadeCompras.objects.latest('id')

    return render(request, 'front/quantidade.html', {'form': form, 'ingredientes': ingredientes, 'lista': lista })

@login_required
def adicionar_detalhes_receita(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)
        return redirect('/adicionar_detalhes_receita_2/'+str(receitas.id)+'')
    
    return render(request, 'front/adicionar_detalhes_receita_1.html', {'form': form})

@login_required
def adicionar_detalhes_receita_2(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)
        return redirect('/adicionar_detalhes_receita_3/'+str(receitas.id)+'')
    
    return render(request, 'front/adicionar_detalhes_receita_2.html', {'form': form})

@login_required
def adicionar_detalhes_receita_3(request, id):
    id_ = get_object_or_404(Receita, pk=id)
    receitas = Receita.objects.get(pk=id)
    form = ReceitaForm(instance=id_)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)
        return redirect('/adicionar_detalhes_receita_4/'+str(receitas.id)+'')
    
    return render(request, 'front/adicionar_detalhes_receita_3.html', {'form': form, 'receitas': receitas})

@login_required
def adicionar_detalhes_receita_4(request, id):
    id_ = get_object_or_404(Receita, pk=id)
    receitas = Receita.objects.get(pk=id)
    form = ReceitaForm(instance=id_)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)
            receitas.Total_Valor_Venda = int(receitas.Valor_Venda) * int(receitas.Venda_Media)
            receitas.save()
        return redirect('/detalhes_receita/'+str(receitas.id)+'?id=' + str(receitas.id))
    
    return render(request, 'front/adicionar_detalhes_receita_4.html', {'form': form, 'receitas': receitas})

@login_required
def materiais_receita(request, id):
    receitas = Receita.objects.all().count()

    if receitas <= 0:
        form = ReceitaForm()
        if request.method == 'POST':
            form = ReceitaForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user 
                form.save()
                receitas = Receita.objects.latest('id')
            return redirect('/materiais_receita_1/'+str(receitas.id)+'')
        
        return render(request, 'front/materiais_receita.html', {'form': form})
    else:
        receitas = Receita.objects.all()

        filtro = Receita.objects.all()
        myFilter = ReceitaFilter(request.GET, queryset=filtro)
        receitas = myFilter.qs

        acompanhamentos = Receita.objects.filter(categoria='Acompanhamentos').count()
        bolos = Receita.objects.filter(categoria='Bolos').count()
        bebidas = Receita.objects.filter(categoria='Bebidas').count()
        caldos_molhos = Receita.objects.filter(categoria='Caldos e Molhos').count()
        doces_sobremesas = Receita.objects.filter(categoria='Doces e Sobremesas').count()
        petisco = Receita.objects.filter(categoria='Petisco').count()
        pratos = Receita.objects.filter(categoria='Pratos').count()
        salgados = Receita.objects.filter(categoria='Salgados').count()
        outra = Receita.objects.filter(categoria='Outra Categoria').count()

        return render(request, 'front/materiais_receita.html', {'receitas': receitas, 'acompanhamentos': acompanhamentos, 'bolos': bolos, 'bebidas': bebidas,
        'caldos_molhos': caldos_molhos, 'doces_sobremesas': doces_sobremesas, 'petisco': petisco, 'pratos': pratos, 'salgados': salgados, 'outra': outra,
        'myFilter': myFilter})

@login_required
def materiais_receita_1(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)
        return redirect('/materiais_receita_2/'+str(receitas.id)+'')
    
    return render(request, 'front/materiais_receita_1.html', {'form': form})

@login_required
def materiais_receita_2(request, id):
    id_ = get_object_or_404(Receita, pk=id)

    form = ReceitaForm(instance=id_)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=id_)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            receitas = Receita.objects.get(pk=id)
            receitas.Custo_Material = int(receitas.Quantidade_Tipo_Material) * int(receitas.Valor_Material)
            receitas.Custo_Total_Geral = int(float(receitas.Custo_Total_Ingredientes)) + int(receitas.Custo_Material)
            receitas.Lucro_Bruto = int(receitas.Total_Valor_Venda) - receitas.Custo_Total_Geral

            receitas.Porc_Custo_Total_Geral = (receitas.Custo_Total_Geral / int(receitas.Total_Valor_Venda)) * 100
            receitas.Porc_Custo_Total_Geral = round(receitas.Porc_Custo_Total_Geral, 2)
            receitas.Porc_Custo_Total_Ingredientes = (int(float(receitas.Custo_Total_Ingredientes)) / int(receitas.Total_Valor_Venda)) * 100
            receitas.Porc_Custo_Total_Ingredientes = round(receitas.Porc_Custo_Total_Ingredientes, 2)
            receitas.Porc_Custo_Material = (receitas.Custo_Material / int(receitas.Total_Valor_Venda)) * 100
            receitas.Porc_Custo_Material = round(receitas.Porc_Custo_Material, 2)
            receitas.Porc_Lucro_Bruto = (receitas.Lucro_Bruto / int(receitas.Total_Valor_Venda)) * 100
            receitas.Porc_Lucro_Bruto = round(receitas.Porc_Lucro_Bruto, 2)
            
            receitas.save()

        return redirect('/materiais_receita/'+str(receitas.id)+'?id='+str(receitas.id))
    
    return render(request, 'front/materiais_receita_2.html', {'form': form})

@login_required
def lucro_receita(request, id):
    receitas = Receita.objects.all().count()

    if receitas <= 0:
        form = ReceitaForm()
        if request.method == 'POST':
            form = ReceitaForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user 
                form.save()
                receitas = Receita.objects.latest('id')
            return redirect('/lucro_receita/'+str(receitas.id)+'')
        
        return render(request, 'front/lucro_receita.html', {'form': form})
    else:
        receitas = Receita.objects.all()

        filtro = Receita.objects.all()
        myFilter = ReceitaFilter(request.GET, queryset=filtro)
        receitas = myFilter.qs

        acompanhamentos = Receita.objects.filter(categoria='Acompanhamentos').count()
        bolos = Receita.objects.filter(categoria='Bolos').count()
        bebidas = Receita.objects.filter(categoria='Bebidas').count()
        caldos_molhos = Receita.objects.filter(categoria='Caldos e Molhos').count()
        doces_sobremesas = Receita.objects.filter(categoria='Doces e Sobremesas').count()
        petisco = Receita.objects.filter(categoria='Petisco').count()
        pratos = Receita.objects.filter(categoria='Pratos').count()
        salgados = Receita.objects.filter(categoria='Salgados').count()
        outra = Receita.objects.filter(categoria='Outra Categoria').count()

        return render(request, 'front/lucro_receita.html', {'receitas': receitas, 'acompanhamentos': acompanhamentos, 'bolos': bolos, 'bebidas': bebidas,
        'caldos_molhos': caldos_molhos, 'doces_sobremesas': doces_sobremesas, 'petisco': petisco, 'pratos': pratos, 'salgados': salgados, 'outra': outra,
        'myFilter': myFilter})

