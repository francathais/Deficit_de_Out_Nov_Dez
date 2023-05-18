# -*- coding: utf-8 -*-
"""Cópia de codigo para tabelas de em1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UVWp1-LK0JiY5Wy6W1P6jeiGlb8LQYb3

#EM2 TABELAS
"""

import pandas as pd

# Ler a tabela original
df = pd.read_excel('EM2 de todos os contratos para colab.xlsx')

df

# Selecionar apenas as colunas de interesse
cols = ['UNIDADE', 'SERVICO', 'CARGO', 'EM2', 'CONTRATO', 'MES DE REFERENCIA']
df = df[cols]

# Adicionar o ano
df['Ano'] = 2022

# Usar a função pivot_table() para transformar a tabela
EM2TABELA = pd.pivot_table(df, values='EM2', index=['UNIDADE', 'CONTRATO', 'CARGO'], columns=['MES DE REFERENCIA'])

# Transformar o índice em colunas
EM2TABELA.reset_index(inplace=True)

# Renomear as colunas
EM2TABELA.columns = ['UNIDADE', 'CONTRATO', 'CARGO', 'EM2 (OUTUBRO)', 'EM2 (NOVEMBRO)', 'EM2 (DEZEMBRO)']

# Colocando 0 em linhas sem informação
EM2TABELA = EM2TABELA.fillna(0)

# Adicionar coluna com a soma dos déficits dos três meses
total_deficits = EM2TABELA.groupby('UNIDADE')['EM2 (OUTUBRO)', 'EM2 (NOVEMBRO)', 'EM2 (DEZEMBRO)'].sum()
total_deficits['Total Déficits'] = total_deficits.sum(axis=1)
total_deficits.reset_index(inplace=True)

# Combinar a nova coluna com a tabela original
EM2TABELA = pd.merge(EM2TABELA, total_deficits[['UNIDADE', 'Total Déficits']], on='UNIDADE', how='left')

# visualiza nova tabela
EM2TABELA

#SALVAR
!pip install openpyxl
EM2TABELA.to_excel("EM2TABELA.xlsx", index=False)

#SALVAR
from google.colab import files
files.download("EM2TABELA.xlsx")

#pega a lista d eunidades
lista_valores_unicos = EM2TABELA['UNIDADE'].unique().tolist()
lista_valores_formatados = '\n'.join(lista_valores_unicos)
print(lista_valores_formatados)

# dicionário de categorias de atendimento
categorias = {

'AMA JARDIM PERI': "AMA 24h",
'AMA SOROCABANA':"AMA 24h",
'AMA VILA PIAUÍ':"AMA 24h",
'AMA/UBS INTEGRADA JARDIM CASTRO ALVES':"AMA 12h",
'AMA/UBS INTEGRADA JARDIM ICARAÍ - QUINTANA':"AMA 12h",
'AMA/UBS INTEGRADA JARDIM LADEIRA ROSA':"AMA 12h",
'AMA/UBS INTEGRADA JARDIM MIRNA':"AMA 12h",
'AMA/UBS INTEGRADA JARDIM PAULISTANO':"AMA 12h",
'AMA/UBS INTEGRADA MASSAGISTA MÁRIO AMÉRICO':"AMA 12h",
'AMA/UBS INTEGRADA VILA BARBOSA':"AMA 12h",
'AMA/UBS INTEGRADA VILA NOVA JAGUARÉ':"AMA 12h",
'AMA/UBS INTEGRADA VILA PALMEIRAS':"AMA 12h",
'PSM BALNEÁRIO SÃO JOSÉ':'PSM',
'PSM FREGUESIA DO Ó - 21 DE JUNHO':'PSM',
'PSM LAPA - PROF. JOÃO CATARIN MEZOMO':'PSM',
'UPA DONA MARIA ANTONIETA FERREIRA DE BARROS':"UPA",
'UPA JARDIM ELISA MARIA I':"UPA",
'UPA PARELHEIROS':"UPA",

}

# adiciona uma nova coluna com a categoria de atendimento de cada unidade
EM2TABELA['Categoria'] = EM2TABELA['UNIDADE'].map(categorias)

print(EM2TABELA)

#Contrato R001


# filtra a tabela por contrato
tabela_contrato_A = EM2TABELA.query("CONTRATO == 'R001'")

# adiciona uma nova coluna com a categoria de atendimento de cada unidade
tabela_contrato_A['Categoria'] = tabela_contrato_A['UNIDADE'].map(categorias)

# agrupa a tabela por categoria e soma o déficit total de cada categoria
deficit_contrato_A_por_categoria = tabela_contrato_A.groupby('Categoria')['EM2 (OUTUBRO)', 'EM2 (NOVEMBRO)', 'EM2 (DEZEMBRO)'].sum()

