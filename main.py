import os
from cadastro import CadastroEspecialidade, CadastroMedico, CadastroPaciente, CadastroEndereco, CadastroConsulta, CadastrarUsuario
from editar import EditarMedico, EditarPaciente, EditarEndereco
from consultar import ConsultarEndereco, ConsultarEspecialidade, ConsultarMedico, ConsultarPaciente
from excluir import ExcluirEspecialidade, ExcluirMedico, ExcluirPaciente, ExcluirEndereco
from login import FazerLogin

loop = True
while loop == True:
    opc = input("Faça Login [1] ou Crie uma conta [2]: ")

    if opc == '1':
        loop = FazerLogin()

    elif opc == '2':
        CadastrarUsuario()
        
    else:
        print("Opção inválida, tente novamente...")

while(True):       
    print("\n")
    print("Bem vindo ao sistema da clínica")
    print("\n")
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
            print("------------------------")
            print("Opção 1 - Especialidades")
            print("Opção 2 - Médico")
            print("Opçãp 3 - Pacientes")
            print("Opção 4 - Endereço")
            print("Opção 5 - Sair")
            print("------------------------")

            opc = input("\nDigite a opção desejada: ")

            if opc == '1':
                CadastroEspecialidade()
                break

            elif opc == '2':
                CadastroMedico()
                break

            elif opc == '3':        
                CadastroPaciente()
                break

            elif opc == '4':
                CadastroEndereco()
                break

            elif opc == '5':
                break

            else:
                os.system('cls')
                print("Opção Inválida, tente novamente")
    
    elif opc == '2':
        CadastroConsulta()
        break

    elif opc == '3':
        os.system('cls')

        while(True):
            print("------------------------")
            print("Opção 1 - Médico")
            print("Opçãp 2 - Pacientes")
            print("Opção 3 - Endereço")
            print("Opção 4 - Sair")
            print("------------------------")

            opc = input("\nDigite a opção desejada: ")

            if opc == '1':
                EditarMedico()
                break

            elif opc == '2':
                EditarPaciente()
                break

            elif opc == '3':        
                EditarEndereco()
                break
            elif opc == '4':
                break
            else:
                os.system('cls')
                print("Opção Inválida, tente novamente")       

    elif opc == '4':
            print("------------------------")
            print("Opção 1 - Especialidades")
            print("Opção 2 - Médico")
            print("Opçãp 3 - Pacientes")
            print("Opção 4 - Endereço")
            print("Opção 5 - Sair")
            print("------------------------")
            opc = input("O que deseja consultar: ")

            if opc == '1':
                ConsultarEspecialidade()
                break

            elif opc == '2':
                ConsultarMedico()
                break
            
            elif opc == '3':
                ConsultarPaciente()
                break

            elif opc == '4':
                ConsultarEndereco()
                break
            elif opc == '5':
                break
            else:
                os.system('cls')
                print("Opção inválida")
    
    elif opc == '5':
        print("------------------------")
        print("Opção 1 - Especialidades")
        print("Opção 2 - Médico")
        print("Opçãp 3 - Pacientes")
        print("Opção 4 - Endereço")
        print("Opção 5 - Sair")
        print("------------------------")
        opc = input("O que deseja excluir: ")

        if opc == '1':
            ExcluirEspecialidade()
            break

        elif opc == '2':
            ExcluirMedico()
            break
        
        elif opc == '3':
            ExcluirPaciente()
            break

        elif opc == '4':
            ExcluirEndereco()
            break
        elif opc == '5':
            break
        else:
            os.system('cls')
            print("Opção inválida") 


    elif opc == '6':
        print("Fechando....")
        exit()