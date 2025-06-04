from datetime import datetime
import os
import sys
import secrets
import random


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
    "chave de acesso": '1234',
    
}}

chaveMestra = ['1234']

destinos_aereo = ["NOVA YORK", "PARIS", "LONDRES", "TÓQUIO", "DUBAI", "ROMA", "BARCELONA", "BANGCOC", "SYDNEY", "HONG KONG", "SÃO PAULO", "RIO DE JANEIRO", "FORTALEZA", "SALVADOR", "MANAUS", "PORTO ALEGRE", "BELO HORIZONTE"]
destinos_rodoviario = ["RIO BRANCO", "MACEIÓ", "MACAPÁ", "MANAUS", "SALVADOR", "FORTALEZA", "BRASÍLIA", "VITÓRIA", "GOIÂNIA", "SÃO LUÍS","CUIABÁ", "CAMPO GRANDE", "BELO HORIZONTE", "BELÉM", "JOÃO PESSOA", "CURITIBA", "RECIFE", "TERESINA", "RIO DE JANEIRO", "NATAL", "PORTO ALEGRE", "PORTO VELHO", "BOA VISTA", "FLORIANÓPOLIS", "SÃO PAULO", "ARACAJU", "PALMAS"]
destinos_ferroviario = ["SÃO PAULO", "RIO DE JANEIRO", "BELO HORIZONTE", "CURITIBA", "SALVADOR", "FORTALEZA", "RECIFE", "PORTO ALEGRE","BRASÍLIA", "MANAUS", "CAMPINAS", "GOIÂNIA", "NATAL", "FLORIANÓPOLIS", "BELÉM", "VITÓRIA", "SÃO LUÍS", "JOÃO PESSOA", "MACEIÓ", "CUIABÁ"]

def menu():
    print('APLICATIVO DE RESERVAS\n')
    print('1. Criar usuário')
    print('2. Comprar passagem')
    print('3. Cadastro de Funcionários')
    print('4. Meu Perfil')
    print('5. Minhas reservas')
    print('6. Menu Administrativo')
    print('7. Sair')

def cadastro(pessoa, cargo, identificador):
    print(f'\n--- NOVO {pessoa.upper()} ---')
    cpf = input(f'\nDigite o CPF do {pessoa} (Utilize o formato 123.456.789-00): ')
    
    if cargo == funcionarios:
        mestra = input('É necessário entrar com a chave mestra para cadastrar um novo funcionário: ')
        if mestra in chaveMestra:
            print('\n--- CADASTRO DE FUNCIONÁRIO ---')
            identificador = input('\nDigite o ID do funcionário: ') 
            if identificador in funcionarios:
                print('ID já cadastrado')
            else:
                nome = input(f'\nDigite o nome do {pessoa}: ')
                cpf = input(f'\nDigite o CPF do {pessoa} (Utilize o formato 123.456.789-00): ')
                tel = input('Telefone: ')
                email = input('Email: ')
                while True:
                    chave = input('Crie uma chave de acesso: ')
                    if len(chave) < 8:
                        print('A chave de acesso deve possuir pelo menos 8 caracteres')
                    else:
                        os.system('cls')
                        print('Chave de acesso cadastrada com sucesso')
                        cargo[identificador] = {
                                "id": id,
                                "nome": nome,
                                "cpf": cpf,
                                "telefone": tel,
                                "email": email,
                                "chave de acesso": chave,
                            }
                        print('Funcionário cadastrado com sucesso.')
                        break
        else:
            print('Chave mestra não confere.')
            sair()
    else:
        if cpf in cargo:
            print('CPF já cadastrado')
        else:
            nome = input(f'\nDigite o nome do {pessoa}: ')
            tel = input('Telefone: ')
            email = input('Email: ')
            while True:
                senha = input('Crie uma senha: ')
                if len(senha) < 8:
                    print('A senha deve possuir pelo menos 8 caracteres')
                else:
                    os.system('cls')
                    print('Senha cadastrada com sucesso')
                    cargo[identificador] = {
                        "nome": nome,
                        "cpf": cpf,
                        "telefone": tel,
                        "email": email,
                        "senha": senha,
                        "viagens": []
                    }
                    print(f'{pessoa} cadastrado com sucesso.')
                    break
                
