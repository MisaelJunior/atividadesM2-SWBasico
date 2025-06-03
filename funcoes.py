from datetime import datetime
import os
import sys

cpf = ''

usuarios = {"470.331.668-42":{
    "nome": 'Misael',
    "cpf": '470.331.668-42',
    "telefone": '11998473130',
    "email": 'misael@umc.br',
    "senha": '1234',
    "viagens":[]
}}

chaves_de_acesso = ['1234']

destinos_aereo = ["NOVA YORK", "PARIS", "LONDRES", "TÓQUIO", "DUBAI", "ROMA", "BARCELONA", "BANGCOC", "SYDNEY", "HONG KONG", "SÃO PAULO", "RIO DE JANEIRO", "FORTALEZA", "SALVADOR", "MANAUS", "PORTO ALEGRE", "BELO HORIZONTE"]
destinos_rodoviario = ["RIO BRANCO", "MACEIÓ", "MACAPÁ", "MANAUS", "SALVADOR", "FORTALEZA", "BRASÍLIA", "VITÓRIA", "GOIÂNIA", "SÃO LUÍS","CUIABÁ", "CAMPO GRANDE", "BELO HORIZONTE", "BELÉM", "JOÃO PESSOA", "CURITIBA", "RECIFE", "TERESINA", "RIO DE JANEIRO", "NATAL", "PORTO ALEGRE", "PORTO VELHO", "BOA VISTA", "FLORIANÓPOLIS", "SÃO PAULO", "ARACAJU", "PALMAS"]
destinos_ferroviario = ["SÃO PAULO", "RIO DE JANEIRO", "BELO HORIZONTE", "CURITIBA", "SALVADOR", "FORTALEZA", "RECIFE", "PORTO ALEGRE","BRASÍLIA", "MANAUS", "CAMPINAS", "GOIÂNIA", "NATAL", "FLORIANÓPOLIS", "BELÉM", "VITÓRIA", "SÃO LUÍS", "JOÃO PESSOA", "MACEIÓ", "CUIABÁ"]

def menu():
    print('APLICATIVO DE RESERVAS\n')
    print('1. Criar usuário')
    print('2. Comprar passagem')
    print('3. Reservar hotel')
    print('4. Minhas passagens')
    print('5. Minhas reservas')
    print('6. Sair')

def menu_transportes():
    print('-----Tipos de Transporte-----')
    print('1. Aéreo')
    print('2. Rodoviário')
    print('3. Ferroviário')
    
    
def executar(comando):
    if comando == 1: criar_usuario()
    elif comando == 2: comprar_passagem()
    elif comando == 3: reservar_hotel()
    elif comando == 4: minhas_passagens()
    elif comando == 5: minhas_reservas()
    elif comando == 6: print('\nSair')
    elif comando == 741852963: verifica_clientes()
    else: print('\nOpção inválida.')
    
def criar_usuario():
    print('\n--- NOVO USUÁRIO ---')
    nome = input('\nDigite o nome do usuário: ')
    cpf = input('\nDigite o CPF do usuário (Utilize o formato 123.456.789-00): ')

    if cpf in usuarios:#consultando se o cpf já foi cadastrado
        print('CPF já cadastrado')
    else:#cadastrando o usuário
        tel = input('Telefone: ')
        email = input('Email: ')
        while True:
            senha = input('Crie uma senha: ')
            if len(senha) < 8:
                print('A senha deve possuir pelo menos 8 caracteres')
            else:
                os.system('cls')
                print('Senha cadastrada com sucesso')
                break
                
        
        usuarios[cpf] = {
            "nome": nome,
            "cpf": cpf,
            "telefone": tel,
            "email": email,
            "senha": senha,
            "viagens": []
        }
        print('Usuário cadastrado com sucesso.')

def validarSenha(identificador):
    tentativa = 1
    while True:
        validacao = input('Entre com a senha: ')
        if validacao == usuarios[identificador]["senha"]:#valida a senha do usuario
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
                        for i in destinos_aereo:
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
                break 
            except ValueError:
                print("Data inválida. Por favor, insira no formato AAAA-MM-DD.")
        
        print(f'Datas {data1.date()} - {data2.date()} reservadas com sucesso!')
        return data1.date(), data2.date()
        
def reservar_hotel():
    print('\n--- RESERVAR HOTEL ---')
    nome_hotel = input('\nDigite o nome do hotel: ')
    localizacao = input('\nDigite a localização do hotel: ')
    data_checkin = input('\nDigite a data de check-in: ')
    data_checkout = input('\nDigite a data de check-out: ')

    hotel = Reserva_Hotel(nome_hotel, localizacao, data_checkin, data_checkout)
    reservas_hoteis.append(hotel)

    print(f'\nQuarto do hotel {nome_hotel} reservado com sucesso!\n')
    hotel.exibir_dados()
    
def minhas_passagens():
    print('\n-------------------------------Minhas Passagens--------------------------------\nLOGIN')
    cpf = input('Entre com o CPF (Utilize o formato 123.456.789-00): ')
    if cpf in usuarios:
        validarSenha(cpf)
        print('')
        print('-' *80)
        print(f'\nUsuário: {usuarios[cpf]["nome"]}')
        print(f'CPF: {usuarios[cpf]["cpf"]}')
        print(f'Telefone: {usuarios[cpf]["telefone"]}')
        print(f'Email: {usuarios[cpf]["email"]}')
        print(f'Viagens:')
        for j in usuarios[cpf]["viagens"]:
                print(f' IDA  --- Partida: {j["partida"]}, Destino: {j["destino"]}, Data: {j["data de ida"]}')
                print(f'VOLTA --- Partida: {j["destino"]}, Destino: {j["partida"]}, Data: {j["data de volta"]}')
    else:
        print('CPF não cadastrado.\nRealize o cadastro ou corrija as informações para continuar.')
        while True:
                try:
                    r = input('Deseja cadastrar um novo usuário? s/n ')
                    if r.lower() == 's' or r.lower() == 'sim' :
                        criar_usuario()
                        break
                    elif r.lower() == 'n' or r.lower() == 'nao' or r.lower() == 'não':
                        minhas_passagens()
                        break
                    else:
                        print('Opção inválida!')
                except ValueError:
                    print('O tipo de dado inserido é inválido, tente novamente!')
    
def minhas_reservas():
    print('\n--- USUÁRIOS CADASTRADOS ---')
    for usuario in usuarios:
        usuario.exibir_dados()

    print('\n--- CONSULTAS AGENDADAS ---')
    for consulta in consultas:
        consulta.exibir_dados()

    print('\n--- PASSAGENS COMPRADAS ---')
    for passagem in passagens:
        passagem.exibir_dados()

    print('\n--- HOTÉIS RESERVADOS ---')
    for hotel in reservas_hoteis:
        hotel.exibir_dados()

def verifica_clientes():
    senha_adm = input('Insira sua chave de acesso administrativa: ')
    if senha_adm in chaves_de_acesso:
        os.system('cls')
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
                                                   
    else:
        print('Chave de acesso Incorreta')
        sys.exit()