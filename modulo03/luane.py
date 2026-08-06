'''
Como lavar o cabelo 👧👨‍🦲💇‍♀️

1. Molhe o cabelo

2. Pegue 1 a 3x pumps de shampoo e massageie seu couro cabeludo por 2 minutos e retire,
caso haja necessidade, repita esse processo.

3. Após a retirada do shampoo, pegue a máscara ideal para a necessidade do seu cabelo,
e passe no comprimento até as pontas massageando e sem passar na raiz. Deixe a máscara
agindo conforme informado na embalagem, por exemplo, 3 a 5 minutos. Assim que acabar o tempo de pausa,
pode retirar.

4. Caso a máscara não tenha ação condicionante ou se sentir necessidade, passe o condicionador
no comprimento as pontas e deixe agindo por 2 minutos e retire.

5. Após lavar o cabelo, faça a sua finalização ideal! utilize o leave-in, creme de pentear, óleo.
O que for dá sua escolha.



Extra: Dicas para um(a) careca lavar o couro cabeludo!
Não é só porque é careca que não deve lavar o couro cabeludo

1. Umideça a sua careca

2. Pegue 1x pump de shampoo e massageie se couro cabeludo e enxague

Fazendo isso você ajuda a controlar a oleosidade e mantém o brilho da sua carequinha!
'''


def lavar_cabelo(cabelo_limpo):
    print('\nComo lavar o cabelo - Sistema Simples 👧💇‍♀️')
    print('Manual para lavar o seu cabelo:')
    print('1. Molhe o cabelo')
    print('2. Pegue de 1 a 3x pumps de shampoo')
    print('3. Massageie o couro cabeludo por 2 minutos e retire, caso necessário, repita')
    print('4. Escolha uma máscara, passe no comprimento as pontas')
    print('5. Deixe agir conforme informado na embalagem e retire')
    print('6. Se preferir, passe o condicionador e deixe agir por 2 minutos e retire')
    print('7. Após lavar o cabelo, faça a sua finalização ideal!')
    
    if cabelo_limpo.lower() == 'shampoo':
        resultado = 'Massageie o couro cabeludo por 2 minutos e retire o shampoo'
    elif cabelo_limpo.lower() == 'mascara':
        resultado = 'Enluve o comprimento até as pontas e deixe agir, depois retire'
    elif cabelo_limpo.lower() == 'condicionador':
        resultado  = 'Passe no comprimento as pontas e depois retire'
    else:
        resultado = '+1 dia sem lavar'
        
    return resultado

cabelo_limpo = lavar_cabelo('shampoo')
print(f'\nEsta é a sua etapa: {cabelo_limpo}')