# imprime a tabela com o déficit total por categoria
print(deficit_contrato_A_por_categoria)

#Contrato R002


# filtra a tabela por contrato
tabela_contrato_A = EM2TABELA.query("CONTRATO == 'R002'")

# adiciona uma nova coluna com a categoria de atendimento de cada unidade
tabela_contrato_A['Categoria'] = tabela_contrato_A['UNIDADE'].map(categorias)

# agrupa a tabela por categoria e soma o déficit total de cada categoria
deficit_contrato_A_por_categoria = tabela_contrato_A.groupby('Categoria')['EM2 (OUTUBRO)', 'EM2 (NOVEMBRO)', 'EM2 (DEZEMBRO)'].sum()

# imprime a tabela com o déficit total por categoria
print(deficit_contrato_A_por_categoria)

#Contrato R007


# filtra a tabela por contrato
tabela_contrato_A = EM2TABELA.query("CONTRATO == 'R007'")

# adiciona uma nova coluna com a categoria de atendimento de cada unidade
tabela_contrato_A['Categoria'] = tabela_contrato_A['UNIDADE'].map(categorias)

# agrupa a tabela por categoria e soma o déficit total de cada categoria
deficit_contrato_A_por_categoria = tabela_contrato_A.groupby('Categoria')['EM2 (OUTUBRO)', 'EM2 (NOVEMBRO)', 'EM2 (DEZEMBRO)'].sum()

# imprime a tabela com o déficit total por categoria
print(deficit_contrato_A_por_categoria)

#Contrato R016


# filtra a tabela por contrato
tabela_contrato_A = EM2TABELA.query("CONTRATO == 'R016'")

# adiciona uma nova coluna com a categoria de atendimento de cada unidade
tabela_contrato_A['Categoria'] = tabela_contrato_A['UNIDADE'].map(categorias)

# agrupa a tabela por categoria e soma o déficit total de cada categoria
deficit_contrato_A_por_categoria = tabela_contrato_A.groupby('Categoria')['EM2 (OUTUBRO)', 'EM2 (NOVEMBRO)', 'EM2 (DEZEMBRO)'].sum()

# imprime a tabela com o déficit total por categoria
print(deficit_contrato_A_por_categoria)

#Contrato R018


# filtra a tabela por contrato
tabela_contrato_A = EM2TABELA.query("CONTRATO == 'R018'")

# adiciona uma nova coluna com a categoria de atendimento de cada unidade
tabela_contrato_A['Categoria'] = tabela_contrato_A['UNIDADE'].map(categorias)

# agrupa a tabela por categoria e soma o déficit total de cada categoria
deficit_contrato_A_por_categoria = tabela_contrato_A.groupby('Categoria')['EM2 (OUTUBRO)', 'EM2 (NOVEMBRO)', 'EM2 (DEZEMBRO)'].sum()

# imprime a tabela com o déficit total por categoria
print(deficit_contrato_A_por_categoria)

"""#TABELA EM1"""

import pandas as pd

# Ler a tabela original
df2 = pd.read_excel('EM1 de todos contratos para colab.xlsx')

df2

# Selecionar apenas as colunas de interesse
cols = ['UNIDADE', 'SERVICO', 'CARGO', 'EM1', 'CONTRATO', 'MES DE REFERENCIA']
df2 = df2[cols]

# Adicionar o ano
df2['Ano'] = 2022

# Usar a função pivot_table() para transformar a tabela
EM1TABELA = pd.pivot_table(df2, values='EM1', index=['UNIDADE', 'CONTRATO', 'CARGO'], columns=['MES DE REFERENCIA'])

# Transformar o índice em colunas
EM1TABELA.reset_index(inplace=True)

# Renomear as colunas
EM1TABELA.columns = ['UNIDADE', 'CONTRATO', 'CARGO', 'EM1 (OUTUBRO)', 'EM1 (NOVEMBRO)', 'EM1 (DEZEMBRO)']

# Colocando 0 em linhas sem informação
EM1TABELA = EM1TABELA.fillna(0)

# Adicionar coluna com a soma dos déficits dos três meses
total_deficits = EM1TABELA.groupby('UNIDADE')['EM1 (OUTUBRO)', 'EM1 (NOVEMBRO)', 'EM1 (DEZEMBRO)'].sum()
total_deficits['Total Déficits'] = total_deficits.sum(axis=1)
total_deficits.reset_index(inplace=True)

