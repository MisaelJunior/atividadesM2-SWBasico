from datetime import datetime
import os
import sys
import secrets
import random
from funções import funcoesMenu
from funções import funcoesMenu
# Variáveis globais
id = ''
cpf = ''

usuarios = {"470.331.668-42":{
    "nome": 'Misael',
    "cpf": '470.331.668-42',
    "telefone": '11998473130',
    "email": 'misael@umc.br',
    "senha": '1234',
    "viagens":[]
}}

funcionarios = {"11251102593":{
    "id": '11251102593',
    "nome": 'Misael',
    "cpf": '470.331.668-42',
    "telefone": '11998473130',
    "email": 'misael@umc.br',
    "senha": '1234',
    
}}

chaveMestra = ['1234']

destinos_aereo = ["NOVA YORK", "PARIS", "LONDRES", "TÓQUIO", "DUBAI", "ROMA", "BARCELONA", "BANGCOC", "SYDNEY", "HONG KONG", "SÃO PAULO", "RIO DE JANEIRO", "FORTALEZA", "SALVADOR", "MANAUS", "PORTO ALEGRE", "BELO HORIZONTE"]
destinos_rodoviario = ["RIO BRANCO", "MACEIÓ", "MACAPÁ", "MANAUS", "SALVADOR", "FORTALEZA", "BRASÍLIA", "VITÓRIA", "GOIÂNIA", "SÃO LUÍS","CUIABÁ", "CAMPO GRANDE", "BELO HORIZONTE", "BELÉM", "JOÃO PESSOA", "CURITIBA", "RECIFE", "TERESINA", "RIO DE JANEIRO", "NATAL", "PORTO ALEGRE", "PORTO VELHO", "BOA VISTA", "FLORIANÓPOLIS", "SÃO PAULO", "ARACAJU", "PALMAS"]
destinos_ferroviario = ["SÃO PAULO", "RIO DE JANEIRO", "BELO HORIZONTE", "CURITIBA", "SALVADOR", "FORTALEZA", "RECIFE", "PORTO ALEGRE","BRASÍLIA", "MANAUS", "CAMPINAS", "GOIÂNIA", "NATAL", "FLORIANÓPOLIS", "BELÉM", "VITÓRIA", "SÃO LUÍS", "JOÃO PESSOA", "MACEIÓ", "CUIABÁ"]

# Função para realizar o cadastro de usuários e funcionários
def cadastro(pessoa, cargo, identificador):
    print(f'\n\033[1;36m{"="*40}\n      NOVO {pessoa.upper()}\n{"="*40}\033[0m')
    cpf = input(f'\nDigite o CPF do {pessoa} (Utilize o formato 123.456.789-00): ')
    
    if cargo == funcionarios:
        mestra = input('\nÉ necessário entrar com a chave mestra para cadastrar um novo funcionário: ')
        if mestra in chaveMestra:
            print(f'\n\033[1;36m{"-"*40}\n      CADASTRO DE FUNCIONÁRIO\n{"-"*40}\033[0m')
            identificador = input('\nDigite o ID do funcionário: ') 
            if identificador in funcionarios:
                print('\n\033[91m[!] ID já cadastrado.\033[0m\n')
            else:
                nome = input(f'\nDigite o nome do {pessoa}: ')
                
                tel = input('Telefone: ')
                email = input('Email: ')
                while True:
                    chave = input('Crie uma chave de acesso: ')
                    if len(chave) < 8:
                        print('\n\033[91m[!] A chave de acesso deve possuir pelo menos 8 caracteres.\033[0m\n')
                    else:
                        os.system('cls')
                        print('\n\033[92m' + '-'*40)
                        print('Chave de acesso cadastrada com sucesso!')
                        print('-'*40 + '\033[0m')
                        cargo[identificador] = {
                                "id": id,
                                "nome": nome,
                                "cpf": cpf,
                                "telefone": tel,
                                "email": email,
                                "chave de acesso": chave,
                            }
                        print('\n\033[92m' + '='*40)
                        print('Funcionário cadastrado com sucesso!')
                        print('='*40 + '\033[0m\n')
                        break
        else:
            print('\n\033[91m[!] Chave mestra não confere.\033[0m\n')
            funcoesMenu.sair()
    else:
        if cpf in cargo:
            print('\n\033[91m[!] CPF já cadastrado.\033[0m\n')
        else:
            nome = input(f'\nDigite o nome do {pessoa}: ')
            tel = input('Telefone: ')
            email = input('Email: ')
            while True:
                senha = input('Crie uma senha: ')
                if len(senha) < 8:
                    print('\n\033[91m[!] A senha deve possuir pelo menos 8 caracteres.\033[0m\n')
                else:
                    os.system('cls')
                    print('\n\033[92m' + '-'*40)
                    print('Senha cadastrada com sucesso!')
                    print('-'*40 + '\033[0m')
                    cargo[identificador] = {
                        "nome": nome,
                        "cpf": cpf,
                        "telefone": tel,
                        "email": email,
                        "senha": senha,
                        "viagens": []
                    }
                    print('\n\033[92m' + '='*40)
                    print(f'{pessoa.capitalize()} cadastrado com sucesso!')
                    print('='*40 + '\033[0m\n')
                    break
