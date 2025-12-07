# Variáveis globais e locais

def multiplicador(numero):
    return a * numero

a = 3 # esta variável tem escopo global
b = multiplicador(5)
print(f'O valor de b é: {b}')
