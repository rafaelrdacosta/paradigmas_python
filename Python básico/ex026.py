# Solicitação de dados ao usuário
num = int(input('Digite um número inteiro: '))
flutuante = float(input('Digite um número de ponto flutuante: '))
booleano = bool(input('Digite um valor booleano (True ou False): '))


# Exibição dos valores convertidos
print(f'\nNúmero inteiro: {num} (tipo: {type(num)})')
print(f'Número de ponto flutuante: {flutuante:.2f} (tipo: {type(flutuante)}')
print(f'Valor booleano: {booleano} (tipo: {type(booleano)})')