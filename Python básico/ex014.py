# Variável de escopo global
mensagem_global = 'Eu sou uma variável global'

def minha_funcao():
    # Variável de escopo local
    mensagem_local = 'Eu sou uma variável local'
    print(mensagem_local)

minha_funcao()

# Se tentarmos acessar a variável local fora da função causará um erro
# print(mensagem_local)

# Variável global ainda é acessível
print(mensagem_global)