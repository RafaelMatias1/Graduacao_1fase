"""
    Exercicio 11

    Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.


"""

distancia = float(input("Digite a distância a percorrer (em quilômetros): "))
velocidade_media = float(input("Digite a velocidade média esperada (em km/h): "))

tempo_horas = distancia / velocidade_media

print("O tempo de viagem previsto é de aproximadamente", tempo_horas, "horas.")
