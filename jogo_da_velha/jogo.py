from time import sleep
from jogo_da_velha.erro import *

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
di = {}
li = []

print(f'{'-'*30}\nVamos jogar o jogo da velha\n{'-'*30}')

while True:

    r = ver(f'Escolha\n1 para [ X ]\n2 para [ 0 ]\n3 para Sair\n\nResposta: ')

    if r in {1, 2, 3}:

        print(f'{'-' * 30}')

        match r:
            case 1:
                print('Você escolheu [ X ].')
                print('Player 2 ficará com [ O ].')
                di['nome'] = 'Player 1'
                di['obj'] = 'X'
                li.append(di.copy())
                di.clear()
                di['nome'] = 'Player 2'
                di['obj'] = 'O'
                li.append(di.copy())
                di.clear()
            case 2:
                print('Você escolheu [ O ].')
                print('Player 2 ficará [ X ].')
                di['nome'] = 'Player 1'
                di['obj'] = 'O'
                li.append(di.copy())
                di.clear()
                di['nome'] = 'Player 2'
                di['obj'] = 'X'
                li.append(di.copy())
                di.clear()
            case 3:
                print('Jogo encerrado')
        print(f'{'-' * 30}')


        sleep(2)

        if not r == 3:
            print(f'{'-'*30}\nJogo iniciará em')

            '''for c in range(3, 1 -1, -1):
                sleep(2)
                print(f'{c}', end = '...')
            print(f'\n{'-'*30}')'''

        break



if r in {1, 2}:
    velha(lista)


if not r == 3:
    t = True
    i = 0
    while True:
        for c in range(9):
            while True:
                try:
                    posição = int(input(f'\n{li[i]['nome']}\nEm qual posição vai jogar? '))
                except (ValueError, TypeError):
                    print('Erro de Valor.')
                except KeyboardInterrupt:
                    print('Player encerrou a jogada.')
                    t = False
                    break
            if not t == True:

                for c in lista:
                    for v in c:
                        if posição == v:
                            v = li[i]['obj']
            i += 1
            if i == 3:
                i = 0
            else:
                break
        if t == False:
            break

