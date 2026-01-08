from time import sleep

def linha():
    print('-'*50)


def cabe(msg):
    linha()
    print(f'\033[1;33m{msg.center(50)}\033[m')


def opção(v):
    try:
        valor = int(input(v))
    except (ValueError, TypeError):
        print('\033[1;31mValor invalido. Por favor informe novamente.\033[m')
    except KeyboardInterrupt:
        print('\033[1;36mUsuário encerrou o programa.\033[m')
        return 3
    else:
        if valor > 3 or valor < 1:
            print('\033[1;31mValor invalido.\033[m')
        else:
            return valor
    linha()
    sleep(2)


def ler():
    lista = []
    try:
        with open("registro.txt", "rt", encoding="utf-8") as arquivo:
            for c in arquivo:
                if ';' in c:
                    remove = c.split(';')
                    remove[1] = remove[1].replace('\n','')
                    lista.append(remove)
    except FileNotFoundError:
        pass
    else:
        for c in lista:
            print(f'{c[0]:<30}{c[1]:<4} anos')



def cad(name, id):
    with open("registro.txt","a", encoding="utf-8") as arquivo:
        arquivo.write(f'{name};{id}\n')



def menu(msg):
    encerrar = 0
    while True:
        cabe('Opções Do Menu')

        for n, c in enumerate(msg):
            print(f'\033[1;33m{n+1}:\033[m \033[1m{c}\033[m')
        linha()

        r = opção('Opcão: ')

        if r == 1:
            cabe('Mostrar Cadastro')
            linha()
            ler()
            linha()
            sleep(2)

        elif r == 2:
            cabe('Novo Cadastro')
            linha()

            while True:
                try:
                    nome = str(input('Nome: ')).title()
                    if nome == '':
                        nome = 'Desconhecido'
                        print('\033[1;33mUsuário não quis informa os dados.\033[m')
                except (ValueError, TypeError):
                    print('\033[1;31mValor invalido. Por favor informe novamente.\033[m')
                except KeyboardInterrupt:
                    print('\033[1;36mUsuário encerrou o cadastro.\033[m')
                    encerrar = 3
                    break
                else:
                    break
                linha()

            if not encerrar == 3:

                while True:
                    try:
                        idade = str(input('Idade: '))
                        if idade == '':
                            idade = '0'
                            print('\033[1;33mUsuário não quis informa os dados.\033[m')
                    except (ValueError, TypeError):
                        print('\033[1;31mValor invalido. Por favor informe novamente.\033[m')
                    except KeyboardInterrupt:
                        print('\033[1;36mUsuário encerrou o cadastro.\033[m')
                        encerrar = 3
                        break
                    else:
                        break

            if not encerrar == 3:
                cad(nome, idade)
                print('\033[1;32mCadastrado com sucesso!\033[m')
                linha()
                sleep(2)

            elif encerrar == 3:
                return 3

        elif r == 3:
            return r
            break