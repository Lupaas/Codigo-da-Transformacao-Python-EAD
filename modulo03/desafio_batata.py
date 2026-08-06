'''
Como fritar batata frita (no Óleo)

1. Descasque as batatas
2. Cortá-las em formato de palito
3. Aquecer o óleo até ficar bem quente
4. Coloque as batatas dentro do óleo até ficar frita
5. Retire as batatas e coloque sobre o papel toalha para absorver o oléo que restou
6. Caso queira, jogue uma pitada de sal



Como fritar batata frita (na Air fryer)

1. Pré-aqueça a air fryer de 3 a 5 minutos.
2. Descasque as batatas.
3. Cortá-las em formato de palito.
4. Coloque as batatas em um recipiente, jogue um fio de azeite ou óleo e misture bem.
5. Coloque dentro da air fryer de 15 a 25 minutos. Chacoalhe o cesto a cada 5 ou 10 minutos).
6. Retire as batatas e coloque em um recipiente.
7. Caso queira, jogue uma pitada de sal.
'''

def fritar_batata(tempo_fritura):
    print('\nComo fritar batata frita 🍟')
    print('1. Descasque as batatas')
    print('2. Cortá-las em formato de palito')
    print('3. Aqueça o óleo até ficar bem quente')
    print('4. Coloque as batatas dentro do óleo até ficarem fritas')
    print('5. Retire as batatas e coloque em cima do papel toalha')
    print('6. Jogue uma pitada de sal')

    if tempo_fritura.lower() == 'pouco':
        resultado = 'Batata totalmente crua! 😓'
    elif tempo_fritura.lower() == 'ideal':
        resultado = 'Crocante por fora e macia por dentro 😋'
    elif tempo_fritura.lower() == 'muito':
        resultado = 'Xii, ficou queimada e grudando no dente 🤡'
    else:
        resultado = 'Outra hora você frita 🥱'

    return resultado

batata_pronta = fritar_batata('ideal')
print(f'\nEsse é o ponto da batata: {batata_pronta}')
