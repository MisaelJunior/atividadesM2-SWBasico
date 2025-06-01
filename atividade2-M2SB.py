# Aplicativo de reservas: agendar consultas, reservas de hotel ou passagens
# Data: 06/06/2025
# Autores: Diego Miranda - turma C - 11251505836
#          Enzo Pereira - turma C - 11251103452
#          Misael da Silva - turma C - 11251102593

import os

class Usuario:
    def _init_(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')

class Consulta:
    def _init_(self, especialidade, local, medico, data_consulta):
        self.especialidade = especialidade
        self.local = local
        self.medico = medico
        self.data_consulta = data_consulta

    def exibir_dados(self):
        print(f'Especialidade: {self.especialidade}')
        print(f'Local: {self.local}')
        print(f'Médico: {self.medico}')
        print(f'Data: {self.data_consulta}')

class Passagem:
    def _init_(self, origem, destino, data_partida, tipo_transporte):
        self.origem = origem
        self.destino = destino
        self.data_partida = data_partida
        self.tipo_transporte = tipo_transporte

    def exibir_dados(self):
        print(f'Origem: {self.origem}')
        print(f'Destino: {self.destino}')
        print(f'Data da partida: {self.data_partida}')
        print(f'Tipo de transporte: {self.tipo_transporte}')

class Reserva_Hotel:
    def _init_(self, nome_hotel, localizacao, data_checkin, data_checkout):
        self.nome_hotel = nome_hotel
        self.localizacao = localizacao
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout

    def exibir_dados(self):
        print(f'Nome do Hotel: {self.nome_hotel}')
        print(f'Localização: {self.localizacao}')
        print(f'Data de check-in: {self.data_checkin}')
        print(f'Data de check-out: {self.data_checkout}')

usuarios = []
consultas = []
passagens = []
reservas_hoteis = []

def menu():
    print('APLICATIVO DE RESERVAS\n')
    print('1. Criar usuário')
    print('2. Agendar consulta')
    print('3. Comprar passagem')
    print('4. Reservar hotel')
    print('5. Listar todos os dados cadastrados')
    print('6. Sair')

def criar_usuario():
    print('\n--- NOVO USUÁRIO ---')
    nome = input('\nDigite o nome do usuário: ')
    cpf = (input('\nDigite o CPF do usuário (use pontos e traço): '))

    usuario = Usuario(nome, cpf)
    usuarios.append(usuario)

    print('\nUsuário criado com sucesso!\n')
    usuario.exibir_dados()

def agendar_consulta():
    print('\n--- AGENDAR CONSULTA ---')
    especialidade = input('\nDigite a especialidade: ')
    local = input('\nDigite o local da consulta: ')
    medico = input('\nDigite o nome do médico: ')
    data_consulta = input('\nDigite a data da consulta: ')

    consulta = Consulta(especialidade, local, medico, data_consulta)
    consultas.append(consulta)

    print('\nConsulta agendada com sucesso!\n')
    consulta.exibir_dados()

def comprar_passagem():
    print('\n--- COMPRAR PASSAGEM ---')
    origem = input('\nDigite o local de origem da viagem: ')
    destino = input('\nDigite o local de destino da viagem: ')
    data_partida = input('\nDigite a data de partida: ')
    tipo_transporte = input('\nDigite o tipo de transporte da viagem: ')

    passagem = Passagem(origem, destino, data_partida, tipo_transporte)
    passagens.append(passagem)

    print('\nPassagem comprada com sucesso!\n')
    passagem.exibir_dados()

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

def listar_dados():
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

def executar(comando):
    if comando == 1: criar_usuario()
    elif comando == 2: agendar_consulta()
    elif comando == 3: comprar_passagem()
    elif comando == 4: reservar_hotel()
    elif comando == 5: listar_dados()
    elif comando == 6: print('\nSair')
    else: print('\nOpção inválida.')

comando = 0

while comando != 6:
    os.system('cls')
    menu()
    comando = int(input('\nEscolha uma opção: '))
    executar(comando)
    input('\nPressione qualquer tecla.')