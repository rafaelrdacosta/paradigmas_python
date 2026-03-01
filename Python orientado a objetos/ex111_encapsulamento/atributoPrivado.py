'''Burlando atributos privados
Python não possui atributos privados reais
'''

from Classes.Conta import Conta

conta = Conta(1, 1000)

#Burlando o atributo conta privado
#_nomedaclasse__atributo
saldo1 = conta._Conta__saldo
print(saldo1)

#Irá dar erro porque o atributo saldo é privado
saldo2 = conta.saldo
print(saldo2)