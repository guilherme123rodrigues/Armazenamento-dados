from interface.menu import *

while True:
    r = menu(['Mostrar Cadastro', 'Novo Cadastro', 'Sair'])
    if r == 3:
        cabe('Saindo do sistema...Até logo!')
        linha()
        sleep(2)
        break
