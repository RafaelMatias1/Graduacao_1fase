def data_por_extenso(data):
    meses = {
        1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 
        5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 
        9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'
    }
    dia, mes, ano = map(int, data.split('/'))
    return f"{dia} de {meses[mes]} de {ano}"

data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

print("Data de nascimento por extenso:", data_por_extenso(data_nascimento))
