"""
CRUD
"""

def criar_contato():
    nome = input('Digite o nome do contato: ')
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    
    with open('contatos.txt', 'a') as file:
        file.write(f"{nome},{telefone},{email}\n")
    print('Contato criado com sucesso!')

def listar_contatos():
    try:
        with open('contatos.txt', 'r') as file:
            contatos = file.readlines()
            if contatos:
                print("Lista de contatos:")
                for contato in contatos:
                    print(contato.strip())
            else:
                print("Nenhum contato encontrado.")
    except FileNotFoundError:
        print("Nenhum contato encontrado.")

def atualizar_contato():
    nome_antigo = input('Digite o nome do contato que deseja atualizar: ')
    novo_nome = input('Digite o novo nome (ou deixe em branco para manter o mesmo): ')
    novo_telefone = input('Digite o novo telefone (ou deixe em branco para manter o mesmo): ')
    novo_email = input('Digite o novo email (ou deixe em branco para manter o mesmo): ')
    
    with open('contatos.txt', 'r') as file:
        contatos = file.readlines()
    
    with open('contatos.txt', 'w') as file:
        for contato in contatos:
            campos = contato.strip().split(',')
            if campos[0] == nome_antigo:
                campos[0] = novo_nome if novo_nome else campos[0]
                campos[1] = novo_telefone if novo_telefone else campos[1]
                campos[2] = novo_email if novo_email else campos[2]
                contato = ','.join(campos) + '\n'
            file.write(contato)
    
    print('Contato atualizado com sucesso!')

def deletar_contato():
    nome = input('Digite o nome do contato que deseja deletar: ')
    
    with open('contatos.txt', 'r') as file:
        contatos = file.readlines()
    
    with open('contatos.txt', 'w') as file:
        for contato in contatos:
            campos = contato.strip().split(',')
            if campos[0] != nome:
                file.write(contato)
    
    print('Contato deletado com sucesso!')

def main():
    while True:
        print('\nSelecione uma das opções:')
        print('1) Criar contato')
        print('2) Listar contatos')
        print('3) Atualizar contato')
        print('4) Deletar contato')
        print('5) Sair')
        opcao = input('Digite o número da opção desejada: ')
        
        if opcao == '1':
            criar_contato()
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            atualizar_contato()
        elif opcao == '4':
            deletar_contato()
        elif opcao == '5':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()
