# Parâmetros, procedimentos e funções

def taximetro(distancia):
    def calculaMult():
        if distancia < 5:
            return 1.2
        else:
            return 1
    multiplicador = calculaMult()
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor

distancia = eval(input('Informe a distância percorrida em km: '))
pagamento = taximetro(distancia)
print(f'O valor da corrida é R$ {pagamento:.2f}')