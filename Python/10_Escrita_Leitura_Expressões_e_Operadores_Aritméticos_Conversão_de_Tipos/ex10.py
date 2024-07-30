"""
    Exercicio 10

    Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar. 


"""

preco_mercadoria = float(input("Digite o preço da mercadoria: "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))

valor_desconto = preco_mercadoria * (percentual_desconto / 100)

preco_pagar = preco_mercadoria - valor_desconto

print("O valor do desconto é: R$", valor_desconto)
print("O preço a pagar é: R$", preco_pagar)
