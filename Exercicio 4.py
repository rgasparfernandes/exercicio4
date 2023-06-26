# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 20:56:12 2023

@author: Raquel Fernandes
"""

import pandas as pd

# 1. Importar os Dados
data = pd.read_excel('dados.xlsx', sheet_name='Data')

# 2. Limpeza dos Dados


# 3. Calcular Variação Percentual para Portugal
def calcular_variacao_percentual(consumo_inicial, consumo_final):
    return (consumo_final - consumo_inicial) / consumo_inicial * 100

# Filtrar os dados para Portugal
data_portugal = data[data['Country Name'] == 'Portugal']

# Selecionar as colunas de interesse (Ano e Consumo de Energia)
data_portugal = data_portugal[['Ano', 'Consumo de Energia']]

# Extrair os valores para Portugal entre 1990 e 2000
consumo_1990 = data_portugal[data_portugal['Ano'] == 1990]['Consumo de Energia'].values[0]
consumo_2000 = data_portugal[data_portugal['Ano'] == 2000]['Consumo de Energia'].values[0]

# Calcular e imprimir a variação percentual
variacao_percentual = calcular_variacao_percentual(consumo_1990, consumo_2000)
print(f'Variação percentual no consumo de energia elétrica em Portugal entre 1990 e 2000: {variacao_percentual:.2f}%')