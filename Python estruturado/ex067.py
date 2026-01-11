# Parâmetros, procedimentos e funções
def maior_elemento(lista):
    if len(lista) <= 1:
        return lista[0]

    maior = lista[0]

    for num in lista[1:]:
        if num > maior:
            maior = num
    return maior

lista = [7, 2, 5, 1, 4, 3, 6]
maior = maior_elemento(lista)
print(f'O maior número na lista é: {maior}')