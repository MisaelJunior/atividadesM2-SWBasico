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
    input('\nPressione qualquer tecla.')