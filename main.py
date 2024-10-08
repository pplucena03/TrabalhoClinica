import os
from Cadastro import Cadastro
from Editor import Editor
from Consulta import consulta


while(True):
    print("\n")
    print("bem vindo ao sistema ...")
    print("\n")
    print("------------------------")
    print("Opção 1 - Cadastro")
    print("Opção 2 - Agendar Consulta")
    print("Opçãp 3 - Editar")
    print("Opção 4 - Consultas Agendadas")
    print("Opção 5 - Excluir")
    print("------------------------")
    
    opc = input()
    
    if opc == '1':
        os.system('cls')
        Cadastro(opc)
        break
    elif opc == '2':
        print("teste")
    elif opc == '3':        
        Editor(opc)
    elif opc == '4':
        consulta(opc)
    elif opc == '5':
        print("teste5")
    else:
        print("Opção Invalida. tente uma opção valida")