# Combinar a nova coluna com a tabela original
EM1TABELA = pd.merge(EM1TABELA, total_deficits[['UNIDADE', 'Total Déficits']], on='UNIDADE', how='left')

# visualiza nova tabela
EM1TABELA

#SALVAR
!pip install openpyxl
EM1TABELA.to_excel("EM1TABELA.xlsx", index=False)

#SALVAR
from google.colab import files
files.download("EM1TABELA.xlsx")

UNIDADES = EM1TABELA['UNIDADE'].unique().tolist()
for unidade in UNIDADES:
    print(unidade)

"""#GRAFICOS

#VEJO AS UNIDADES QUE TENHO PARA FAZER O DICIONARIO DE CATEGORIAS, IMPORTANTE VERIFICAR SE ALGUMA NÃO FOI CATEGORIZADA
"""

UNIDADES = EM1TABELA['UNIDADE'].unique().tolist()
for unidade in UNIDADES:
    print(unidade)

"""#CRIO O DICIONÁRIO DE CATEGORIAS """

# dicionário de categorias de atendimento
categorias = {
'UPA PARELHEIROS': 'Urgência/ Emergência',
 'UBS RECANTO CAMPO BELO': 'Atenção Básica',
 'PSM BALNEÁRIO SÃO JOSÉ':'Urgência/ Emergência',
 'UBS JARDIM CAMPINAS':'Atenção Básica',
 'UBS JARDIM SÃO NORBERTO': 'Atenção Básica',
 'UBS VARGEM GRANDE':'Atenção Básica',
 'UBS VERA POTY':'Atenção Básica',
 'UBS JARDIM IPORÃ':'Atenção Básica',
 'UBS PARELHEIROS':'Atenção Básica',
 'CEO III PARELHEIROS- CLÍNICA ODONTOL. ESPEC. YVETTE RANZINI VIEGAS':'At. Especializada',
 'UBS JARDIM EMBURÁ':'Atenção Básica',
 'UBS COLÔNIA':'Atenção Básica',
 'UBS BARRAGEM':'Atenção Básica',
 'UBS JARDIM DAS FONTES':'Atenção Básica',
 'UBS JARDIM SANTA FÉ':'Atenção Básica',
 'UBS JARDIM SILVEIRA':'Atenção Básica',
 'UBS MARSILAC':'Atenção Básica',
 'UBS NOVA AMÉRICA':'Atenção Básica',
 'UBS VILA ROSCHEL':'Atenção Básica',
 'CER II PARELHEIROS':'At. Especializada',
 'CAPS INFANTO JUVENIL II PARELHEIROS':'At. Especializada',
 'UPA DONA MARIA ANTONIETA FERREIRA DE BARROS':'Urgência/ Emergência',
 'UBS JARDIM CLIPER':'Atenção Básica',
 'AMB ESPEC DR. MILTON ALDRED':'At. Especializada',
 'AMA/UBS INTEGRADA JARDIM CASTRO ALVES':'Atenção Básica',
 'UBS JARDIM ELIANE':'Atenção Básica',
 'AMA/UBS INTEGRADA JARDIM ICARAÍ - QUINTANA':'Atenção Básica',
 'AMA/UBS INTEGRADA JARDIM MIRNA':'Atenção Básica',
 'UBS JARDIM REPUBLICA':'Atenção Básica',
 'UBS JORDANÓPOLIS':'Atenção Básica',
 'UBS PARQUE RESIDENCIAL COCAIA INDEPENDENTE':'Atenção Básica',
 'UBS SERGIO CHADDAD':'Atenção Básica',
 'UBS VARGINHA':'Atenção Básica',
 'UBS VELEIROS':'Atenção Básica',
 'UBS CHÁCARA DO CONDE':'Atenção Básica',
 'UBS JARDIM NOVO HORIZONTE':'Atenção Básica',
 'CAPS ADULTO III CAPELA DO SOCORRO':'At. Especializada',
 'HOSPITAL MUNICIPAL CAPELA DO SOCORRO': 'At. Especializada' ,
 'UBS AUTODROMO DR FAUZER SIMAO ABRAO':'Atenção Básica',
 'UBS SHANGRILÁ ELLUS': 'Atenção Básica',
 'CAPS III ADULTO GRAJAÚ':'At. Especializada',
 'CAPS INFANTO JUVENIL III CIDADE DUTRA':'At. Especializada',
 'CAPS ÁLCOOL E DROGAS III GRAJAÚ':'At. Especializada',
 'UBS ANCHIETA':'Atenção Básica',
 'UBS JARDIM LUCÉLIA':'Atenção Básica',
 'CER IV MILTON ALDRED':'At. Especializada',
 'CAPS INFANTO JUVENIL II CAPELA DO SOCORRO':'At. Especializada',
 'RESIDÊNCIA TERAPÊUTICA CAPELA DO SOCORRO IV':'At. Especializada',
 'UBS GAIVOTAS':'Atenção Básica',
 'RESIDÊNCIA TERAPÊUTICA CAPELA DO SOCORRO III':'At. Especializada',
 'CEO II CAPELA DO SOCORRO':'At. Especializada',
 'CAPS INFANTO JUVENIL II LAPA':'At. Especializada',
 'UBS PARQUE DA LAPA':'Atenção Básica',
 'PSM LAPA - PROF. JOÃO CATARIN MEZOMO':'Urgência/ Emergência',
 'UBS VILA IPOJUCA - WANDA COELHO DE MORAES': "Atenção Básica",
 'AMA/UBS INTEGRADA VILA NOVA JAGUARÉ':"Atenção Básica",
 'UBS VILA ROMANA':'Atenção Básica',
 'CAPS III ADULTO LAPA':'At. Especializada',
 'HOSPITAL MUNICIPAL SOROCABANA (HD LAPA)':'At. Especializada',
 'HOSPITAL MUNICIPAL SOROCABANA':'At. Especializada',
 'UBS VILA ANGLO - DR. JOSÉ SERRA RIBEIRO':'Atenção Básica',
 'UBS VILA JAGUARA':'Atenção Básica',
 'UBS MENINÓPOLIS - DR. MÁRIO FRANCISCO NAPOLITANO':'Atenção Básica',
 'UBS JOSÉ DE BARROS MAGALDI':'Atenção Básica',
 'UBS DR. MANOEL JOAQUIM PERA':'Atenção Básica',
 'UBS ALTO DE PINHEIROS':'Atenção Básica',
 'UBS JARDIM EDITE GERONCIO HENRIQUE NETO':'Atenção Básica',
 'UBS/AE/CEO DR. WALTER ELIAS':'Atenção Básica',
 'UBS ADELAIDE LOPES':'Atenção Básica',
 'UBS JARDIM GUARANI':'Atenção Básica',
 'AMA/UBS INTEGRADA JARDIM LADEIRA ROSA':'Atenção Básica',
 'UBS JARDIM PERI':'Atenção Básica',
 'UBS JARDIM VISTA ALEGRE':'Atenção Básica',
 'UBS MARIA CECÍLIA F. DONNANGELO':'Atenção Básica',
 'UBS SILMARYA REJANE MARCOLINO DE SOUZA':'Atenção Básica',
 'UBS VILA DIONÍSIA':'Atenção Básica',
 'UBS ELISA MARIA II':'Atenção Básica',
 'UBS VILA PENTEADO - FÁTIMA DE JESUS VIANA ROSA':'Atenção Básica',
 'UBS VILA PROGRESSO - JARDIM MONTE ALEGRE':'Atenção Básica',
 'AMA ESPECIALIDADES PARQUE PERUCHE':'Urgência/ Emergência',
 'CAPS ALCOOL E DROGAS II CACHOEIRINHA':'At. Especializada',
 'CAPS ADULTO II CASA VERDE':'At. Especializada',
 'CAPS INFANTO JUVENIL II FREGUESIA BRASILÂNDIA':'At. Especializada',
 'CAPS ÁLCOOL E DROGAS III FREGUESIA DO Ó BRASILANDIA':'At. Especializada',
 'CAPS INFANTO JUVENIL II CASA VERDE CACHOEIRINHA LIMAO':'At. Especializada',
 'UBS NOVA ESPERANÇA - PAULISTANO II':'Atenção Básica',
 'UNIDADE HOSPITALAR BRASILANDIA FO':'At. Especializada',
 'UBS VILA SANTA MARIA':'Atenção Básica',
 'AMA/UBS INTEGRADA VILA BARBOSA':'Atenção Básica',
 'UBS VILA TEREZINHA':'Atenção Básica',
 'UBS DR. AUGUSTO LEOPOLDO AYROSA GALVÃO':'Atenção Básica',
 'UBS DRA. ILZA WELTMAN HUTZLER':'Atenção Básica',
 'UBS JARDIM ICARAÍ - BRASILÂNDIA':'Atenção Básica',
 'AMA/UBS INTEGRADA JARDIM PAULISTANO':'Atenção Básica',
 'AMA/UBS INTEGRADA MASSAGISTA MÁRIO AMÉRICO':'Atenção Básica',
 'AMA/UBS INTEGRADA VILA PALMEIRAS':'Atenção Básica',
 'UBS CRUZ DAS ALMAS':'Atenção Básica',
 'UBS VILA DIONISIA II':'Atenção Básica',
}

