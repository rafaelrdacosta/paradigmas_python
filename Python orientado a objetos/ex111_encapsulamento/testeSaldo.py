'''Como evitar alteração indevida no saldo?
Definindo atributos públicos e privados
O uso de -- indica que um atributo é privado, ou seja,
somente pode ser alterado pelo método da classe'''

class Conta:
    def __init__(self, numero, saldo):
        self.__numero = numero #atributo privado
        self.__saldo = saldo  #atributo privado


def main():
    conta = Conta(1, 1000)
    saldo = conta.saldo
    #Vai ocorrer um erro porque o atributo saldo é privado
    print(saldo)

if __name__ == '__main__':
    main()
