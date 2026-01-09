# Estrutura de repetição while
while True: #cria um laço infinito
    print('loop')
    palavra = input('Entre com uma palavra: ')
    if palavra == 'sair':
        break
print('Você digitou sair e agora está fora do laço.')