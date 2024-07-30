"""
    Exercicio 1

    Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80
    km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa,
    cobrando R$ 5 por km acima de 80 km/h.
"""

carro = int(input("Digite a velocidade do carro:"))
if(carro > 80):

    print("Voce recebera uma multa no  valor de R$5 por esta a cima de 80Km/h")

else:

    print("voce estava a baixo de 80KM/h fique tranquilo nao recebera multa")

