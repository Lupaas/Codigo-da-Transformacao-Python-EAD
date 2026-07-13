'''
>>Projeto açaíteria:
> PO (Como dono da açaíteria: Quero um sistema de vendas para minha açaíteria,
> para que eu possa organizar os produtos, controlar as vendas e oferecer um atendimento mais eficiente aos clientes.)

> QA (Como cliente: Quero um sistema de vendas para a açaíteria,
> para que eu possa visualizar os produtos, escolher meu açaí, acessar informações da loja e realizar minhas compras de forma rápida e prática.)

> Tech (Como programador: Quero desenvolver um sistema de vendas para uma açaíteria,
> para que eu possa criar um software organizado, funcional e de fácil manutenção, utilizando conceitos básicos de programação em Python.)

> Dev (Como desenvolvedor: Quero implementar um sistema de vendas para a açaíteria,
> para que eu possa desenvolver funcionalidades como cadastro de produtos, listagem, realização de vendas, consulta de localização, contato, redes sociais e feedback dos clientes.)

> UX (Como designer de experiência do usuário: Quero um sistema de vendas para a açaíteria,
> para que eu possa oferecer um menu simples, intuitivo e de fácil navegação, proporcionando uma boa experiência durante a utilização do sistema.)

> IA (Como analista de dados: Quero um sistema de vendas para a açaíteria,
> para que eu possa coletar informações sobre vendas, preferências dos clientes e feedbacks, auxiliando na melhoria dos produtos e do atendimento.)
'''

# Ufa, quebrei a maldição
# print('Olá, Mundo!')



# Inicializando as variáveis para o Produto 1 (Açaí Tradicional)
p1_nome = "Açaí Tradicional"
p1_estoque = 50
p1_preco = 16.00
p1_validade = "12/12/2026 "
p1_descricao = "Açaí tradicional, um clássico que nunca falha."


# Inicializando as variáveis para o Produto 2 (Açaí Premium)
p2_nome = "Açaí Premium"
p2_estoque = 50
p2_preco = 24.00
p2_validade = "12/12/2026"
p2_descricao = "Açaí premium, 500ml de pura tentação!"


# Inicializando as variáveis para o Produto 3 (Açaí Especial)
p3_nome = "Açaí Especial"
p3_estoque = 50
p3_preco = 35.00
p3_validade = "12/12/2026"
p3_descricao = "Açaí especial, um tigelão de 1,5L feito para quem não brinca em serviço!."


# Inicializando as variáveis para o Tamanho do Açaí
tamanho_acai = ("tradicional", "premium", "especial")
topping_acai = ("frutas", "granola", "paçoca", "nutella")


#Iniciando as variáveis para o Histórico de vendas do Açaí
historico_vendas = []



