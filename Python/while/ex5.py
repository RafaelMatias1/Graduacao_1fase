"""5) Faça um programa para escrever os 10 primeiros múltiplos de 3."""

contagem = 0


numero = 1


while contagem < 10:
    if numero % 3 == 0:
        print(numero)
        contagem += 1
    numero += 1
