#EXERCÍCIO 2

import os

total = []
itens = []
valores = []
quantidade = []
precos =[]


cardapio = {
    100: ('Cachorro Quente', 3.50),
    101: ('Bauru Simples  ', 3.80),
    102: ('Bauru com Ovo  ', 4.50),
    103: ('Hamburger      ', 4.70),
    104: ('Cheeseburger   ', 5.30),
    105: ('Refrigerante   ', 4.00)
}
def listaDeCompras():
    print('\n--------------Lista de Compras--------------\nQuantidade de produtos: ', len(itens))
    print('     ITEM       | QTD | VALOR(un) |  TOTAL\n--------------------------------------------')
    for i in range(len(itens)):
        print(f'{itens[i]} |  {quantidade[i]}  x  R$ {precos[i]}   | R$ {valores[i]:.2f}')
        if i+1 == len(itens):
            print(f'                                   Valor total = R$ {sum(total):.2f}')
    

def menu():
    print('Menu de lanches\n')
    print('100 - Cachorro Quente - R$ 3,50')
    print('101 - Bauru Simples - R$ 3,80')
    print('102 - Bauru c/Ovo - R$ 4,50')
    print('103 - Hamburger - R$ 4,70')
    print('104 - Cheeseburger - R$ 5,30')
    print('105 - Refrigerante - R$ 4,00')
    print('1 - Carrinho')
    print('0 - Sair/Cancelar\n')

def opcoes():
    while (True):
        resposta = ''
        
        while (True):
            try:
                opcao = int(input('\nDigite o código do lanche: '))
                break  
            except ValueError:
                print('Opção inválida! Digite um número inteiro.')


        if opcao in cardapio:
            nome, preco = cardapio[opcao]

            while True:
                try:
                    qntd = int(input(f'\nQuantos {nome} irá levar? '))
                    if qntd < 0:
                        print('Digite um número maior ou igual a 0.')
                    else:
                        break
                except ValueError:
                    print('Opção inválida! Digite um número inteiro.')

            valor = qntd * preco
            if qntd != 0:
                total.append(valor)
                itens.append(nome)
                valores.append(valor)
                quantidade.append(qntd)
                precos.append(preco)
                print(f'\nO valor a ser pago pelo(s) {nome} é de R$ {valor:.2f}.\nSubtotal: R$ {sum(total):.2f}')
        elif opcao == 1:
            listaDeCompras()   
        elif opcao == 0:
            print ('Sair.')
            break
        else:
            print ('Código inválido.')
        
            opcoes()

        if opcao != 0:
            while not ((resposta == 's') or (resposta == 'sim') or (resposta == 'n') or (resposta == 'não')):
                resposta = input('\nDeseja algo mais? s/n\n')
                

        if resposta == 'n' or resposta == 'não':
            os.system('cls')
            listaDeCompras()
            print(f'\nO valor total é de R$ {sum(total):.2f}.\nDirija-se ao caixa para efetuar o pagamento.')
            break
        else:
            os.system('cls')
            menu()

opcao = ''
while opcao != 0:
    os.system('cls')
    menu()
    
    opcoes()

    opcao = 0

    input('\nPressione qualquer tecla.')