while True:
   print('-' * 48 + '\n')
   print('Bem-vindo ao Sistema de Vendas - Açaíteria!\n')
   print('1 - Cadastrar produto')
   print('2 - Lista de produtos')
   print('3 - Realizar venda')
   print('4 - Cardápio')
   print('5 - Promoções')
   print('6 - Forma de pagamento')
   print('7 - Modos de entrega')
   print('8 - Histórico de vendas')
   print('9 - Contato')
   print('0 - Sair do Sistema')
   print('\n--------------------------------------\n')


   opcao__definida = (input('Digite a opção desejada: '))

   if opcao__definida == '1':
    print('Cadastranto produto...\n')
    if p1_nome == "Açaí Tradicional":
            p1_nome = input('Digite o nome do produto: ')
            p1_estoque = int(input('Digite a quantidade em estoque: '))
            p1_preco = float(input('Digite o preço do produto: '))
            p1_validade = input('Digite a validade do produto: ')    
            p1_descricao = input('Digite a descrição do produto: ')
            print(f'\n🎉 Produto "{p1_nome}" cadastrado na vaga 1!')
    elif p2_nome == "Açaí Premium":
              p2_nome = input('Digite o nome do produto: ')
              p2_estoque = int(input('Digite a quantidade em estoque: '))
              p2_preco = float(input('Digite o preço do produto: '))
              p2_validade = input('Digite a validade do produto: ')    
              p2_descricao = input('Digite a descrição do produto: ')
              print(f'\n🎉 Produto "{p2_nome}" cadastrado na vaga 2!')      
    elif p3_nome == "Açaí Especial":
        p3_nome = input('Digite o nome do produto: ')
        p3_estoque = int(input('Digite a quantidade em estoque: '))
        p3_preco = float(input('Digite o preço do produto: '))
        p3_validade = input('Digite a validade do produto: ')    
        p3_descricao = input('Digite a descrição do produto: ')
        print(f'\n🎉 Produto "{p3_nome}" cadastrado na vaga 3!')

    else:
        print('❌ Sistema cheio! Limite de 3 produtos atingido.')


   elif opcao__definida == '2':
    print('Listando produto...')

    if p1_nome == "Açaí Tradicional" and p2_nome == "Açaí Premium" and p3_nome == "Açaí Especial":
         
        print('Nenhum produto cadastrado no sistema ainda.')

    else:
            # Mostra o Produto 1 se ele existir
            if p1_nome != "Açaí Tradicional":
                print(f"Nome: {p1_nome} | Preço: R$ {p1_preco:.2f} | Estoque: {p1_estoque} unid.")

                print(f"Validade: {p1_validade} | Descrição: {p1_descricao}")

                print('-' * 30)
                
            # Mostra o Produto 2 se ele existir
            if p2_nome != "Açaí Premium":

                print(f"Nome: {p2_nome} | Preço: R$ {p2_preco:.2f} | Estoque: {p2_estoque} unid.")

                print(f"Validade: {p2_validade} | Descrição: {p2_descricao}")

                print('-' * 30)

            # Mostra o Produto 3 se ele existir
            if p3_nome != "Açaí Especial":

                print(f"Nome: {p3_nome} | Preço: R$ {p3_preco:.2f} | Estoque: {p3_estoque} unid.")

                print(f"Validade: {p3_validade} | Descrição: {p3_descricao}")

                print('-' * 30)


   elif opcao__definida == '3':
    print('Realizar venda...')

    if p1_nome == "Açaí Tradicional" and p2_nome == "Açaí Premium" and p3_nome == "Açaí Especial":
            print(f'Não há produtos cadastrados para realizar vendas.')
    else:
            nome_venda = input('Digite o nome do produto que deseja vender: ')
            
            # Testamos o nome digitado contra o Produto 1
            if nome_venda.lower() == p1_nome.lower() and p1_nome != "Açaí Tradicional":
                qtd_venda = int(input(f"Quantas unidades de '{p1_nome}' deseja vender? "))
                if qtd_venda <= p1_estoque:
                    p1_estoque -= qtd_venda
                    total = qtd_venda * p1_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p1_nome}: {p1_estoque} unidades.')

                    venda_atual = {
                        "produto": p1_nome,
                        "quantidade": qtd_venda,
                        "total": total
                     }
                    
                    historico_vendas.append(venda_atual)
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p1_estoque}.')
            
            # Testamos contra o Produto 2
            elif nome_venda.lower() == p2_nome.lower() and p2_nome != "Açaí Premium":
                qtd_venda = int(input(f"Quantas unidades de '{p2_nome}' deseja vender? "))
                if qtd_venda <= p2_estoque:
                    p2_estoque -= qtd_venda
                    total = qtd_venda * p2_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p2_nome}: {p2_estoque} unidades.')

                    venda_atual = {
                        "produto": p2_nome,
                        "quantidade": qtd_venda,
                        "total": total
                     }
                    
                    historico_vendas.append(venda_atual)
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p2_estoque}.')
                    
            # Testamos contra o Produto 3
            elif nome_venda.lower() == p3_nome.lower() and p3_nome != "Açaí Especial":
                qtd_venda = int(input(f"Quantas unidades de '{p3_nome}' deseja vender? "))
                if qtd_venda <= p3_estoque:
                    p3_estoque -= qtd_venda
                    total = qtd_venda * p3_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p3_nome}: {p3_estoque} unidades.')

                    venda_atual = {
                        "produto": p3_nome,
                        "quantidade": qtd_venda,
                        "total": total
                     }
                    
                    historico_vendas.append(venda_atual)
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p3_estoque}.')
            
            else:
                print('👀 Erro: Produto não encontrado!')


   elif opcao__definida == '4':
    print('Bem vindo ao nosso Cardápio! \n')
    print(tamanho_acai)

    selecionar_tam = input('\n''Digite o tamanho do açaí que você quer: ')

    if selecionar_tam == 'tradicional':
     print(f'✅ Anotado! Você selecionou: {p1_nome} 300ml''\n')

    elif selecionar_tam == 'premium':
     print(f'✅ Anotado! Você selecionou: {p2_nome} 500ml''\n')

    elif selecionar_tam  == 'especial':
     print(f'✅ Anotado! Você selecionou: {p3_nome} 1,5L''\n')

    else:
     print('Desculpe, nós não temos essa opção no cardápio. Tente novamente')

    print('Abaixo, está a nossa lista de adicionais:')
    print(topping_acai)
    adicional_acai = input('\n''Digite o topping que você quer adicionar: ')

    if adicional_acai == 'frutas':
     print(f'✅ Anotado! Você selecionou: {adicional_acai}')

    elif adicional_acai == 'granola':
     print(f'✅ Anotado! Você selecionou: {adicional_acai}')

    elif adicional_acai == 'paçoca':
     print(f'✅ Anotado! Você selecionou: {adicional_acai}')

    elif adicional_acai == 'nutella':
     print(f'✅ Anotado! Você selecionou: {adicional_acai}')

    else:
     print('Desculpe, nós não temos essa opção no cardápio. Tente novamente')


    if selecionar_tam in (f'{tamanho_acai}') and adicional_acai in (f'{topping_acai}'):
        print('\n'f'Esse é o resumo do seu pedido: Açaí {selecionar_tam} com {adicional_acai}!')

   elif opcao__definida == '5':
    print('Promoções')

   elif opcao__definida == 6:
    print('Formas de Pagamento')

   elif opcao__definida == 7:
    print('Modos de Entrega')

   elif opcao__definida == '8':
    print('\n''Bem-vindo ao Histórico de vendas!''\n')
    
    if historico_vendas == []:
        print('Humm, parece que não foi feita nenhuma venda ainda. Tente novamente!')
    
    else:
        for venda in historico_vendas:
            print(f"Produto: {venda['produto']}")
            print(f"Quantidade: {venda['quantidade']}")
            print(f"Total: R$ {venda['total']:.2f}"'\n')
            print('-' * 25)

   elif opcao__definida == 9:
    print('Contato')

   elif opcao__definida == '0':
      print('Finalizando o programa...')
      break

   else:
    print('Humm, Algo deu errado. Tente Novamente!')
