# Parâmetros, procedimentos e funções

def calcula_imc(peso, altura):
    return peso * 100 / (altura * 2)

peso = eval(input('Digite o peso em quilos: '))
altura = eval(input('Digite a altura em centímetros: '))
calcula_imc(peso, altura)
imc = calcula_imc(peso, altura)
print(f'IMC = {imc:.2f}')