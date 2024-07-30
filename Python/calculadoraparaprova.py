B = {}
while True:
    n = int(input("Digite a quantidade de dados: "))
    if n > 1:
        break
    else:
        print("Precisa ser mais que 1")
        
X = []
Y = []

for i in range(n):
    x_value = float(input(f"Digite o {i+1}º valor de x: "))
    y_value = float(input(f"Digite o {i+1}º valor de y: "))
    X.append(x_value)
    Y.append(y_value)

sum_X = sum(X)
sum_Y = sum(Y)
sum_XQuadrado = sum(x**2 for x in X)
sum_YQuadrado = sum(y**2 for y in Y)
sum_XY = sum(x * y for x, y in zip(X, Y))

C = (n * sum_XY - sum_X * sum_Y) / ((n * sum_XQuadrado - sum_X**2) ** 0.5 * (n * sum_YQuadrado - sum_Y**2) ** 0.5)
A = (n * sum_XY - sum_X * sum_Y) / (n * sum_XQuadrado - sum_X**2)
qR = (sum_Y - A * sum_X) / n

print("\nResultados finais:")
print(f"A soma dos {n} valores de x é: {sum_X}")
print(f"A soma dos {n} valores de y é: {sum_Y}")
print(f"A soma dos {n} valores de x² é: {sum_XQuadrado}")
print(f"A soma dos {n} valores de y² é: {sum_YQuadrado}")
print(f"A soma dos {n} valores de x*y é: {sum_XY}")
print(f"A correlação destes valores é: {C}")
print(f"A regressão linear destes valores é: y = {A}x + {qR}")