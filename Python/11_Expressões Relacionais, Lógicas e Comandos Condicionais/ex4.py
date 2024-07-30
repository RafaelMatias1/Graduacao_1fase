"""
    Exercicio 4

    Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
    Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45
    para viagens mais longas.
"""
distância = float(input("Digite a distância da viagem que percorrerá em KM: "))

if distância <= 200:

    viagem = distância * 0.45
    print("O preço da viagem é:", viagem)

else:

    viagem = distância * 0.50
    print("O preço da viagem é:", viagem)
