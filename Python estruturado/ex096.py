'''numero = 10
letra = 'a'
resultado = numero + letra
print(resultado)'''

#Correção do erro tipo: conversão da letra para número antes da soma
numero = 10
letra = 'A'

#Convertendo a letra para um número interiro usando a função ord()
numero_letra = ord(letra) - ord('a') + 1

#Realizando a soma corretamente
resultado = numero + numero_letra
print(resultado)