


# Inicializando a lista de agendamentos fora do bloco condicional (ele precisa ser iniciado fora do LOOP)
agendamentos = {}

while True: #loop

# Menu de entrada
    print('Bem vindo ao sistema de agendamento de consultas')
    print('Selecione uma das opções abaixo:')
    print()
    print('1) Listar consultas agendadas')
    print('2) Agendar nova consulta')
    print('3) Desmarcar uma consulta')
    print('4) Sair')
    print()
    opcao_menu = input('Digite a opção desejada: ')  

# Lista de consultas marcadas
    if int(opcao_menu) == 1:  
        print()
        print('Lista de consultas agendadas:')
        print()

        if not agendamentos: #se não tem agendamento mostre:
            print('Não há nenhuma consulta agendada!')
            print()
        else:

# Utilizando vetor dentro de vetor = MATRIZ 
#criação de um mini loop        

            for ind in agendamentos: #mas se tiver agendamentos, mostre o INDEX (agendamento = data e hora) 
                print('=======================================')
                print("Data e hora: " + ind)
                for ind2 in agendamentos[ind]: 
                    print("    " + ind2 + ": " + agendamentos[ind][ind2]) # mostre o segundo INDEX (os index dentro e suas respostas ex: nome: Julia)
                print()

        input('Pressione enter para continuar ')

# Agendar consultas
    elif int(opcao_menu) == 2: 
        print('Você está na área de agendamento de consultas!')
        print('Responda as seguintes perguntas para realizar o agendamento: ')

#váriaveis com as perguntas para o cadastro do cliente mais a consulta
        nome = input('Qual o seu nome? ')
        data_nascimento = input('Qual a sua data de nascimento? ')
        telefone = input('Qual o seu número de telefone? ')
        email = input('Qual o seu e-mail? ')
        sexo = input('Qual o seu sexo? ')
        plano_saude = input('Qual o seu plano de saúde? ')
        objetivo_consulta = input('Qual o objetivo da sua consulta? ')

#loop para caso já estejá marcada a consulta para o mesmo dia e o mesmo horário 
        while True:
            dia = input('Qual o dia seria melhor para o agendamento da sua consulta? ')
            hora = input('Qual o melhor horário para a sua consulta no dia? ')

            if dia + ' ' +  hora in agendamentos:
                print('Esse horário nesse dia não está disponível para agendamento, por favor indique outro.')
            else:
                break
# Finalização 
        print()
        print('A Consulta para ' + nome + ' foi marcada para ' + dia + ' no horário ' + hora)
        print()
        
        dados_paciente = {'nome': nome, 'data_nascimento': data_nascimento, 'telefone': telefone, 'email': email, 'sexo': sexo, 'plano_saude': plano_saude, 'objetivo_consulta': objetivo_consulta}

# Adicionando o agendamento atual à lista de agendamentos
        agendamentos[dia + ' ' +  hora] = dados_paciente

        input('Precione enter para continuar ')

    elif int(opcao_menu) == 3:

#criação de um mini loop       
 
        for ind in agendamentos:
            print(ind)  #mostrar o itens que esão no INDEX 

        agendamento_del = input('Informe qual a data e hora deseja desmarcar ou pressione Enter para cancelar: ')

        if agendamento_del:  # Verifica se o usuário forneceu uma data e hora para desmarcar

            if agendamento_del in agendamentos: # a váriavel criada antes (agendamento_del) vai usar o dados do INDEX agendamento 


                confirmacao = input('Tem certeza que deseja desmarcar essa consulta para o ' + dia + ' no horário ' + hora + '? (s/n): ') #confirmar se o usuário quer excluir essa data

                if confirmacao.lower() == 's': #a confirmaçao do usuário é necessária para deletar a data e hora marcada
                    del agendamentos[agendamento_del]
                #lower() irá converter essa entrada para minúsculas antes de compará-la com 's'.
                 
                    print('O agendamento foi excluído.')
                
                else:
                    print('Operação de desmarcar consulta cancelada.')
            
            else:
                print('O agendamento selecionado não foi encontrado.')
        
        else:
            print('Operação de desmarcar consulta cancelada.')

        input('Precione enter para continuar ')

    elif int(opcao_menu) == 4:
        break