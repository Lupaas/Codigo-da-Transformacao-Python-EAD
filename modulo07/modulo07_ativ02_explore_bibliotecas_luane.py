'''
Programador: As variáveis, serão inseridas no app - (Back-End)

Dev: Existe a interação com o usuário - Web Design (Front-end)
'''

import utilidades
import datetime
from faker import Faker

fake = Faker('pt-BR')

num1 = 10
num2 = 5


# O teste irá auxiliar no entendimento de como funciona as contas, como o python trabalha com elas
print('\n🥮🍥 Teste de Utilidades 🍥🥮')
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

print('\n')
print('-' * 50)


# "Dados Criados" foi um simples exemplo de como o Faker é utilizado.
print('\n 📝 Dados Criados - Prova de Matemática 📝')
print(f'Nome de mentira: {fake.name()}')
print(f'E-mail de mentira: {fake.email()}')
print(f'Telefone de mentira: {fake.phone_number()}')

# "Dados da Prova" exibe o horário exato em que você executou
print(f'\n 📜 Dados da Prova de Matemática 📜')
agora = datetime.datetime.now()
print(f'Data e hora atual: {agora.strftime('%H:%M %d/%m/%Y')}\n')