from time import sleep

cor = [
    '\033[1;31m', # vermelho        0 <- índice
    '\033[1;33m', # amarelo         1 <- índice
    '\033[32m',   # verde           2 <- índice
    '\033[m',     # sem_formatação  3 <- índice
    '\033[7;33m'  # tela_invertida  4 <- índice
]


def interface(msg):
    for c in msg:
        print('=' * 40)
        print(f'{c:^34}')
        print('=' * 40)
        sleep(2)


def dados(l):
    print()
    print('Dado(s) do(s) veículo(s)'.center(40))
    print('-=' * 20)
    print(f'{cor[4]}{'Veículo':<17}{'Placa':<20}{'Cor':}{cor[3]}')
    # Aqui eu desempaco os dados
    for c in l:
        # Cada dados desempacota vai para a função cla de class
        cla(c)
    print('-=' * 20)
    print()


def cla(v):
    class Veiculo:
        def __init__(self, modelo, placa, cor_veiculo):
            self.modelo = modelo
            self.placa = placa
            self.cor_veiculo = cor_veiculo
            # Essas duas variável vão servir para eu separar os dados co "-"
            placa1 = ''
            placa2 = ''

        def tabe(self):
            placa1 = self.placa[:4] + '-'
            placa2 = self.placa[-4:]
            self.placa = placa1 + placa2
            print(f'{self.modelo:15}{self.placa:<17}{self.cor_veiculo}')


    carro = Veiculo(v[0], v[1], v[2])
    carro.tabe()