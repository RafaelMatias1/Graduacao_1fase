def Palíndromo(frase):
    frase = frase.replace(' ', '').lower()
    return frase == frase[::-1]

sequencia = input("Digite uma sequência de caracteres: ")

if Palíndromo(sequencia):
    print(f'"{sequencia}" é palíndromo.')
else:
    print(f'"{sequencia}" não é palíndromo.')