def menu_transportes():
    print('-----Tipos de Transporte-----')
    print('1. Aéreo')
    print('2. Rodoviário')
    print('3. Ferroviário')

def consultaUsuario(cpf):
    if cpf in usuarios:
        print('\n-------------------------------Busca de usuários--------------------------------\n')
        print('-' *80)
        print(f'\nUsuário: {usuarios[cpf]["nome"]}')
        print(f'CPF: {usuarios[cpf]["cpf"]}')
        print(f'Telefone: {usuarios[cpf]["telefone"]}')
        print(f'Email: {usuarios[cpf]["email"]}')
        print(f'Viagens:')
        for i in usuarios[cpf]["viagens"]:
            print(f' IDA  --- Partida: {i["partida"]}, Destino: {i["destino"]}, Data: {i["data de ida"]}')
            print(f'VOLTA --- Partida: {i["destino"]}, Destino: {i["partida"]}, Data: {i["data de volta"]}')  
    
def executar(comando):
    while True:
        try:
            if comando == 1:
                cadastro('usuário', usuarios, cpf)
                break
            elif comando == 2:
                comprar_passagem()
                break
            elif comando == 3:
                cadastro('funcionário', funcionarios, id)
                break
            elif comando == 4:
                meuPerfil()
                break
            elif comando == 5:
                minhas_reservas()
                break
            elif comando == 6:
                verifica_clientes()
                break
            elif comando == 7:
                sair()
            else: print('\nOpção inválida.')
        except ValueError:
            print('\nOpção inválida.')

def sair():
    print('\nSair.')
    sys.exit()    

def validarSenha(identificador):
    tentativa = 1
    while True:
        validacao = input('Entre com a senha: ')
        if validacao == usuarios[identificador]["senha"]:
            break
        else:
            print(f'Senha Incorreta\nTentativa {tentativa}/3')
            tentativa += 1
            if tentativa > 3:
                sys.exit()
        
