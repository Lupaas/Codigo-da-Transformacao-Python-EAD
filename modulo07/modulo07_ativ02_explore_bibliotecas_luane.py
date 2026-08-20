'''
Programador: As variáveis, serão inseridas no app - (Back-End)

Dev: Existe a interação com o usuário - Web Design (Front-end)
'''

from datetime import datetime, timedelta
from faker import Faker
import random
import utilidades


num1 = 10
num2 = 5

print('🥮🍥 Teste de Utilidades 🍥🥮')
print(f'Números utilizados: {num1} e {num2}')

print(f' Usando Adição ({num1}) + ({num2}) :', utilidades.soma(num1, num2))

print(f' Usando Subtração ({num1}) - ({num2}) :', utilidades.subtrair(num1, num2))

print(f' Usando Multiplicação ({num1}) * ({num2}) :', utilidades.multiplicar(num1, num2))

print(f' Usando Divisão ({num1}) / ({num2}) :', utilidades.dividir(num1, num2))

print(f' Usando Divisão Inteira ({num1}) // ({num2}) :', utilidades.divisao_inteira(num1, num2))

print(f' Usando Resto da Divisão ({num1}) % ({num2}) :', utilidades.resto_divisao(num1, num2))

print(f' Usando Potenciação ({num1}) ^ ({num2}) :', utilidades.potencia(num1, num2))

print('\n === Teste de Segurança (Divisão por Zero) ===')
print("Divisão por zero:", utilidades.dividir(10, 0))



# -------------------------------------------------------------

print('\n' + '='*50)
print('       🍨  SISTEMA DE PEDIDOS - AÇAÍTERIA  🍨     ')
print('='*50 + '\n')

fake = Faker('pt_BR')

nome_cliente = fake.name()
telefone = fake.cellphone_number()
endereco = fake.street_address()

tamanhos = ['300ml', '500ml', '700ml']
acompanhamentos = ['Leite em Pó', 'Granola', 'Paçoca', 'Morango', 'Banana']

tamanho_escolhido = random.choice(tamanhos)
item1, item2, item3 = random.sample(acompanhamentos, 3)

qtd_acais = 2
preco_unitario = 13
taxa_entrega = 5

subtotal = utilidades.multiplicar(qtd_acais, preco_unitario)
total_pedido = utilidades.soma(subtotal, taxa_entrega)

agora = datetime.now()
tempo_preparo_e_entrega = 45 
hora_entrega = agora + timedelta(minutes=tempo_preparo_e_entrega)


print('=== COMPROVANTE DO PEDIDO ===')
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
print(f'Previsão de Entrega: {hora_entrega.strftime("%H:%M:%S")}')
print('='*50)


print('='*50)
print('***Dados Criados - Prova de Matemática***')
print(f'Nome de mentira: {fake.name()}')
print(f'E-mail de mentira: {fake.email()}')
print(f'Telefone de mentira: {fake.phone_number()}')


print(f'Dados da Prova de Matemática')
agora = datetime.datetime.now()
print(f'Data e hora atual: {agora.strftime('%H:%M %d/%m/%Y')}')