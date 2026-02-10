'''Escreva uma função que busca recursivamente o
maior elemento em uma lista de números inteiros.'''

def busca_maior(lista):
    if len(lista) == 1:
        return lista[0]
    maior = lista[0]
    for i in range (0, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior

lista = [13, 1, 8, 24, 4, 5]
maior = busca_maior(lista)
print(maior)