# Função para consultar usuário por CPF                
def consultaUsuario(cpf):
    if cpf in usuarios:
        print('\n' + '\033[1;36m' + '-'*80)
        print('{:^80}'.format('BUSCA DE USUÁRIOS'))
        print('-'*80 + '\033[0m')
        print(f'\033[1;37mUsuário:   \033[0m{usuarios[cpf]["nome"]}')
        print(f'\033[1;37mCPF:       \033[0m{usuarios[cpf]["cpf"]}')
        print(f'\033[1;37mTelefone:  \033[0m{usuarios[cpf]["telefone"]}')
        print(f'\033[1;37mEmail:     \033[0m{usuarios[cpf]["email"]}')
        print('\033[1;36m' + '-'*80 + '\033[0m')
        print('{:^80}'.format('VIAGENS'))
        print('\033[1;36m' + '-'*80 + '\033[0m')
        if usuarios[cpf]["viagens"]:
            for i in usuarios[cpf]["viagens"]:
                print(f' \033[1;36mIDA  \033[0m--- Partida: {i["partida"]}, Destino: {i["destino"]}, Data: {i["data de ida"]}')
                print(f' \033[1;36mVOLTA\033[0m --- Partida: {i["destino"]}, Destino: {i["partida"]}, Data: {i["data de volta"]}')
            print('\033[92m[✔] Consulta realizada com sucesso!\033[0m')
        else:
            print('\033[91m[!] Nenhuma viagem cadastrada para este usuário.\033[0m')
        print('\033[1;36m' + '-'*80 + '\033[0m')
    else:
        print('\033[91m[!] CPF não cadastrado!\033[0m')
        cpfNaoCadastrado()
# Função para validar a senha ou chave de acesso
def validarSenha(identificador, cargo):
    tentativa = 1
    while True:
        if cargo == funcionarios:
            validacao = input('\033[1;34mEntre com a Chave de acesso:\033[0m ')
        elif cargo == usuarios:
            validacao = input('\033[1;34mEntre com a senha:\033[0m ')
            
        if validacao == cargo[identificador]["senha"]:
            print('\033[92m[✔] Acesso autorizado!\033[0m')
            break
        else:
            if cargo == funcionarios:
                print(f'\033[91mChave de acesso Incorreta\nTentativa {tentativa}/3\033[0m')
            else:
                print(f'\033[91mSenha Incorreta\nTentativa {tentativa}/3\033[0m')
            tentativa += 1
            if tentativa > 3:
                print('\033[91m[!] Número máximo de tentativas excedido. Encerrando...\033[0m')
                sys.exit()
