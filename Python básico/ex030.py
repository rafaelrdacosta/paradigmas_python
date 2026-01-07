# Atribuição de valores a variáveis
nome = 'Alice'
idade = 30

# Entrada de dados do usuário
altura = float(input('Digite a sua altura em metros: '))
peso = float(input('Digite o seu peso em kg: '))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Saída de dados formatada
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Altura: {altura:.2f}m')
print(f'Peso: {peso:.1f}kg')
print(f'IMC: {imc:.2f}')