'''
Módulo 04 - Estrutura de Dados - Lista
Objetivo: Adicionar uma fruta digitada
pelo usuário na lista de frutas.



frutas = ['uva', 'maça', 'goiaba']
print(frutas) #['uva', 'maça', 'goiaba']

print('Digite uma fruta para adicionar na lista: ')

nova_fruta = input()
frutas.append('jambu')

print(frutas) #['uva', 'maça', 'goiaba', 'jambu']



Eu tinha que add de alguma forma a fruta 'jambu'
foquei apenas em add a fruta na lista, 
mas o correto seria add a fruta que o usuário digitou.
'''



frutas = ["uva", "maça", "pitaya", "pera", "banana"]

while True:
  print('-' * 40)
  print('Oiê! Essa é a Lista de frutas''\n')

  print(frutas)  #['uva', 'maça', 'pitaya', 'pera', 'banana'] 

  nova_fruta = input('\n''Qual a fruta que você deseja adicionar na lista? ')
  frutas.append(nova_fruta)
  print(f'Essas são as nossas frutas: {frutas}\n')

# Eu posso remover e adicionar elementos
# variavel + atributo devo usar o ponto "frutas.append(nova_fruta)"
## para adicionar a fruta na lista