# Função para comprar passagem       
def comprarPassagem():
    print('\n' + '\033[1;34m' + '='*40)
    print(' ' * 10 + 'COMPRAR PASSAGEM')
    print('='*40 + '\033[0m')
    cpf = input('\nDigite o CPF do usuário (Utilize o formato 123.456.789-00): ')
    if cpf not in usuarios:
        cpfNaoCadastrado()

    validarSenha(cpf, usuarios)
    funcoesMenu.menuTransportes()
    while True:
        try:
            tipo_de_transporte = int(input('\nSelecione um tipo de transporte\n 1 - Aéreo\n 2 - Rodoviário\n 3 - Ferroviário\nOpção: '))
            if tipo_de_transporte not in [1, 2, 3]:
                print('\033[91m\n[!] Opção inválida! Digite um número de 1 a 3.\033[0m\n')
            else:
                break
        except ValueError:
            print('\033[91m\n[!] Opção inválida! Digite um número de 1 a 3.\033[0m\n')

    if tipo_de_transporte == 1:
        print('\n' + '\033[1;34m' + '-'*40)
        print('Tipo de transporte escolhido: Aéreo')
        print('-'*40 + '\033[0m')
        partida_lista = destinos_rodoviario
        destino_lista = destinos_aereo
    elif tipo_de_transporte == 2:
        print('\n' + '\033[1;32m' + '-'*40)
        print('Tipo de transporte escolhido: Rodoviário')
        print('-'*40 + '\033[0m')
        partida_lista = destinos_rodoviario
        destino_lista = destinos_rodoviario
    else:
        print('\n' + '\033[1;33m' + '-'*40)
        print('Tipo de transporte escolhido: Ferroviário')
        print('-'*40 + '\033[0m')
        partida_lista = destinos_ferroviario
        destino_lista = destinos_ferroviario

    # Escolha do local de partida
    while True:
        ver_partidas = input('\nGostaria de ver todos os locais de partida disponíveis? (s/n): ').strip().lower()
        if ver_partidas in ['s', 'sim']:
            print('\n' + '\033[1;36m' + '-'*40)
            print('Locais de partida disponíveis:')
            print('-'*40 + '\033[0m')
            for i in partida_lista:
                print(f' - {i}')
            print('\033[1;36m' + '-'*40 + '\033[0m')
            break
        elif ver_partidas in ['n', 'nao', 'não']:
            break
        else:
            print('\033[91m\n[!] Opção inválida!\033[0m\n')

    a = input('\nEscolha o local de partida: ').strip().upper()
    while a not in partida_lista:
        print('\033[91m\n[!] Local de partida não disponível ou incorreto!\033[0m\n')
        a = input('Escolha o local de partida: ').strip().upper()
    print(f'\n\033[92m[✔] Local de partida definido: {a}\033[0m')

    # Escolha do local de destino
    while True:
        ver_destinos = input('\nGostaria de ver todos os locais de destino disponíveis? (s/n): ').strip().lower()
        if ver_destinos in ['s', 'sim']:
            print('\n' + '\033[1;36m' + '-'*40)
            print('Locais de destino disponíveis:')
            print('-'*40 + '\033[0m')
            for i in destino_lista:
                print(f' - {i}')
            print('\033[1;36m' + '-'*40 + '\033[0m')
            break
        elif ver_destinos in ['n', 'nao', 'não']:
            break
        else:
            print('\033[91m\n[!] Opção inválida!\033[0m\n')

    b = input('\nEscolha o local de destino: ').strip().upper()
    while b not in destino_lista:
        print('\033[91m\n[!] Local de destino não disponível ou incorreto!\033[0m\n')
        b = input('Escolha o local de destino: ').strip().upper()
    print(f'\n\033[92m[✔] Local de destino definido: {b}\033[0m')

    # Reservar datas
    print('\n' + '\033[1;35m' + '-'*40)
    print('Reserva de datas')
    print('-'*40 + '\033[0m')
    data_ida, data_volta = reservarData()

    usuarios[cpf]["viagens"].append({
        "partida": a,
        "destino": b,
        "data de ida": str(data_ida),
        "data de volta": str(data_volta),
    })

    print('\n' + '\033[92m' + '='*40)
    print('Passagem registrada com sucesso!')
    print('='*40 + '\033[0m\n')
