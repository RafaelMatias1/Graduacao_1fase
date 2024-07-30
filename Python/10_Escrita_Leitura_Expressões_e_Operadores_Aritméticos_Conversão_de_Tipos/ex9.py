"""
    Exercicio 9

    Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário. 

"""

salario_atual = float(input("Digite o valor do salário atual: "))
porcentagem_aumento = float(input("Digite a porcentagem do aumento: "))

aumento = salario_atual * (porcentagem_aumento / 100)

novo_salario = salario_atual + aumento

print("O valor do aumento é: R$", aumento)
print("O novo salário é: R$", novo_salario)
