from datetime import datetime, timedelta
from faker import Faker
import random
import utilidades


print('\n' + '='*50)
print('       🍨  SISTEMA DE PEDIDOS - AÇAÍTERIA  🍨     ')
print('='*50 + '\n')

fake = Faker('pt_BR')

# As variáveis irão pegar na "Faker" as informações necessárias para exibir o pedido do cliente
nome_cliente = fake.name()
telefone = fake.cellphone_number()
endereco = fake.street_address()

# As listas com o tamanho e acompanhamentos
tamanhos = ['300ml', '500ml', '700ml']
acompanhamentos = ['Leite em Pó', 'Granola', 'Paçoca', 'Morango', 'Banana', 'Leite Condensado']

# "tamanho_escolhido" e "item1, item2, item3" são para que seja escolhido de forma aleatoria
tamanho_escolhido = random.choice(tamanhos)
item1, item2, item3 = random.sample(acompanhamentos, 3)

# "qtd_acais", "preco_unitario" e "taxa_entrega" irá mostrar a quantidade fixa no comprovante
qtd_acais = 2
preco_unitario = 13
taxa_entrega = 5

# Importando "utilidades" faz o subtotal e o total do pedido
subtotal = utilidades.multiplicar(qtd_acais, preco_unitario)
total_pedido = utilidades.soma(subtotal, taxa_entrega)

# Exibe o horário exato + o pedido pronto e entrega
agora = datetime.now()
tempo_preparo_e_entrega = 45 
hora_entrega = agora + timedelta(minutes=tempo_preparo_e_entrega)

# Gerencia o menu "Comprovante do pedido" e exibe no terminal
print(' 📜 COMPROVANTE DO PEDIDO 📜 ')
print(f'Cliente:             {nome_cliente}')
print(f'Telefone:            {telefone}')
print(f'Endereço:            {endereco}')
print('-' * 45)
print(f'Pedido:              {qtd_acais}x Açaí {tamanho_escolhido}')
print(f'Adicionais:          {item1}, {item2} e {item3}')
print('-' * 45)
print(f'Subtotal (Açaís):    R$ {subtotal:.2f}')
print(f'Taxa de Entrega:     R$ {taxa_entrega:.2f}')
print(f'Total a Pagar:       R$ {total_pedido:.2f}')
print('-' * 45)
print(f'Horário do Pedido:   {agora.strftime("%H:%M:%S")}')
print(f'Previsão de Entrega: {hora_entrega.strftime("%H:%M:%S")}\n')
print('='*50)