# Função para reservar datas de ida e volta        
def reservarData():
    while True:
        while True:
            try:
                data_str = input("Insira data de ida no formato AAAA-MM-DD: ")
                data1 = datetime.strptime(data_str, "%Y-%m-%d")
                break 
            except ValueError:
                print('\033[91m[!] Data inválida. Por favor, insira no formato AAAA-MM-DD.\033[0m')
                
        while True:
            try:
                data_str = input("Insira data de volta no formato AAAA-MM-DD: ")
                data2 = datetime.strptime(data_str, "%Y-%m-%d")
                if data2 >= data1:
                    break
                else:
                    print('\033[91m[!] A data de volta NÃO pode ser ANTERIOR a data de ida.\033[0m') 
            except ValueError:
                print('\033[91m[!] Data inválida. Por favor, insira no formato AAAA-MM-DD.\033[0m')
        
        print('\033[92m[✔] Datas {} - {} reservadas com sucesso!\033[0m'.format(data1.date(), data2.date()))
        return data1.date(), data2.date()
# Função para exibir o perfil do usuário
def perfilUsuario():
    print('\n' + '='*80)
    print('{:^80}'.format('MEU PERFIL'))
    print('='*80)
    print('\033[1;34mLOGIN\033[0m')
    cpf = input('Entre com o CPF (Utilize o formato 123.456.789-00): ')
    if cpf in usuarios:
        validarSenha(cpf, usuarios)
        os.system('cls')
        print('\n' + '='*80)
        print('{:^80}'.format('MEU PERFIL'))
        print('='*80)
        print(f'\033[1;37mNome:      \033[0m{usuarios[cpf]["nome"]}')
        print(f'\033[1;37mCPF:       \033[0m{usuarios[cpf]["cpf"]}')
        print(f'\033[1;37mTelefone:  \033[0m{usuarios[cpf]["telefone"]}')
        print(f'\033[1;37mEmail:     \033[0m{usuarios[cpf]["email"]}')
        print('-'*80)
        print('{:^80}'.format('MINHAS PASSAGENS'))
        print('-'*80)
        if usuarios[cpf]["viagens"]:
            for j in usuarios[cpf]["viagens"]:
                print(f' \033[1;36mIDA  \033[0m--- Partida: {j["partida"]}, Destino: {j["destino"]}, Data: {j["data de ida"]}')
                print(f' \033[1;36mVOLTA\033[0m --- Partida: {j["destino"]}, Destino: {j["partida"]}, Data: {j["data de volta"]}')
        else:
            print('\033[91m[!] Nenhuma passagem cadastrada.\033[0m')
        print('='*80)
    else:
        cpfNaoCadastrado()
