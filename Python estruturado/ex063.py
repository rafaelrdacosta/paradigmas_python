# Parâmetros, procedimentos e funções

def func1(x):
    x = 10
    print(f'Função func1: x = {x}')

def func2(x):
    x = 20
    print(f'Função func2: x = {x}')

x = 0
print(f'Programa principal: x = {x}')
func1(x)
print(f'Após func1: x = {x}')
func2(x)
print(f'Após func2: x = {x}')