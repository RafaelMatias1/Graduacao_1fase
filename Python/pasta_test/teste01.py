


print('Bem vindo ao sistema de agendamento de consultas')
print('Selecione uma das opções abaixo:')
print()
print('1) Listar consultas agendadas')
print('2) Agendar nova consulta')
print('3) Desmarcar uma consulta')
print()
opcao_menu = input('Digite a opção desejada: ')

if int(opcao_menu) == 1:
    print('Ver consultas marcadas')

elif int(opcao_menu) == 2:
    print('Você está na área de agendamento de consultas!')
    print('Responda as seguintes perguntas para realizar o agendamento')
    nome = input('Qual o seu nome? ')
    telefone = input('Qual o seu número de telefone? ')
    email = input('Qual o seu e-mail? ')
    sexo = input('Qual o seu sexo? ')
    plano_saude = input('Qual o seu plano de saúde? ')
    dia = input('Qual o dia seria melhor para o agendamento da sua consulta? ')
    hora = input('Qual o melhor horário para a sua consulta no dia? ')

    with open('consultas.txt', 'a') as file:
        file.write(f"Nome: {nome}, Telefone: {telefone}, Email: {email}, Sexo: {sexo}, Plano de Saúde: {plano_saude}, Dia: {dia}, Hora: {hora}\n")
    print(nome, 'a sua consulta foi marcada para', dia, 'no horário', hora)
    print()

elif int(opcao_menu) == 3:
    print('Desmarcar uma consulta')
    