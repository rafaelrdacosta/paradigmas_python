# Uso da função eval e da clausula try-except

def calcular_expressao():
    expressao = input('Digite uma expressão matemática: ')

    try:
        # Avaliar a expressão usando eval
        resultado = eval(expressao)
        print('O resultado da expressão é: ', resultado)
    except Exception as e:
        print('Erro ao avaliar a expressão: ', e)

# Chamar a função
calcular_expressao()