# adiciona uma nova coluna com a categoria de atendimento de cada unidade
EM1TABELA['Categoria'] = EM1TABELA['UNIDADE'].map(categorias)

print(EM1TABELA)

"""SOMANDO DÉFICIT POR MÊS DE CADA CATEGORIA SEM O CONTRATO"""

# adiciona uma nova coluna com a categoria de atendimento de cada unidade
EM1TABELA['Categoria'] = EM1TABELA['UNIDADE'].map(categorias)

# agrupa a tabela por categoria e soma o déficit total de cada categoria
deficit_por_categoria = EM1TABELA.groupby('Categoria')['EM1 (OUTUBRO)', 'EM1 (NOVEMBRO)', 'EM1 (DEZEMBRO)'].sum()

# imprime a tabela com o déficit total por categoria
print(deficit_por_categoria)

"""SOMANDO DÉFICIT POR MÊS DE CADA CATEGORIA 
Precisa digitar o contrato no código para gerar o de cada um
"""

#Contrato R001


# filtra a tabela por contrato
tabela_contrato_A = EM1TABELA.query("CONTRATO == 'R001'")

# adiciona uma nova coluna com a categoria de atendimento de cada unidade
tabela_contrato_A['Categoria'] = tabela_contrato_A['UNIDADE'].map(categorias)

