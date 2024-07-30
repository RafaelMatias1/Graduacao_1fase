"""7) Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada,
em vez de começar com 1 e 10."""

numero1 = int(input('Digite o número para saber qual a sua tabuada: '))
numero2 = int(input(f'Digite um número para multiplicar o número {numero1}: '))
resultado = numero1 * numero2
print(f'{numero1} x {numero2} = {resultado}')
