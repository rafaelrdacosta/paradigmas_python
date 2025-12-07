# Variáveis locais

def multiplicador(numero):
    a = 2  # esta variável tem escopo local
    print(f'Dentro da função, a variável vale: {a}')
    return a * numero

a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f'O valor de b é: {b}')
print(f'Fora da função, a variável a vale: {a}')