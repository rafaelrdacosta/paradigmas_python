# Python estruturado - elif
vnr = eval(input('Digite um número: '))
print('Valor digitado: ', vnr)
print('Antes do if.')

if vnr <= 100:
    print('Entrou no if do 100')
elif vnr <= 500:
    print('Entrou no elif do 500')
else:
    print('Entrou no else.')