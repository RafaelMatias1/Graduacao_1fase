nome = input("digite o eu nome:")

lestras_escada = ''

for letras in reversed(nome):
    lestras_escada += letras
    print(lestras_escada)