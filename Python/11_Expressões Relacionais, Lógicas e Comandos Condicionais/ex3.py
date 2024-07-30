"""
    Exercicio 3

     Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
    salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
    15%.
"""
salario = float(input("Digite o seu salario recebido nesse mes"))

if salario > 1250:
    print("salario teve um aumento de 10%")
elif salario <= 1250:
    print("O seu salario deve diminuir 15%")
else:
    print("Seu salario nao teve alteração")