# Função para exibir o perfil do usuário e permitir alterações
def meuPerfil():
    perfilUsuario()
    cpf = input('Entre com o CPF para ver as opções (Utilize o formato 123.456.789-00): ')
    if cpf in usuarios:    
        while True:
            try:
                print('\n' + '='*60)
                print(' ' * 20 + 'PERFIL DO USUÁRIO')
                print('='*60)
                print('1. Alterar Nome')
                print('2. Alterar Telefone')
                print('3. Alterar Email')
                print('4. Alterar Senha')
                print('5. Recadastro')
                print('6. Imprimir Passagem')
                print('7. Excluir Perfil')
                print('8. Voltar')
                print('-'*60)
                    
                while True:
                    try:
                        escolha = int(input('Selecione uma ação: '))
                        if escolha < 1 or escolha > 8:
                            print('\033[91m[!] Opção Inválida!\033[0m')
                        else:
                            print(f'\033[92m[✔] Opção selecionada: {escolha}\033[0m')
                            break
                    except ValueError:
                        print('\033[91m[!] Tipo de dado inserido inválido!\033[0m')
                
                if escolha == 1:
                    nome = input('Insira o novo nome: ')
                    usuarios[cpf]["nome"] = nome
                    print('\033[92m[✔] Nome alterado com sucesso!\033[0m')
                    input('Pressione a tecla Enter para continuar')
                    os.system('cls')
                elif escolha == 2:
                    telefone = input('Insira o novo número de telefone: ')
                    usuarios[cpf]["telefone"] = telefone
                    print('\033[92m[✔] Telefone alterado com sucesso!\033[0m')
                    input('Pressione a tecla Enter para continuar')
                    os.system('cls')
                elif escolha == 3:
                    email = input('Insira o novo email: ')
                    usuarios[cpf]["email"] = email
                    print('\033[92m[✔] Email alterado com sucesso!\033[0m')
                    input('Pressione a tecla Enter para continuar')
                    os.system('cls')
                elif escolha == 4:
                    senha_atual = input('Entre com a senha atual: ')
                    if senha_atual == usuarios[cpf]["senha"]:
                        while True:
                            nova_senha = input('Nova senha: ')
                            if len(nova_senha) < 8:
                                print('\033[91m[!] A senha deve possuir pelo menos 8 caracteres\033[0m')
                            else:
                                os.system('cls')
                                print('\033[92m[✔] Senha cadastrada com sucesso\033[0m')
                                break 
                        usuarios[cpf]["senha"] = nova_senha
                        print('\033[92m[✔] Senha alterada com sucesso!\033[0m')
                        input('Pressione a tecla Enter para continuar')
                    os.system('cls')
                elif escolha == 5:
                    print('\n' + '-'*60)
                    print('Ao confirmar seu cadastro será excluído e você será direcionado(a) à criação de um novo cadastro')
                    print('-'*60)
                    while True:
                        try:
                            r = input('Deseja excluir o cadastro atual e criar um novo usuário? (s/n): ')
                            if r.lower() == 's' or r.lower() == 'sim' :
                                cpf = input('Excluindo cadastro...\nConfirme o seu CPF: ')
                                validarSenha(cpf, usuarios)
                                del usuarios[cpf]
                                print('\033[92m[✔] Usuário excluído com sucesso!\033[0m')
                                cadastro('usuário', usuarios, cpf)
                                break
                            elif r.lower() == 'n' or r.lower() == 'nao' or r.lower() == 'não':
                                break
                            else:
                                print('\033[91m[!] Opção inválida!\033[0m')
                        except ValueError:
                            print('\033[91m[!] O tipo de dado inserido é inválido, tente novamente!\033[0m')
                    input('Pressione a tecla Enter para continuar')
                    os.system('cls')
                elif escolha == 6:
                    if usuarios[cpf]["viagens"]:
                        codigo = secrets.token_hex(20)
                        print('\n' + '-'*60)
                        print(f'Código para o pagamento: \033[1;36m{codigo}\033[0m')
                        print('A passagem só será validada caso o pagamento seja confirmado.')
                        print('-'*60)
                        gerarPassagem(cpf)
                    else:
                        print('\033[91m[!] Nenhuma viagem cadastrada. Não é possível gerar código.\033[0m')
                    input('Pressione a tecla Enter para continuar')
                    os.system('cls')
                elif escolha == 7:
                    print('\n' + '-'*60)
                    print('Ao confirmar seu cadastro será excluído')
                    print('-'*60)
                    while True:
                        try:
                            r = input('Deseja excluir o cadastro atual? (s/n):\nAo confirmar seu cadastro será excluído: ')
                            if r.lower() == 's' or r.lower() == 'sim' :
                                cpf = input('Excluindo cadastro...\nConfirme o seu CPF: ')
                                validarSenha(cpf, usuarios)
                                del usuarios[cpf]
                                print('\033[92m[✔] Usuário excluído com sucesso!\033[0m')
                                break
                            elif r.lower() == 'n' or r.lower() == 'nao' or r.lower() == 'não':
                                break
                            else:
                                print('\033[91m[!] Opção inválida!\033[0m')
                        except ValueError:
                            print('\033[91m[!] O tipo de dado inserido é inválido, tente novamente!\033[0m')
                    input('Pressione a tecla Enter para continuar')
                else:
                    print('\033[91m[!] Retornando ao menu anterior.\033[0m')
                    break
            except ValueError:
                print('\033[91m[!] Tipo de dado inserido inválido!\033[0m')
    else:
        cpfNaoCadastrado()   
