"""
    Exercicio 5

    Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
    Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado
    da operação solicitada.
"""

numeroUm = float(input("Digite o primeiro numero para o calculo"))
numeroDois = float(input("Digite o segundo numero para o calculo"))

calculoUm = numeroUm + numeroDois

calculoDois = numeroUm - numeroDois

calculoTres = numeroUm * numeroDois

calculoQuatro = numeroUm / numeroDois

print("O peimeiro calculo deu:", calculoUm, "\nO segundo calculo deu:", calculoDois, "\n O terceiro calculo deu:", calculoTres, "\n O quarto calculo deu:", calculoQuatro)

