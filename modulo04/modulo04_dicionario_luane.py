'''

'''

print('\n''Módulo 04 - Estrutura de dados - Dicionário ')
print('-' * 40 )

cardapio_semana = {
    "segunda": "Bife Acebolado",
    "terça": "Arroz Tropeiro",
    "quarta": "Lasanha de Berinjela",
    "quinta": "Pizza de Brócolis",
    "sexta": "Sushi Doce",
    "sábado": "Podrão",
    "domingo": "Churrasco Vegano"
}

while True:
  
  print('Bem-vindo ao Cardápio da Semana! \n')
  nome_usuario = input('Primeiro, precisamos do seu nome para continuarmos: ')

  dia_escolhido = input('\n''Agora, digite um dia da semana para receber o prato do dia: ').lower().strip()

  if dia_escolhido in cardapio_semana:
    comida = cardapio_semana[dia_escolhido]

    print('\n'f'É um prazer, {nome_usuario}! Na(o) {dia_escolhido}, temos um prato especial para você:\n{comida}!\n')

    print('-' * 40 )

  else:
    print(f'Desculpe, não temos "{dia_escolhido}" válido no cardápio. Tente novamente!')

    print('-' * 40 )