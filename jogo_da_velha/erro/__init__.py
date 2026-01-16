from time import sleep

cor = [
    '\033[31m', # vermelho <-- 0
    '\033[32m', # verde    <-- 1
    '\033[33m', # amarelo  <-- 2
    '\033[m',   # limpar   <-- 3
]


def ver(msg):
    while True:
        try:
            r = int(input(msg))
        except (ValueError, TypeError):
            print(f'{cor[0]}Valor incorreto.{cor[3]}')
        except KeyboardInterrupt:
            print(f'{cor[2]} Player encerrou a jogada.{cor[3]}')
            return 3
        else:
            if not r in {1, 2, 3}:
                print(f'{cor[0]}Valor invalido, informe valor entre (1 a 2).{cor[3]}')
            else:
                return r
        print('-'*30)
        sleep(2)



def velha(r):
    c_lin = 1
    for c in r:
        cont = 1
        for v in c:
            if cont < 3:
                print(f'{v:^6}|', end='')
            else:
                print(f'{v:^6}', end=' ')
            cont += 1
        if c_lin <= 2:
            print('\n------+------+------')
            c_lin += 1


def index(l, i, v):
    cont = 1
    for c in l:
        for v in c:
            cont += 1
            if cont == i:
                v[(i-1)] = v
