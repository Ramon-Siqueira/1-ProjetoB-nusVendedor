import pandas as pd
from twilio.rest import Client

# Se for maior enviar sms com nome, mês e vendas do vendedor
account_sid = "AC6e4954a1bf2fbe571b8a452f073255e4"
auth_token  = "e1f9be70311464b5085d0830439c609a"
client = Client(account_sid, auth_token)


# lógica - Passo a passo para a solução

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511930878654", 
            from_="+19705389207",
            body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)
# Para cada um arquivo:
# Verificar se algum valor na coluna de vendas é > que 55 mil
