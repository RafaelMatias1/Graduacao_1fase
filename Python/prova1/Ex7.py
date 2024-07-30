def corrigir_numero_telefone(telefone):
    telefone = ''.join(filter(str.isdigit, telefone))

    if len(telefone) == 7:
        telefone_corrigido = '3' + telefone
        return telefone_corrigido
    else:
        return telefone

telefone = input("Digite o número de telefone: ")

telefone_corrigido = corrigir_numero_telefone(telefone)
print("Número de telefone corrigido:", telefone_corrigido)
