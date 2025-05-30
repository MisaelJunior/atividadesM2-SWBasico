#EXERCÍCIO 3

import os

jogador_1 = input('Jogador(a) 1, digite seu nome: ')

while True:
    num_1 = int(input(f'{jogador_1}, escolha um número entre 1 e 10: '))
    if num_1<1 or num_1>10:
        print('\nOpção inválida, tente novamente.\n')
    else:
        break

os.system('cls')

jogador_2 = input('\nJogador(a) 2, digite seu nome: ')
tentativa = int(input(f'\nQual foi o número escolhido pelo(a) {jogador_1}? '))

while tentativa <1 or tentativa >10:
    print('\nOpção inválida, escolha um número entre 1 e 10.\n')
    tentativa = int(input(f'Qual foi o número escolhido pelo(a) {jogador_1}? '))

tentativas = 1

while tentativa != num_1:
    print('\nVocê errou!!! Tente novamente.')
    tentativa = int(input(f'\nQual foi o número escolhido pelo(a) {jogador_1}? '))
    
    while tentativa <1 or tentativa >10:
        print('\nOpção inválida, escolha um número entre 1 e 10.\n')
        tentativa = int(input(f'Qual foi o número escolhido pelo(a) {jogador_1}? '))

    tentativas += 1

else:
    print(f'\nParabéns, você acertou o número escolhido pelo(a) {jogador_1} em {tentativas} tentativas!\n')