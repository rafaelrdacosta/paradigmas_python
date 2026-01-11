# Parâmetros, procedimentos e funções

def taximetro(distancia, multiplicador=1):
    # multiplicador = 1 -> default, se não for passado esse parâmetro
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor

pagamento = taximetro(3.5)
print(f'Valor corrida: R$ {pagamento:.2f}')