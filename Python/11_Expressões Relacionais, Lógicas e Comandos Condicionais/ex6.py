"""
    Exercicio 6

    Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O
    programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O
    valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação
    como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
"""
def calcular_prestacao(valor_casa, salario, anos):
    meses = anos * 12
    prestacao = valor_casa / meses
    return prestacao

def aprovar_emprestimo():
    valor_casa = float(input("Digite o valor da casa a comprar: "))
    salario = float(input("Digite o salário: "))
    anos = int(input("Digite a quantidade de anos a pagar: "))

    prestacao_maxima = salario * 0.3

    prestacao = calcular_prestacao(valor_casa, salario, anos)

    if prestacao <= prestacao_maxima:
        print("Empréstimo aprovado! Prestação mensal: R$", round(prestacao, 2))
    else:
        print("Empréstimo negado! Prestação mensal excede 30% do salário.")

aprovar_emprestimo()
