import os
import getpass
from cadastro import cadastro_especialidade, cadastro_medico, cadastro_paciente, cadastro_endereco, cadastro_consulta
from editar import editar_medico, editar_paciente, editar_endereco
from consultar import consultar_endereco, consultar_especialidade, consultar_medico, consultar_paciente
from excluir import excluir_especialidade, excluir_medico, excluir_paciente, excluir_endereco
from usuario import fazer_login, cadastro_usuario, check_senha

loop = True
while loop:
    opc = input("Fazer Login [1], Criar uma conta [2], Entrar sem login [3] ou Sair [4]: ")

    if opc == '1':
        print("------------------------")
        user = input("Digite o username: ")
        senha = getpass.getpass("Digite sua senha: ")
        print("------------------------\n")
        loop = fazer_login(user, senha)


    elif opc == '2':
        print("------------------------")
        user = input("Digite o novo username: ")
        senha = getpass.getpass("Digite a senha: ")
        print("------------------------\n")
        loop = cadastro_usuario(user, senha)
    
    elif opc == '3':
        loop = False
    
    elif opc == '4':
        os.system('cls')
        exit()
    else:
        os.system('cls') 
        print("Opção inválida, tente novamente...")

print("\n")
print("Bem vindo ao sistema da clínica")
print("\n")


while(True):       
    print("\nMENU PRINCIPAL")
    print("------------------------")
    print("Opção 1 - Cadastro")
    print("Opção 2 - Agendar Consulta")
    print("Opçãp 3 - Editar")
    print("Opção 4 - Consultar")
    print("Opção 5 - Excluir")
    print("Opção 6 - Sair")
    print("------------------------")
    
    opc = input("\nDigite a opção desejada: ")
    
    if opc == '1':
        os.system('cls')

        while(True):
            print("     CADASTRAR")
            print("------------------------")
            print("Opção 1 - Especialidades")
            print("Opção 2 - Médico")
            print("Opçãp 3 - Pacientes")
            print("Opção 4 - Endereço")
            print("Opção 5 - Sair")
            print("------------------------")

            opc = input("\nDigite a opção desejada: ")
            

            if opc == '1':
                cadastro_especialidade()

            elif opc == '2':
                cadastro_medico()

            elif opc == '3':        
                cadastro_paciente()

            elif opc == '4':
                cadastro_endereco()

            elif opc == '5':
                break

            else:
                os.system('cls')
                print("Opção Inválida, tente novamente")
    
    elif opc == '2':
        cadastro_consulta()

    elif opc == '3':
        os.system('cls')

        while(True):
            print("        EDITAR")
            print("------------------------")
            print("Opção 1 - Médico")
            print("Opçãp 2 - Pacientes")
            print("Opção 3 - Endereço")
            print("Opção 4 - Sair")
            print("------------------------")

            opc = input("\nDigite a opção desejada: ")

            if opc == '1':
                editar_medico()
                
            elif opc == '2':
                editar_paciente()

            elif opc == '3':        
                editar_endereco()
                
            elif opc == '4':
                break
            else:
                os.system('cls')
                print("Opção Inválida, tente novamente")       

    elif opc == '4':
            os.system('cls')
            while(True):
                print("      CONSULTAR")
                print("------------------------")
                print("Opção 1 - Especialidades")
                print("Opção 2 - Médico")
                print("Opçãp 3 - Pacientes")
                print("Opção 4 - Endereço")
                print("Opção 5 - Sair")
                print("------------------------")
                opc = input("O que deseja consultar: \n")

                if opc == '1':
                    consultar_especialidade()

                elif opc == '2':
                    consultar_medico()
                
                elif opc == '3':
                    consultar_paciente()

                elif opc == '4':
                    consultar_endereco()
                    
                elif opc == '5':
                    break
                else:
                    os.system('cls')
                    print("Opção inválida")
    
    elif opc == '5':
        os.system('cls')
        while(True):
            print("        EXCLUIR")
            print("------------------------")
            print("Opção 1 - Especialidades")
            print("Opção 2 - Médico")
            print("Opçãp 3 - Pacientes")
            print("Opção 4 - Endereço")
            print("Opção 5 - Sair")
            print("------------------------")
            opc = input("O que deseja excluir: ")

            if opc == '1':
                excluir_especialidade()

            elif opc == '2':
                excluir_medico()
            
            elif opc == '3':
                excluir_paciente()

            elif opc == '4':
                excluir_endereco()
                
            elif opc == '5':
                break

            else:
                os.system('cls')
                print("Opção inválida") 


    elif opc == '6':
        print("Fechando....")
        exit()