'''
Módulo04 - Estrutura de Dados - Listas

Módulo04 - Estrutura de Dados - Tuplas

'''
print('\n''Módulo 04 -  Estrutura de Dados - Tuplas ')
print('-' * 40 )


dias_da_semana = ("segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo")
print('\n''Bem vindo à Lista da Semana!')

print(dias_da_semana)

nome_usuario = input('Primerio, precisamos saber o seu nome: ')
print(f'Ooiê, {nome_usuario}!')

novo_dia = input('Qual dia da semena é ideal pra você? ').lower().strip()

if novo_dia == 'domingo':
  print('Hmm, dia de macarronada!! 🍜')

elif novo_dia == 'segunda':
  print('Tá looonge do fim de semana! 😓')

elif novo_dia == 'terça':
  print('-1 dia! Falta pouco para o final de semana 🥱')

elif novo_dia == 'quarta':
  print('Bora que bora! 😌')

elif novo_dia == 'quinta':
  print('Metade da semana já foi ✌')

elif novo_dia == 'sexta':
  print('Sextoou! 😁')

elif novo_dia == 'sabado':
  print('Sábadoou! 🤩')

else:
  print('❌ Hmm, não existe esse dia na Lista da Semana. Tente novamente!')