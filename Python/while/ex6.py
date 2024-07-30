"""6) Faça um programa para exibir os resultados no mesmo formato de uma tabuada de um número
fornecido pelo usuário: 2x1 = 2, 2x2 = 4, …"""

numero = int(input('Digite o número para saber qual a sua tabuada:'))


for index1 in range(1, 11):
    resultado = numero * index1
    print(f'{numero} x {index1} = {resultado}')