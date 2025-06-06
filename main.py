# Aplicativo de reservas: agendar, reservar e comprar passagens
#Entidades escolhidas: Passageiro, Viagem, Passagem, Administrador
# Data: 06/06/2025
# Autores: Diego Miranda - turma C - 11251505836
#          Enzo Pereira - turma C - 11251103452
#          Misael da Silva - turma C - 11251102593

#libs
import os
from funções import funcoesMenu

#main
comando = 0

while comando != 7:
    os.system('cls')
    funcoesMenu.menu()
    while True:
        try:
            comando = int(input('\nEscolha uma opção: '))
            if comando in [1, 2, 3, 4, 5, 6, 7]:
                break
            else:
                print('\033[1;31mOpção inválida. Por favor, escolha uma opção válida.\033[0m')
        except ValueError:
            print('\033[1;31mTipo de dado inserido inválido! Por favor, insira um número de 1 a 7.\033[0m')
    funcoesMenu.executar(comando)
    while True:
        try:
            resp = input('\033[1;34mDeseja voltar ao menu principal? s/n\nAo escolher n o programa será encerrado.\033[0m\n')
            if resp.lower() == 's' or resp.lower() == 'sim':
                os.system('cls')
                funcoesMenu.menu()
                comando = int(input('\nEscolha uma opção: '))
                funcoesMenu.executar(comando)
            elif resp.lower() == 'n' or resp.lower() == 'não' or resp.lower() == 'nao':
                comando = 7
                break
            else:
                print('\033[1;31mValor inválido\033[0m')
        except ValueError:
            print('\033[1;31mTipo de dado inserido inválido!\033[0m')
            
    input('\n\033[1;32mSaindo...\033[0m\n\nPressione a tecla Enter para continuar')
        