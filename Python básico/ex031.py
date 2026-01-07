# Definição preços produtos
hamburguer = 10.50
batata_frita = 4.00
refrigerante = 3.00

# Entrada de dados usuário
quantidade_hamburger = int(input('Digite a quantidade de hambúrgueres desejados: '))
quantidade_batata = int(input('Digite a quantidade de batatas fritas desejadas:  '))
quantidade_refrigerante = int(input('Digite a quantidade de refrigerante desejados: '))

# Cálculo do preço total
preco_total = (hamburguer * quantidade_hamburger) + (batata_frita * quantidade_batata) + (refrigerante * quantidade_refrigerante)

# Exibição do preço do pedido
print(f'O preço total do seu pedido é R$ {preco_total:.2f}')