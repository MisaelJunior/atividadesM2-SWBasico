# Aplicativo de reservas: agendar consultas, reservas de hotel ou passagens
# Data: 06/06/2025
# Autores: Diego Miranda - turma C - 11251505836
#          Enzo Pereira - turma C - 11251103452
#          Misael da Silva - turma C - 11251102593

#libs
import os
import funcoes

#main
comando = 0

while comando != 6:
    os.system('cls')
    funcoes.menu()
    comando = int(input('\nEscolha uma opção: '))
    funcoes.executar(comando)
    while True:
        try:
            resp = input('Deseja voltar ao menu principal? s/n\n')
            if resp.lower() == 's' or resp.lower() == 'sim':
                os.system('cls')
                funcoes.menu()
                comando = int(input('\nEscolha uma opção: '))
                funcoes.executar(comando)
            elif resp.lower() == 'n' or resp.lower() == 'não' or resp.lower() == 'nao':
                comando = 6
                break
            else:
                print('Valor inválido')
        except ValueError:
            print('Tipo de dado inserido inválido!')
            
    input('\nPressione qualquer tecla.')
    