# agrupa a tabela por categoria e soma o déficit total de cada categoria
deficit_contrato_A_por_categoria = tabela_contrato_A.groupby('Categoria')['EM1 (OUTUBRO)', 'EM1 (NOVEMBRO)', 'EM1 (DEZEMBRO)'].sum()

# imprime a tabela com o déficit total por categoria
print(deficit_contrato_A_por_categoria)

#Contrato R002


# filtra a tabela por contrato
tabela_contrato_A = EM1TABELA.query("CONTRATO == 'R002'")

# adiciona uma nova coluna com a categoria de atendimento de cada unidade
tabela_contrato_A['Categoria'] = tabela_contrato_A['UNIDADE'].map(categorias)

# agrupa a tabela por categoria e soma o déficit total de cada categoria
deficit_contrato_A_por_categoria = tabela_contrato_A.groupby('Categoria')['EM1 (OUTUBRO)', 'EM1 (NOVEMBRO)', 'EM1 (DEZEMBRO)'].sum()

# imprime a tabela com o déficit total por categoria
print(deficit_contrato_A_por_categoria)

#Contrato R007


# filtra a tabela por contrato
tabela_contrato_A = EM1TABELA.query("CONTRATO == 'R007'")

# adiciona uma nova coluna com a categoria de atendimento de cada unidade
tabela_contrato_A['Categoria'] = tabela_contrato_A['UNIDADE'].map(categorias)

# agrupa a tabela por categoria e soma o déficit total de cada categoria
deficit_contrato_A_por_categoria = tabela_contrato_A.groupby('Categoria')['EM1 (OUTUBRO)', 'EM1 (NOVEMBRO)', 'EM1 (DEZEMBRO)'].sum()

# imprime a tabela com o déficit total por categoria
print(deficit_contrato_A_por_categoria)

#Contrato R016


# filtra a tabela por contrato
tabela_contrato_A = EM1TABELA.query("CONTRATO == 'R016'")

# adiciona uma nova coluna com a categoria de atendimento de cada unidade
tabela_contrato_A['Categoria'] = tabela_contrato_A['UNIDADE'].map(categorias)

# agrupa a tabela por categoria e soma o déficit total de cada categoria
deficit_contrato_A_por_categoria = tabela_contrato_A.groupby('Categoria')['EM1 (OUTUBRO)', 'EM1 (NOVEMBRO)', 'EM1 (DEZEMBRO)'].sum()

# imprime a tabela com o déficit total por categoria
print(deficit_contrato_A_por_categoria)

#Contrato R018


# filtra a tabela por contrato
tabela_contrato_A = EM1TABELA.query("CONTRATO == 'R018'")

# adiciona uma nova coluna com a categoria de atendimento de cada unidade
tabela_contrato_A['Categoria'] = tabela_contrato_A['UNIDADE'].map(categorias)

# agrupa a tabela por categoria e soma o déficit total de cada categoria
deficit_contrato_A_por_categoria = tabela_contrato_A.groupby('Categoria')['EM1 (OUTUBRO)', 'EM1 (NOVEMBRO)', 'EM1 (DEZEMBRO)'].sum()

# imprime a tabela com o déficit total por categoria
print(deficit_contrato_A_por_categoria)