def comprar_passagem():
    print('\n--- COMPRAR PASSAGEM ---')
    cpf = input('\nDigite o CPF do usuário (Utilize o formato 123.456.789-00): ')
    if cpf in usuarios:
        validarSenha(cpf)        
        menu_transportes()
        while True:
                try:
                    tipo_de_transporte = int(input('Selecione um tipo de transporte: '))
                    if tipo_de_transporte < 1 or tipo_de_transporte > 3:
                        print('\033[1;31mOpção inválida! Digite um número de 1 a 3.\033[m')
                    else:
                        break
                except ValueError:
                    print('\033[1;31mOpção inválida! Digite um número de 1 a 3.\033[m')
        
        if tipo_de_transporte == 1:
            print('Tipo de transporte escolhido: Aéreo')
            while True:
                try:
                    r = input('Gosataria de ver todos os locais de partida disponíveis? s/n\n')
                    if r.lower() == 's' or r.lower() == 'sim':
                        for i in destinos_rodoviario:
                            print(i)
                        break
                    elif r.lower() == 'n' or r.lower() == 'nao' or r.lower() == 'não':
                        break
                    else:
                        print('Opção inválida!')
                except ValueError:
                    print('O tipo de dado inserido é inválido, tente novamente!')
            
            input('Pressione a tecla Enter para continuar\n')
                    
            while True:
                try:
                    a = input('Escolha o local de partida: ')
                    if a.upper() in destinos_rodoviario:
                        print(f'Local de partida definido! {a.upper()}')
                        break
                    else:
                        print('Local de partida não disponível ou incorreto!')
                except ValueError:
                    print('O tipo de dado inserido é inválido, tente novamente!')
                    
            while True:
                try:
                    r = input('Gosataria de ver todos os locais de destino disponíveis? s/n\n')
                    if r.lower() == 's' or r.lower() == 'sim':
                        for i in destinos_aereo:
                            print(i)
                        break
                    elif r.lower() == 'n' or r.lower() == 'nao' or r.lower() == 'não':
                        break
                    else:
                        print('Opção inválida!')
                except ValueError:
                    print('O tipo de dado inserido é inválido, tente novamente!')
                    
            input('Pressione a tecla Enter para continuar\n')
                    
            while True:
                try:
                    b = input('Escolha o local de destino: ')
                    if b.upper() in destinos_aereo:
                        print(f'Local de destino definido! {b.upper()}')
                        break
                    else:
                        print('Local de destino não disponível ou incorreto!')
                except ValueError:
                    print('O tipo de dado inserido é inválido, tente novamente!')

            usuarios[cpf]["viagens"].append({
                    "partida": a.upper(),
                    "destino": b.upper(),
                    "data de ida": None,
                    "data de volta": None,
                })   
            
            data_ida, data_volta = reservar_data()

            usuarios[cpf]["viagens"][-1]["data de ida"] = str(data_ida)
            usuarios[cpf]["viagens"][-1]["data de volta"] = str(data_volta)

            
            
        elif tipo_de_transporte == 2:
            print('Tipo de transporte escolhido: Rodoviário')
            while True:
                try:
                    r = input('Gosataria de ver todos os locais de partida disponíveis? s/n')
                    if r.lower() == 's' or r.lower() == 'sim':
                        for i in destinos_rodoviario:
                            print(i)
                        break
                    elif r.lower() == 'n' or r.lower() == 'nao' or r.lower() == 'não':
                        break
                    else:
                        print('Opção inválida!')
                except ValueError:
                    print('O tipo de dado inserido é inválido, tente novamente!')
            
            input('Pressione a tecla Enter para continuar')
            
            while True:
                try:
                    a = input('Escolha o local de partida: ')
                    if a.upper() in destinos_rodoviario:
                        print(f'Local de partida definido! {a.upper()}')
                        break
                    else:
                        print('Local de partida não disponível ou incorreto!')
                except ValueError:
                    print('O tipo de dado inserido é inválido, tente novamente!')
            while True:
                try:
                    r = input('Gosataria de ver todos os locais de destino disponíveis? s/n')
                    if r.lower() == 's' or r.lower() == 'sim':
                        for i in destinos_rodoviario:
                            print(i)
                        break
                    elif r.lower() == 'n' or r.lower() == 'nao' or r.lower() == 'não':
                        break
                    else:
                        print('Opção inválida!')
                except ValueError:
                    print('O tipo de dado inserido é inválido, tente novamente!')
            
            input('Pressione a tecla Enter para continuar')
            
            while True:
                try:
                    b = input('Escolha o local de destino: ')
                    if b.upper() in destinos_rodoviario:
                        print(f'Local de destino definido! {b.upper()}')
                        break
                    else:
                        print('Local de destino não disponível ou incorreto!')
                except ValueError:
                    print('O tipo de dado inserido é inválido, tente novamente!')
                    
            usuarios[cpf]["viagens"].append({
                    "partida": a.upper(),
                    "destino": b.upper(),
                    "data de ida": None,
                    "data de volta": None,
                })  
            
            data_ida, data_volta = reservar_data()

            usuarios[cpf]["viagens"][-1]["data de ida"] = str(data_ida)
            usuarios[cpf]["viagens"][-1]["data de volta"] = str(data_volta)      
                    
        else:
            print('Tipo de transporte escolhido: Ferroviário')
            while True:
                try:
                    r = input('Gosataria de ver todos os locais de partida disponíveis? s/n')
                    if r.lower() == 's' or r.lower() == 'sim':
                        for i in destinos_ferroviario:
                            print(i)
                        break
                    elif r.lower() == 'n' or r.lower() == 'nao' or r.lower() == 'não':
                        break
                    else:
                        print('Opção inválida!')
                except ValueError:
                    print('O tipo de dado inserido é inválido, tente novamente!')
            
            input('Pressione a tecla Enter para continuar')
            
            while True:
                try:
                    a = input('Escolha o local de partida: ')
                    if a.upper() in destinos_ferroviario:
                        print(f'Local de partida definido! {a.upper()}')
                        break
                    else:
                        print('Local de partida não disponível ou incorreto!')
                except ValueError:
                    print('O tipo de dado inserido é inválido, tente novamente!')
                    
            while True:
                try:
                    r = input('Gosataria de ver todos os locais de destino disponíveis? s/n')
                    if r.lower() == 's' or r.lower() == 'sim':
                        for i in destinos_ferroviario:
                            print(i)
                        break
                    elif r.lower() == 'n' or r.lower() == 'nao' or r.lower() == 'não':
                        break
                    else:
                        print('Opção inválida!')
                except ValueError:
                    print('O tipo de dado inserido é inválido, tente novamente!')
            
            input('Pressione a tecla Enter para continuar')
            
            while True:
                try:
                    b = input('Escolha o local de destino: ')
                    if b.upper() in destinos_ferroviario:
                        print(f'Local de destino definido! {b.upper()}')
                        break
                    else:
                        print('Local de destino não disponível ou incorreto!')
                except ValueError:
                    print('O tipo de dado inserido é inválido, tente novamente!')
                    
            usuarios[cpf]["viagens"].append({
                    "partida": a.upper(),
                    "destino": b.upper(),
                    "data de ida": None,
                    "data de volta": None,
                })
        
            data_ida, data_volta = reservar_data()

            usuarios[cpf]["viagens"][-1]["data de ida"] = str(data_ida)
            usuarios[cpf]["viagens"][-1]["data de volta"] = str(data_volta)
               
    else:
        print('CPF não cadastrado.\nRealize o cadastro ou corrija as informações para continuar.')
        while True:
                try:
                    r = input('Deseja cadastrar um novo usuário? s/n ')
                    if r.lower() == 's' or r.lower() == 'sim' :
                        criar_usuario()
                        break
                    elif r.lower() == 'n' or r.lower() == 'nao' or r.lower() == 'não':
                        comprar_passagem()
                        break
                    else:
                        print('Opção inválida!')
                except ValueError:
                    print('O tipo de dado inserido é inválido, tente novamente!')
        
