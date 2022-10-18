# -*- coding: utf-8 -*-
"""Empresas de Energia X Petrobras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KwoVEAWbRWqtN2Y2OsglvO9fQFfyhbER
"""

# Libs
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Lendo base de dados
base_dados = pd.read_excel('Dados_Empresas_Energia.xlsx')

# Verificando
base_dados.head()

# Aeris Energy: Fabricação de pás eólicas

# Alupar: Geração e transmissão

# AES Brasil: Geração

# Centrais Elétricas de Santa Catarina: Geração e distribuição

# Cemig: Geração, transmissão, distribuição e comercialização

# Companhia Energética de São Paulo (CESP): Geração e comercialização

# CPFL Energia: Geração, transmissão, distribuição e comercialização

# Series Temporais - Setar o Index (Transferindo a data como index) 
base_dados.set_index ('Data', inplace=True)

# Verificando
base_dados.head()

# Gráfico

# Estilo
plt.style.use('seaborn-darkgrid')

# Tamanho
plt.figure(figsize=(16,7))

# Título
plt.title('Análise ações de empresas de Energia', loc='left', fontsize=18, fontweight=0);

# Plot da Petrobras
plt.plot(base_dados.index, base_dados['Petrobras'], color = '#008c4a', linewidth=4, alpha=0.7)

# Texto da Petrobras
plt.text(base_dados.index[-1], base_dados['Petrobras'].tail(1), 'Petrobas', color = '#008c4a', size='large', horizontalalignment='left')

# Plot de todas as colunas
for coluna in base_dados.columns[1:]:

# Plot das outras ações
  plt.plot(base_dados.index, base_dados[coluna], color = 'gray', linewidth=2, alpha=0.7)

  # Texto das outras ações
  plt.text(base_dados.index[-1], base_dados[coluna].tail(1), coluna, color = 'black', size='large', horizontalalignment='left')

# Labels
plt.xlabel('Período')
plt.ylabel('Preço de Fechamento (R$)');

