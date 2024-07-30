"""8) Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro
pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado.
Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de
um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4."""


numero1 = int(input('Digite o número para saber qual a sua tabuada: '))
numero2 = int(input(f'Digite um número para multiplicar o número {numero1}: '))


resultado = 0
# Somar o número1 a si mesmo número2 vezes
for _ in range(numero2):
    resultado += numero1


print(f'{numero1} x {numero2} = {resultado}')


