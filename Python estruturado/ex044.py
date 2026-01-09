# Estrutura de repetição while
print('Antes do while')
palavra = input('Entre com uma palavra: ')
while palavra != 'sair':
    print('Dentro do while')
    palavra = input('Digite sair para encerrar o laço: ')
print('Você digitou sair e agora está fora do laço.')