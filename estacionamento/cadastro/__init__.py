from time import sleep
from estacionamento.armazenamento_registro import  salvar
from estacionamento.funções import dados

cor = [
    '\033[31m',   # vermelho         0   <- índice
    '\033[1;33m', # amarelo          1   <- índice
    '\033[32m',   # verde            2   <- índice
    '\033[m',     # sem_formatação   3   <- índice
]

def cad():

    # lista para armazenar os carros cadastrados
    lista = []
    # lista1 para copiar os dados da lista
    lista1 = []

    while True:
        t = False
        try:
            print('-' * 56)
            print(f'Quantos veículos serão cadastrado no sistema de controle'
                  f'\n{cor[1]}Obs.:{cor[3]}[0] é considerado encerramento do sistema? ')
            print('-' * 56)
            q = int(input('Resposta: '))
        except (ValueError, TypeError):
            print(f'{cor[0]}Valor inválido, informe novamente.{cor[3]}\n{'-' * 40}')
        except KeyboardInterrupt:
            t = True
            print(f'{cor[1]}Sistema foi encerrado! :){cor[3]}.')
            break
        else:
            if q == 0:
                t = True
                break
            else:
                break

    if not t:
        print('-' * 40)

        while q > 0:

            # Tratamento na hora de informar o modelo, caso o usuário interromper, irá retornar t com um valor True, o programa já se encerrará por completo
            while True:
                try:
                    modelo = str(input('Informe o modelo do veículo: ')).strip().title()
                except (TypeError, ValueError):
                    print(f'{cor[0]}Valor inválido, por favor informe novamente.{cor[3]}\n{'-' * 40}')
                except KeyboardInterrupt:
                    t = True
                    print(f'\n{'*' * 40}\nVocê acabou de encerrar o sistema.\n{'*' * 40}')
                    sleep(2.5)
                    break
                else:
                    if modelo == '':
                        print(f'{cor[0]}Valor inválido, por favor informe novamente.{cor[3]}\n{'-' * 40}')
                    else:
                        break
                sleep(2.5)

            # Se o retorno t!= True: ele entrará no código, aqui também irá fazer a mesma coisa como o anterior fez
            # coso interromper ele retornará t com um valor True
            if not t:
                while True:
                    try:
                        placa = str(input('Informe a placa do veículo:')).strip().upper()
                    except (TypeError, ValueError):
                        print(f'{cor[0]}Valor inválido, por favor informe novamente.{cor[3]}\n{'-' * 40}')
                    except KeyboardInterrupt:
                        t = True
                        print(f'\n{'*' * 40}\nVocê acabou de encerrar o sistema.{cor[3]}\n{'*' * 40}')
                        sleep(2.5)
                        break
                    else:
                        if placa == '':
                            print(f'{cor[0]}Valor inválido, por favor informe novamente.{cor[3]}\n{'-' * 40}')
                        elif len(placa) > 8 or len(placa) < 8:
                            print(f'{cor[0]}Valor inválido, por favor informe novamente.{cor[3]}'
                                  f'\n{cor[1]}Obs.:{cor[3]} A numeração da placa tem que conter 8 caractere notal\n{'-' * 40}')
                        else:
                            break
                    sleep(2.5)

                # Se o retorno t!= True: ele entrará no código, aqui também irá fazer a mesma coisa como o anterior fez
                # coso interromper ele retornará t com um valor True
                if not t:
                    while True:
                        try:
                            cor_v = str(input('Informe a cor do veículo: ')).strip().title()
                        except (TypeError, ValueError):
                            print(f'{cor[0]}Valor inválido, por favor informe novamente.{cor[3]}\n{'-' * 40}')
                        except KeyboardInterrupt:
                            t = True
                            print(f'\n{'*' * 40}\nVocê acabou de encerrar o sistema.{cor[3]}\n{'*' * 40}')
                            sleep(2.5)
                            break
                        else:
                            if cor_v == '':
                                print(f'{cor[0]}Valor inválido, por favor informe novamente.{cor[3]}\n{'-' * 40}')
                            else:
                                break
                        sleep(2.5)

            # Se o retorno t!= True: ele entrará no código, aqui vai passar os valores para lista, que será cópiada pela lista1
            if not t:
                lista = [modelo, placa, cor_v]
                lista1.append(lista[:])
                print('-' * 40)

            # Se o t retornar True, ele encerrará o programa, porque no início
            # ele informa que vai ia cadastrar, só que ele pode ou não encerrar o programa a qualquer momento.
            if t:
                q = 0
            else:
                q -= 1

    # Após a finalização do cadastro, ele irá mostrar os dados(s) do(s) carro(s)
    # Fiz uma class dentro de uma função
    if not t:
        dados(lista1)  # A função dados vai receber a lista1 com os dados dos carros
        sleep(3)

    # Encerra o programa
    if not t == False:
        encerra()
        return '3'
    else:
        # chamando uma função para salvar os dados em txt
        salvar(modelo, placa, cor_v)
        # Caso não for encerrado, irá mostra Cadastrado com sucesso
        print(f'{cor[2]}Veículo(s) cadastrado(s) com secesso! :){cor[3]}')


def encerra():
    print(f'{cor[1]}Programa encerado pelo usuário')
