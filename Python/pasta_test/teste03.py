def criar_paciente():
    nome = input('Digite o nome do paciente: ')
    idade = input('Digite a idade do paciente: ')
    telefone = input('Digite o telefone do paciente: ')
    email = input('Digite o email do paciente: ')
    sexo = input('Digite o sexo do paciente: ')
    
    with open('pacientes.txt', 'a') as file:
        file.write(f"{nome},{idade},{telefone},{email},{sexo}\n")
    print('Paciente cadastrado com sucesso!')

def listar_pacientes():
    try:
        with open('pacientes.txt', 'r') as file:
            pacientes = file.readlines()
            if pacientes:
                print("Lista de pacientes:")
                for paciente in pacientes:
                    print(paciente.strip())
            else:
                print("Nenhum paciente cadastrado.")
    except FileNotFoundError:
        print("Nenhum paciente cadastrado.")

def atualizar_paciente():
    nome_antigo = input('Digite o nome do paciente que deseja atualizar: ')
    novo_nome = input('Digite o novo nome (ou deixe em branco para manter o mesmo): ')
    nova_idade = input('Digite a nova idade (ou deixe em branco para manter a mesma): ')
    novo_telefone = input('Digite o novo telefone (ou deixe em branco para manter o mesmo): ')
    novo_email = input('Digite o novo email (ou deixe em branco para manter o mesmo): ')
    novo_sexo = input('Digite o novo sexo (ou deixe em branco para manter o mesmo): ')
    
    with open('pacientes.txt', 'r') as file:
        pacientes = file.readlines()
    
    with open('pacientes.txt', 'w') as file:
        for paciente in pacientes:
            campos = paciente.strip().split(',')
            if campos[0] == nome_antigo:
                campos[0] = novo_nome if novo_nome else campos[0]
                campos[1] = nova_idade if nova_idade else campos[1]
                campos[2] = novo_telefone if novo_telefone else campos[2]
                campos[3] = novo_email if novo_email else campos[3]
                campos[4] = novo_sexo if novo_sexo else campos[4]
                paciente = ','.join(campos) + '\n'
            file.write(paciente)
    
    print('Paciente atualizado com sucesso!')

def deletar_paciente():
    nome = input('Digite o nome do paciente que deseja deletar: ')
    
    with open('pacientes.txt', 'r') as file:
        pacientes = file.readlines()
    
    with open('pacientes.txt', 'w') as file:
        for paciente in pacientes:
            campos = paciente.strip().split(',')
            if campos[0] != nome:
                file.write(paciente)
    
    print('Paciente deletado com sucesso!')

def main():
    while True:
        print('\nSelecione uma das opções:')
        print('1) Cadastrar paciente')
        print('2) Listar pacientes')
        print('3) Atualizar paciente')
        print('4) Deletar paciente')
        print('5) Sair')
        opcao = input('Digite o número da opção desejada: ')
        
        if opcao == '1':
            criar_paciente()
        elif opcao == '2':
            listar_pacientes()
        elif opcao == '3':
            atualizar_paciente()
        elif opcao == '4':
            deletar_paciente()
        elif opcao == '5':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()