# Função para exibir as reservas do usuário      
def minhasReservas():
    cpf = input('Entre com o CPF (Utilize o formato 123.456.789-00): ')
    if cpf in usuarios:
        validarSenha(cpf, usuarios)
        os.system('cls')
        print('-' *80)
        print(f'\nNome: {usuarios[cpf]["nome"]}')
        print('\n-------------------------------Minhas Passagens--------------------------------')
        print(f'Viagens:')
        for j in usuarios[cpf]["viagens"]:
                print(f' IDA  --- Partida: {j["partida"]}, Destino: {j["destino"]}, Data: {j["data de ida"]}')
                print(f'VOLTA --- Partida: {j["destino"]}, Destino: {j["partida"]}, Data: {j["data de volta"]}')
# Função para verificar se o usuário é um funcionário e acessar o menu administrativo
def verificaClientes():
    id = input('\n' + '='*50 + '\nFuncionário, insira seu ID: ')
    if id in funcionarios:
        validarSenha(id, funcionarios)
        os.system('cls')
        print('\n' + '='*50)
        print(' ' * 10 + 'Bem-vindo(a) ao Menu Administrativo')
        print('='*50)
        while True:
            os.system('cls')
            print('\n' + '='*50)
            print(' ' * 10 + 'MENU ADMINISTRATIVO')
            print('='*50)
            print('1. Cadastrar Usuário')
            print('2. Consultar usuário')
            print('3. Alterar dados de usuário')
            print('4. Consultar lista de usuários')
            print('5. Consultar lista de funcionários')
            print('6. Excluir usuário')
            print('7. Excluir Funcionário')
            print('8. Voltar')
            print('-'*50)
            acao = int(input('Que ação deseja realizar? '))
            try:
                if acao == 1:
                    print('\n' + '-'*50)
                    cadastro('usuário', usuarios, cpf)
                    break
                elif acao == 2:
                    print('\n' + '-'*50)
                    cpf = input('Insira o CPF para a Busca: ')
                    consultaUsuario(cpf)
                    break
                elif acao == 3:
                    print('\n' + '-'*50)
                    cpf = input('Insira o CPF para a Busca: ')
                    consultaUsuario(cpf)
                    while True:
                        try:
                            print('\n' + '='*50)
                            print(' ' * 10 + 'Perfil do usuário')
                            print('='*50)
                            print('1. Nome')
                            print('2. Telefone')
                            print('3. Email')
                            print('4. Recadastro')
                            print('5. Voltar')
                            print('-'*50)
                            while True:
                                try:
                                    escolha = int(input('Selecione qual dado deseja alterar: '))
                                    if escolha < 1 or escolha > 5:
                                        print('\033[91m\n[!] Opção Inválida!\033[0m')
                                    else:
                                        print(f'\n[✔] Opção selecionada: {escolha}')
                                        break
                                except ValueError:
                                    print('\033[91m\n[!] Tipo de dado inserido inválido!\033[0m')

                            if escolha == 1:
                                nome = input('\nInsira o novo nome: ')
                                usuarios[cpf]["nome"] = nome
                                print('\n[✔] Nome alterado com sucesso!')
                                input('\nPressione a tecla Enter para continuar')
                                break
                            elif escolha == 2:
                                telefone = input('\nInsira o novo número de telefone: ')
                                usuarios[cpf]["telefone"] = telefone
                                print('\n[✔] Telefone alterado com sucesso!')
                                input('\nPressione a tecla Enter para continuar')
                                break
                            elif escolha == 3:
                                email = input('\nInsira o novo email: ')
                                usuarios[cpf]["email"] = email
                                print('\n[✔] Email alterado com sucesso!')
                                input('\nPressione a tecla Enter para continuar')
                                break
                            elif escolha == 4:
                                print('\n' + '-'*50)
                                print('Ao confirmar seu cadastro será excluído e você será direcionado(a) à criação de um novo cadastro')
                                while True:
                                    try:
                                        r = input('\nDeseja excluir o cadastro atual e criar um novo usuário? (s/n): ')
                                        if r.lower() == 's' or r.lower() == 'sim' :
                                            cpf = input('\nExcluindo cadastro...\nConfirme o seu CPF: ')
                                            validarSenha(cpf, usuarios)
                                            del usuarios[cpf]
                                            print('\n[✔] Usuário excluído com sucesso!')
                                            cadastro('usuário', usuarios, cpf)
                                            break
                                        elif r.lower() == 'n' or r.lower() == 'nao' or r.lower() == 'não':
                                            break
                                        else:
                                            print('\033[91m\n[!] Opção inválida!\033[0m')
                                    except ValueError:
                                        print('\033[91m\n[!] O tipo de dado inserido é inválido, tente novamente!\033[0m')
                                input('\nPressione a tecla Enter para continuar')
                                break
                            else:
                                print('\033[91m\n[!] Retornando ao menu anterior.\033[0m')
                                break
                        except ValueError:
                            print('\033[91m\n[!] O tipo de dado inserido é inválido, tente novamente!\033[0m')
                            input('\nPressione a tecla Enter para continuar')
                elif acao == 4:
                    print('\n' + '='*50)
                    print(' ' * 10 + 'Lista de usuários')
                    print('='*50)
                    print(f'Quantidade de usuários: {len(usuarios)}')
                    for i in usuarios:
                        print('\n' + '-'*50)
                        print(f'Usuário:   {usuarios[i]["nome"]}')
                        print(f'CPF:       {usuarios[i]["cpf"]}')
                        print(f'Telefone:  {usuarios[i]["telefone"]}')
                        print(f'Email:     {usuarios[i]["email"]}')
                        print('Viagens:')
                        for j in usuarios[i]["viagens"]:
                            print(f'  IDA   --- Partida: {j["partida"]}, Destino: {j["destino"]}, Data: {j["data de ida"]}')
                            print(f'  VOLTA --- Partida: {j["destino"]}, Destino: {j["partida"]}, Data: {j["data de volta"]}')
                    print('\n' + '='*50)
                    break
                elif acao == 5:
                    print('\n' + '='*50)
                    print(' ' * 10 + 'Lista de Funcionários')
                    print('='*50)
                    print(f'Quantidade de Funcionários: {len(funcionarios)}')
                    for i in funcionarios:
                        print('\n' + '-'*50)
                        print(f'Nome:      {funcionarios[i]["nome"]}')
                        print(f'ID:        {funcionarios[i]["id"]}')
                        print(f'CPF:       {funcionarios[i]["cpf"]}')
                        print(f'Telefone:  {funcionarios[i]["telefone"]}')
                        print(f'Email:     {funcionarios[i]["email"]}')
                        
                    print('\n' + '='*50)
                    break
                elif acao == 6:
                    excluirPessoa(usuarios, cpf)
                elif acao == 7:
                    excluirPessoa(funcionarios, id)
                elif acao == 8:
                    print('\033[91m\n[!] Retornando ao menu anterior.\033[0m')
                    break
                else:
                    print('\033[91m\n[!] Opção inválida.\033[0m')
            except ValueError:
                print('\033[91m\n[!] Opção inválida.\033[0m')
        input('\nPressione a tecla Enter para continuar')

