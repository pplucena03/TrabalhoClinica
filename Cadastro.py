import os
from datetime import date
def Cadastro (escolha):
    while(True):        
            print("------------------------")
            print("Opção 1 - Especialidades")
            print("Opção 2 - Médico")
            print("Opçãp 3 - Pacientes")
            print("Opção 4 - Endereço")
            print("------------------------")
            
            escolha = input()
        
            if escolha == '1':
                os.system('cls')
                especialidade = input("Especialidades para um médico: ")
                pass
            elif escolha == '2':
                nome_medico = input("Qual o nome do Médico: ")
                crm = input(f"Qual o CRM do do {nome_medico}: ")
                data_nasc = input(f"Qual a data de nascimento do {nome_medico}: ")
                sexo_med = input(f"Qual o sexo do médico {nome_medico}: ")
                numero = input(f"Qual o numero do médico {nome_medico}: ")
                
                print(f"nome do Médico:{nome_medico}")
                print(f"CRM do Médico:{crm}")
                print(f"data de nascimento do Médico:{data_nasc}")
                print(f"sexo do Médico:{sexo_med}")
                print(f"numero do Médico:{numero}")
                print(f"especialidade médico {especialidade}")
                pass
            elif escolha == '3':
                os.system('cls')
                nome_paciente = input("Qual o nome do paciente: ")
                data_paciente = input("Qual a data de nascimento do paciente: ")
                sexo_paciente = input("Qual o sexo do paciente: ")
                telefone = input("Qual o numero do paciente: ")
                 
                print(f"nome do Paciente:{nome_paciente}")
                print(f"data de nascimento do Paciente:{data_paciente}")
                print(f"sexo do Paciente:{sexo_paciente}")
                print(f"numero do Paciente:{telefone}")
                
            elif escolha == '4':
                os.system('cls')
                rua = input("Qual a rua que o paciente mora: ")
                bairro = input("Qual bairro o paciente mora: ")
                cidade = input("Qual cidade o paciente mora: ")
                
                print(f"rua: {rua}")
                print(f"bairoo: {bairro}")
                print(f"cidade: {cidade}")
            else:
                os.system('cls')
                print("Opção Invalida, tente novamente")
     