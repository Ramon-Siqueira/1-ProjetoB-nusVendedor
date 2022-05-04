import pandas as pd

# lógica - Passo a passo para a solução

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:

tabela_vendas_janeiro = pd.read_excel('janeiro.xlsx')

print(tabela_vendas)
# Para cada um arquivo:

# Verificar se algum valor na coluna de vendas é > que 55 mil

# Se for maior enviar sms com nome, mês e vendas do vendedor
