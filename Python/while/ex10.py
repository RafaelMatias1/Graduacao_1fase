"""10) Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no
período."""

depo_inicial = float(input('Qual o depósito inicial? '))
taxa = float(input('Qual a taxa de juros dessa poupança? ')) / 100  


total_ganho = 0  


for mes in range(1, 25):
    juros = depo_inicial * taxa
    total_ganho += juros  
    depo_inicial += juros  
    print(f'No mês {mes}, o percentual de juros foi igual a {juros:.2f} e o total acumulado foi de {depo_inicial:.2f}')


print(f'O total ganho com juros no período de 24 meses foi de {total_ganho:.2f}')



