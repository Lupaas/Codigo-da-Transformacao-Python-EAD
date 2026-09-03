'''
>01 - Em uma ordem numérica, adicione um número entre
10 a 20, e mostre a nova ordem.

ordem = [10, 20, 30, 40, 50]
print(f'Essa é a ordem atual: {ordem}')

novo_numero = int(input('Digite um número para adicionar à ordem: '))
ordem.insert(1, novo_numero)
print(f'Essa é a nova ordem: {ordem}')






>02 - Em uma lista de compras, você deve dar prioridade
máxima para o item do começo da lista


compras = ['arroz', 'feijão', 'macarrão']
print(f'Lista inicial: {compras}')

novo_item = input('Digite o item que deseja adicionar à lista de compras: ')
compras.insert(0, novo_item)
print(f'Essa é a sua nova lista de compras: {compras}')





>03 - Em uma playlist, o programa deve pedir ao usuário
uma música e inserir essa música na 
penúltima posição da lista


playlist = ["If you want to", "Falling Behind", "Spring"]
print(f'Playlist inicial: {playlist}')

nova_musica = input('Qual música você quer adicionar na penúltima posição da playlist? ')
playlist.insert(2, nova_musica)
print(f'Essa é a sua nova Playlist: {playlist}')






>04 - Em uma lista númerica, o programa deve pedir ao usuário 
um número e inserir esse número exatamente no meio da lista.

numeros = [1, 2, 3, 4, 5, 6]
print(f'Lista inicial: {numeros}')

novo_numero = int(input(f'Digite um número para adiciona-lo no meio: '))
numeros.insert(3, novo_numero)
print(f'Essa é a nova lista númerica: {numeros}')






>05 - O programa deve pedir ao usuário uma nova cor
e inseri-la na última posição da lista, 
mas sem usar append().


cores = ["vermelho", "azul", "verde"]
print(f'Lista de cores: {cores}')

nova_cor = input(f'Digite uma cor para ultima posição: ')
cores.insert(3, nova_cor)
print(f'Essa é a lista final: {cores}')






>06 - Em uma lista de hobbies, o programa deve pedir
três vezes para o usuário digitar um hobby e,
a cada vez, inserir esse hobby em uma posição diferente
da lista usando apenas insert().


hobbies = []
print(f'Lista inicial dos hobbies: {hobbies}')

hobby1 = input('Digite seu primerio hobby: ')
hobbies.insert(0, hobby1)

hobby2 = input('Digite seu segundo hobby: ')
hobbies.insert(1, hobby2)

hobby3 = input('Digite seu terceiro hobby: ')
hobbies.insert(2, hobby3)

print(f'Lista top 3 hobbies: {hobbies}')
'''
