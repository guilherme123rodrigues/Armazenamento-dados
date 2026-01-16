from estacionamento.funções import dados

def ler():
    lista = []
    try:
        with open("veiculo.txt", "r", encoding="utf-8") as arquivo:
            for c in arquivo:
                if ';' in c:
                    r = c.strip().split(';')
                    lista.append(r)
    except FileNotFoundError:
        pass
    else:
        dados(lista)


def salvar(modelo, placa, cor):
    with open("veiculo.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f'{modelo};{placa};{cor}\n')