def reservar_data():
    while True:
        while True:
            try:
                data_str = input("Insira data de ida no formato AAAA-MM-DD: ")
                data1 = datetime.strptime(data_str, "%Y-%m-%d")
                break 
            except ValueError:
                print("Data inválida. Por favor, insira no formato AAAA-MM-DD.")
                
        while True:
            try:
                data_str = input("Insira data de volta no formato AAAA-MM-DD: ")
                data2 = datetime.strptime(data_str, "%Y-%m-%d")
                if data2 >= data1:
                    break
                else:
                    print("A data de volta NÃO pode ser ANTERIOR a data de ida.") 
            except ValueError:
                print("Data inválida. Por favor, insira no formato AAAA-MM-DD.")
        
        print(f'Datas {data1.date()} - {data2.date()} reservadas com sucesso!')
        return data1.date(), data2.date()    
    
def meuPerfil():
    print('\n-------------------------------Meu Perfil--------------------------------\nLOGIN')
    cpf = input('Entre com o CPF (Utilize o formato 123.456.789-00): ')
    if cpf in usuarios:
        validarSenha(cpf)
        os.system('cls')
        print('\n-------------------------------Meu Perfil--------------------------------\n')
        print('-' *80)
        print(f'\nNome: {usuarios[cpf]["nome"]}')
        print(f'CPF: {usuarios[cpf]["cpf"]}')
        print(f'Telefone: {usuarios[cpf]["telefone"]}')
        print(f'Email: {usuarios[cpf]["email"]}')
        print('\n-------------------------------Minhas Passagens--------------------------------')
        print(f'Viagens:')
        for j in usuarios[cpf]["viagens"]:
                print(f' IDA  --- Partida: {j["partida"]}, Destino: {j["destino"]}, Data: {j["data de ida"]}')
                print(f'VOLTA --- Partida: {j["destino"]}, Destino: {j["partida"]}, Data: {j["data de volta"]}')
                
        while True:
            try:
                print('Perfil do usuário-----------------------------------')
                print('1. Alterar Nome\n2. Alterar Telefone\n3. Alterar Email\n4. Alterar Senha\n5. Recadastro\n6. Imprimir Passagem\n7. Voltar')
                while True:
                    try:
                        escolha = int(input('Selecione uma ação: '))
                        if escolha < 1 or escolha > 7:
                            print('Opção Inválida!')
                        else:
                            print(escolha)
                            break
                    except ValueError:
                        print('Tipo de dado inserido inválido!')
                
                if escolha == 1:
                    nome = input('Insira o novo nome: ')
                    usuarios[cpf]["nome"] = nome
                    print('Nome alterado com sucesso!')
                    input('Pressione a tecla Enter para continuar')
                    break
                elif escolha == 2:
                    telefone = input('Insira o novo número de telefone: ')
                    usuarios[cpf]["telefone"] = telefone
                    print('Telefone alterado com sucesso!')
                    input('Pressione a tecla Enter para continuar')
                    break
                elif escolha == 3:
                    email = input('Insira o novo email: ')
                    usuarios[cpf]["email"] = email
                    print('Email alterado com sucesso!')
                    input('Pressione a tecla Enter para continuar')
                    break
                elif escolha == 4:
                    senha_atual = input('Entre com a senha atual: ')
                    if senha_atual == usuarios[cpf]["senha"]:
                        while True:
                            nova_senha = input('Nova senha: ')
                            if len(nova_senha) < 8:
                                print('A senha deve possuir pelo menos 8 caracteres')
                            else:
                                os.system('cls')
                                print('Senha cadastrada com sucesso')
                                break 
                        usuarios[cpf]["senha"] = nova_senha
                        print('Senha alterada com sucesso!')
                        input('Pressione a tecla Enter para continuar')
                    break
                elif escolha == 5:
                    print('Ao confirmar seu cadastro será excluído e você será direcionado(a) a criação de um novo cadastro')
                    while True:
                        try:
                            r = input('Deseja excluir o cadastro atual e criar um novo usuário? s/n ')
                            if r.lower() == 's' or r.lower() == 'sim' :
                                cpf = input('Excluindo cadastro...\nConfirme o seu CPF: ')
                                validarSenha(cpf)
                                del usuarios[cpf]
                                print('Usuário excluído com sucesso!')
                                criar_usuario()
                                break
                            elif r.lower() == 'n' or r.lower() == 'nao' or r.lower() == 'não':
                                break
                            else:
                                print('Opção inválida!')
                        except ValueError:
                            print('O tipo de dado inserido é inválido, tente novamente!')
                    input('Pressione a tecla Enter para continuar')
                    break
                elif escolha == 6:
                    if usuarios[cpf]["viagens"]:
                        codigo = secrets.token_hex(20)
                        print(f'Código para o pagamento {codigo}.\nA passagem só será validada caso o pagamento seja confirmado.\n')
                        gerar_passagem(cpf)
                    else:
                        print("Nenhuma viagem cadastrada. Não é possível gerar código.")
                        input('Pressione a tecla Enter para continuar')
                        os.system('cls')
                else:
                    None
                    break
                   
            except ValueError:
                print('Tipo de dado inserido inválido!')  
        
    else:
        print('CPF não cadastrado.\nRealize o cadastro ou corrija as informações para continuar.')
        while True:
                try:
                    r = input('Deseja cadastrar um novo usuário? s/n ')
                    if r.lower() == 's' or r.lower() == 'sim' :
                        criar_usuario()
                        break
                    elif r.lower() == 'n' or r.lower() == 'nao' or r.lower() == 'não':
                        meuPerfil()
                        break
                    else:
                        print('Opção inválida!')
                except ValueError:
                    print('O tipo de dado inserido é inválido, tente novamente!')
    
