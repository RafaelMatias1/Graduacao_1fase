def criar_consulta():
    print('Apresente as suas informalçoes:')

    nome = input('Digite o nome: ')
    idade = input('Digite a sua idade:')
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    
    with open('consulta.txt', 'a') as file:
        file.write(f"{nome},{idade},{telefone},{email}\n")
    print('consulta criado com sucesso!')

def listar_consulta():
    try:
        with open('consulta.txt', 'r') as file:
            consulta = file.readlines()
            if consulta:
                print("Lista de consulta:")
                for consultas in consulta:
                    print(contato.strip())
            else:
                print("Nenhum contato encontrado.")
    except FileNotFoundError:
        print("Nenhum contato encontrado.")

def atualizar_consulta():
    nome_antigo = input('Digite o nome da consulta que deseja atualizar: ')
    novo_nome = input('Digite o novo nome (ou deixe em branco para manter o mesmo): ')
    novo_idade = input('Digite a sua nova idade(ou deixe em branco para manter o mesmo):')
    novo_telefone = input('Digite o novo telefone (ou deixe em branco para manter o mesmo): ')
    novo_email = input('Digite o novo email (ou deixe em branco para manter o mesmo): ')
    
    with open('consulta.txt', 'r') as file:
        consulta = file.readlines()
    
    with open('contatos.txt', 'w') as file:
        for consultas in consulta:
            campos = consulta.strip().split(',')
            if campos[0] == nome_antigo:
                campos[0] = novo_nome if novo_nome else campos[0]
                campos[1] = novo_idade if novo_idade else campos[1]
                campos[2] = novo_telefone if novo_telefone else campos[2]
                campos[3] = novo_email if novo_email else campos[3]
                consulta = ','.join(campos) + '\n'
            file.write(consulta)
    
    print('Contato atualizado com sucesso!')
