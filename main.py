import os
from Cadastro import Cadastro
from Editor import Editor

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
        
        print("------------------------")
        print("Opção 1 - Médico")
        print("Opção 2 - Especialidades")
        print("Opçãp 3 - Pacientes")
        print("Opção 4 - Endereço")
        print("------------------------")
        
        escolha = input()
        Cadastro(escolha)
        break
    elif opc == '2':
        print("teste")
    elif opc == '3':
        
        print("O que você quer editar: \n")
        print("------------------------")
        print("Opção 1 - Médico")
        print("Opçãp 2 - Pacientes")
        print("Opção 3 - Endereço")
        print("------------------------")
        
        escolha_editor = input()
        
        Editor(escolha_editor)
        
    elif opc == '4':
        print("teste4")
    elif opc == '5':
        print("teste5")
    else:
        print("Opção Invalida. tente uma opção valida")