def minhas_reservas():
    cpf = input('Entre com o CPF (Utilize o formato 123.456.789-00): ')
    if cpf in usuarios:
        validarSenha(cpf)
        os.system('cls')
        print('-' *80)
        print(f'\nNome: {usuarios[cpf]["nome"]}')
        print('\n-------------------------------Minhas Passagens--------------------------------')
        print(f'Viagens:')
        for j in usuarios[cpf]["viagens"]:
                print(f' IDA  --- Partida: {j["partida"]}, Destino: {j["destino"]}, Data: {j["data de ida"]}')
                print(f'VOLTA --- Partida: {j["destino"]}, Destino: {j["partida"]}, Data: {j["data de volta"]}')

def verifica_clientes():
    id = input('Funcionário, insira seu ID: ')
    if id in funcionarios:
        senha_adm = input('Insira sua chave de acesso administrativa: ')
        if (senha_adm == funcionarios[id]["chave de acesso"]) or (senha_adm in chaveMestra):
            while True:
                os.system('cls')
                print('1. Cadastrar Usuário\n2. Consultar usuário\n3. Alterar dados de usuário\n4. Consultar lista de usuários\n5. Voltar')
                acao = int(input('Que ação deseja realizar? '))
                try:
                    if acao == 1:
                        criar_usuario()
                        break
                    elif acao == 2:
                        cpf = input('Insira o CPF para a Busca: ')
                        consultaUsuario(cpf)
                        break
                    elif acao == 3:
                        cpf = input('Insira o CPF para a Busca: ')
                        consultaUsuario(cpf)
                        while True:
                            try:
                                print('Perfil do usuário-----------------------------------')
                                print('1. Nome\n2. Telefone\n3. Email\n4. Recadastro\n5. Voltar')
                                while True:
                                    try:
                                        escolha = int(input('Selecione qual dado deseja alterar: '))
                                        if escolha < 1 or escolha > 5:
                                            print('Opção Inválida!')
                                        else:
                                            print(escolha)
                                            break
                                    except ValueError:
                                        print('Tipo de dado inserido inválido!')

                                if escolha == 1:
                                    nome = input('Insira o novo nome: ')
                                    usuarios[cpf]["nome"] = nome
                                    print('Nome alterado com sucesso!')
                                    input('Pressione a tecla Enter para continuar')
                                    break
                                elif escolha == 2:
                                    telefone = input('Insira o novo número de telefone: ')
                                    usuarios[cpf]["telefone"] = telefone
                                    print('Telefone alterado com sucesso!')
                                    input('Pressione a tecla Enter para continuar')
                                    break
                                elif escolha == 3:
                                    email = input('Insira o novo email: ')
                                    usuarios[cpf]["email"] = email
                                    print('Email alterado com sucesso!')
                                    input('Pressione a tecla Enter para continuar')
                                    break
                                elif escolha == 4:
                                    print('Ao confirmar seu cadastro será excluído e você será direcionado(a) a criação de um novo cadastro')
                                    while True:
                                        try:
                                            r = input('Deseja excluir o cadastro atual e criar um novo usuário? s/n ')
                                            if r.lower() == 's' or r.lower() == 'sim' :
                                                cpf = input('Excluindo cadastro...\nConfirme o seu CPF: ')
                                                validarSenha(cpf)
                                                del usuarios[cpf]
                                                print('Usuário excluído com sucesso!')
                                                criar_usuario()
                                                break
                                            elif r.lower() == 'n' or r.lower() == 'nao' or r.lower() == 'não':
                                                break
                                            else:
                                                print('Opção inválida!')
                                        except ValueError:
                                            print('O tipo de dado inserido é inválido, tente novamente!')
                                    input('Pressione a tecla Enter para continuar')
                                    break
                                else:
                                    None
                                    break
                            except ValueError:
                                    print('O tipo de dado inserido é inválido, tente novamente!')
                                    input('Pressione a tecla Enter para continuar')
                    elif acao == 4:
                        print('\n-------------------------------Lista de usuários--------------------------------\nQuantidade de usuários: ', len(usuarios))
                        for i in usuarios:#mostra os dados pessoais de cada usuário cadastrado. OBS: note que a senha cadastrada pelo usuário não é mostrada por segurança
                            print('')
                            print('-' *80)
                            print(f'\nUsuário: {usuarios[i]["nome"]}')
                            print(f'CPF: {usuarios[i]["cpf"]}')
                            print(f'Telefone: {usuarios[i]["telefone"]}')
                            print(f'Email: {usuarios[i]["email"]}')
                            print(f'Viagens:')
                            for j in usuarios[i]["viagens"]:
                                print(f' IDA  --- Partida: {j["partida"]}, Destino: {j["destino"]}, Data: {j["data de ida"]}')
                                print(f'VOLTA --- Partida: {j["destino"]}, Destino: {j["partida"]}, Data: {j["data de volta"]}')
                        break
                    elif acao == 5:
                        break
                    else: print('\nOpção inválida.')
                except ValueError:
                    print('\nOpção inválida.')
            input('\nPressione a tecla Enter para continuar')
                                                    
        else:
            print('Chave de acesso Incorreta')
            sys.exit()

def gerar_valor(viagem, tipo_transporte):
    
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

def gerar_passagem(cpf):
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

        valor = gerar_valor(viagem, tipo_transporte)

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

def gerarAssento():
    fileira = random.randint(1, 30)              
    coluna = random.choice(['A', 'B', 'C', 'D'])  
    return f"{fileira}{coluna}"