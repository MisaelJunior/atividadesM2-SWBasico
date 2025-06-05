import funções.funcoes as funcoes
import sys
# Função para exibir o menu principal
def menu():
    print('\033[1;36m' + '='*40)
    print('        APLICATIVO DE RESERVAS')
    print('='*40 + '\033[0m\n')
    print('\033[1;34m1.\033[0m Criar usuário')
    print('\033[1;34m2.\033[0m Comprar passagem')
    print('\033[1;34m3.\033[0m Cadastro de Funcionários')
    print('\033[1;34m4.\033[0m Meu Perfil')
    print('\033[1;34m5.\033[0m Minhas reservas')
    print('\033[1;34m6.\033[0m Menu Administrativo')
    print('\033[1;34m7.\033[0m Sair')
# Função para executar o comando selecionado pelo usuário
def executar(comando):
    while True:
        try:
            if comando == 1:
                funcoes.cadastro('usuário', funcoes.usuarios, funcoes.cpf)
                break
            elif comando == 2:
                funcoes.comprarPassagem()
                break
            elif comando == 3:
                funcoes.cadastro('funcionário', funcoes.funcionarios, funcoes.id)
                break
            elif comando == 4:
                funcoes.meuPerfil()
                break
            elif comando == 5:
                funcoes.minhasReservas()
                break
            elif comando == 6:
                funcoes.verificaClientes()
                break
            elif comando == 7:
                sair()
            else: print('\nOpção inválida.')
        except ValueError:
            print('\nOpção inválida.')
# Função para exibir o menu de tipos de transporte
def menuTransportes():
    print('\033[1;36m' + '='*35)
    print('      TIPOS DE TRANSPORTE')
    print('='*35 + '\033[0m')
    print('\033[1;34m1.\033[0m Aéreo')
    print('\033[1;34m2.\033[0m Rodoviário')
    print('\033[1;34m3.\033[0m Ferroviário\n')

# Função para sair do programa  
def sair():
    print('\n' + '\033[1;31m' + '='*40)
    print('{:^40}'.format('Saindo do sistema...'))
    print('='*40 + '\033[0m\n')
    sys.exit()