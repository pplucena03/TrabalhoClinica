import os
from Cadastro import CadastroEspecialidade, CadastroMedico, CadastroPaciente, CadastroEndereco
from Editor import Editor

while(True):
    print("\n")
    print("Bem vindo ao sistema da clínica")
    print("\n")
    print("------------------------")
    print("Opção 1 - Cadastro")
    print("Opção 2 - Agendar Consulta")
    print("Opçãp 3 - Editar")
    print("Opção 4 - Consultas Agendadas")
    print("Opção 5 - Excluir")
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
            print("------------------------")

            opc = input("\nDigite a opção desejada: ")

            if opc == '1':
                if CadastroEspecialidade():
                    break

            elif opc == '2':
                CadastroMedico()

            elif opc == '3':        
                CadastroPaciente()

            elif opc == '4':
                CadastroEndereco()

            else:
                os.system('cls')
                print("Opção Inválida, tente novamente")