def excluirPessoa(cargo, identificador):
    if cargo == funcionarios:
        mestra = input('\nÉ necessário entrar com a chave mestra para excluir um funcionário: ')
        if mestra in chaveMestra:
            print(f'\n\033[1;36m{"-"*40}\n      EXCLUSÃO DE FUNCIONÁRIO\n{"-"*40}\033[0m')
            identificador = input('\nDigite o ID do funcionário: ')
            if not identificador in funcionarios:
                print('\n\033[91m[!] ID não encontrado.\033[0m\n')
            else:
                del funcionarios[identificador]
                print('\n[✔] Funcionário excluído com sucesso!')
        else:
            print('\n\033[91m[!] Chave mestra não confere.\033[0m\n')
            funcoesMenu.sair()
    else:
        cpf = input(f'\nDigite o CPF do usuário a ser excluído (Utilize o formato 123.456.789-00): ')
        if not cpf in cargo:
            print('\n\033[91m[!] CPF não encontrado.\033[0m\n')
        else:
            del usuarios[cpf]
            print('\n[✔] Usuário excluído com sucesso!')

# Função para gerar o valor da passagem com base no tipo de transporte e datas
def gerarValor(viagem, tipo_transporte):
    
    data_ida = datetime.strptime(viagem["data de ida"], "%Y-%m-%d")
    data_volta = datetime.strptime(viagem["data de volta"], "%Y-%m-%d")
    dias = (data_volta - data_ida).days

    
    if tipo_transporte == 1:
        preco_por_dia = 200
    elif tipo_transporte == 2:
        preco_por_dia = 100
    elif tipo_transporte == 3:
        preco_por_dia = 120  
    else:
        preco_por_dia = 0

    return dias * preco_por_dia
