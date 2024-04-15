
from Services import Elevador

# Funções para manipular as ações do menu
def subir():
    if elevador.atualAndar < elevador.totalAndar:
        elevador.Subir()
        print('Subindo')
    else:
        print('Você está no andar mais alto!')

def descer():
    if elevador.atualAndar > 0:
        elevador.Descer()
        print('Descendo')
    else:
        print('Você já está no térreo!')

def entrar():
    if elevador.atualCapacidade < elevador.totalCapacidade:
        elevador.Entrar()
        print('Entrando uma pessoa')
    else:
        print('Está lotado!')

def sair():
    elevador.Sair()
    print('Saindo uma pessoa')

# Elevador com capacidade máxima de 6 pessoas e 4 andares
elevador = Elevador(6 , 4)

# Loop principal do menu
while True:
    # Exibir as opções do menu
    print('''Menu do Elevador'''
    '1. Subir'
    '2. Descer'
    '3. Entrar'
    '4. Sair'
    '5. Informações do Elevador'
    '0. Sair do programa''')

    # Capturar a opção escolhida pelo usuário
    opcao = input('Escolha uma opção: ')

    # Executar a ação correspondente à opção escolhida
    if opcao == '1':
        subir()
    elif opcao == '2':
        descer()
    elif opcao == '3':
        entrar()
    elif opcao == '4':
        sair()
    elif opcao == '5':
        print(f'Capacidade Atual: {elevador.atualCapacidade}')
        print(f'Andar Atual: {elevador.atualAndar}')
    elif opcao == '0':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida! Por favor, escolha uma opção válida.')
