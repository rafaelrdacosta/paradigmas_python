"""
Busca recursivamente o maior elemento em uma lista de inteiros.
"""
def busca_maior(lista):
    if len(lista) == 1:
        return lista[0]
    #chamada recursiva: encontra o maior elemento do resto da lista
    maior_do_resto = busca_maior(lista[1:])

    if lista[0] > maior_do_resto:
        return lista[0]
    else:
        return maior_do_resto

# Exemplo de uso
lista = [52, 1, 8, 24, 4, 5]
maior = busca_maior(lista)
print(f"O maior elemento da lista é: {maior}")