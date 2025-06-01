usuarios = {}
destinos_aereo = []
destinos_rodoviario = []
destinos_ferroviario = []
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
        
        usuarios[cpf] = {
            "nome": nome,
            "cpf": cpf,
            "telefone": tel,
            "email": email
        }
        print('Usuário cadastrado com sucesso.')
        
def comprar_passagem():
    print('\n--- COMPRAR PASSAGEM ---')
    cpf = input('\nDigite o CPF do usuário (Utilize o formato 123.456.789-00): ')
    if cpf in usuarios:
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
        elif tipo_de_transporte == 2:
            print('Tipo de transporte escolhido: Rodoviário')
        else:
            print('Tipo de transporte escolhido: Ferroviário')

        
    else:
        print('CPF não cadastrado.\nRealize o cadastro para continuar.')
        criar_usuario()
    

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
    print('\n--- AGENDAR CONSULTA ---')
    especialidade = input('\nDigite a especialidade: ')
    local = input('\nDigite o local da consulta: ')
    medico = input('\nDigite o nome do médico: ')
    data_consulta = input('\nDigite a data da consulta: ')

    consulta = Consulta(especialidade, local, medico, data_consulta)
    consultas.append(consulta)

    print('\nConsulta agendada com sucesso!\n')
    consulta.exibir_dados()
    
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