# Função para gerar a passagem do usuário com os detalhes da viagem
def gerarPassagem(cpf):
    if cpf in usuarios and usuarios[cpf]["viagens"]:
        viagem = usuarios[cpf]["viagens"][-1] 
        
        if "assento" not in viagem:
            viagem["assento"] = gerarAssento()

        destino = viagem["destino"]
        if destino in destinos_aereo:
            tipo_transporte = 1
        elif destino in destinos_rodoviario:
            tipo_transporte = 2
        elif destino in destinos_ferroviario:
            tipo_transporte = 3
        else:
            tipo_transporte = 0

        valor = gerarValor(viagem, tipo_transporte)

        print("\n" + "=" * 40)
        print(" " * 10 + "BILHETE DE VIAGEM")
        print("=" * 40)
        print(f"Passageiro: {usuarios[cpf]['nome']}")
        print(f"CPF: {usuarios[cpf]['cpf']}")
        print("-" * 40)
        print(f"Partida:      {viagem['partida']}")
        print(f"Destino:      {viagem['destino']}")
        print(f"Data de ida:  {viagem['data de ida']}")
        print(f"Data de volta:{viagem['data de volta']}")
        print(f"Assento:      {viagem['assento']}")
        print("-" * 40)
        print(f"Valor total: R$ {valor:.2f}")
        print("=" * 40 + "\n")
    else:
        print("Usuário não encontrado ou nenhuma viagem registrada.")
# Função para gerar um assento aleatório
def gerarAssento():
    fileira = random.randint(1, 30)              
    coluna = random.choice(['A', 'B', 'C', 'D'])  
    return f"{fileira}{coluna}"
# Função para exibir como mensagem caso o CPF não esteja cadastrado
def cpfNaoCadastrado():
    print('\n' + '='*50)
    print(' ' * 10 + '\033[91mCPF NÃO CADASTRADO\033[0m')
    print('='*50)
    print('\n\033[93mRealize o cadastro ou corrija as informações para continuar.\033[0m\n')
    while True:
        r = input('Deseja cadastrar um novo usuário? (s/n): ').strip().lower()
        if r in ['s', 'sim']:
            print('\n' + '-'*50)
            print('\033[92mIniciando cadastro de novo usuário...\033[0m')
            cadastro('usuário', usuarios, cpf)
            return
        elif r in ['n', 'nao', 'não']:
            print('\n' + '-'*50)
            print('\033[91mOperação cancelada pelo usuário.\033[0m\n')
            return
        else:
            print('\n\033[91m[!] Opção inválida! Por favor, responda com "s" ou "n".\033[0m\n')