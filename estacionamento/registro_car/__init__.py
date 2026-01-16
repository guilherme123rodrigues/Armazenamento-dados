from estacionamento.funções import interface
from estacionamento.armazenamento_registro import ler
from estacionamento.cadastro import cad, encerra

# cores
cor = [
    '\033[31m',   # vermelho         0   <- índice
    '\033[1;33m', # amarelo          1   <- índice
    '\033[32m',   # verde            2   <- índice
    '\033[m',     # sem_formatação   3   <- índice
]

while True:
    # Função para mostra o cabeçalho
    interface(['ESTACIONAMENTO ⭐⭐⭐⭐⭐', 'SISTEMA DE REGISTRO DO VEÍCULO'])
    r = str(input('''
[ 1 ] Ver cadastra
[ 2 ] novo Cadastro
[ 3 ] Sair
Opção: ''')).strip()
    match r:
        case '1':
            ler()
        case '2':
            r = cad()
            if r == '3':
                break
        case '3':
            encerra()
            break
        case _:
            print(f'{cor[0]}Erro, tente novamente.{cor[3]}')
