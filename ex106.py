class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    # Definição dos métodos

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def gerar_extrato(self):
        print(f'Numero: {self.numero} \n CPF: {self.cpf} \n Saldo: {self.saldo}')

    def tranfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return('Saldo insuficiente.')
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return('Transferência realizada.')

def main():
    # Instanciando um objeto
    c1 = Conta(1, 64194159349, 'Rafael', 0)
    c2 = Conta(2, 12345678901, 'Jéh', 0)
    c1.depositar(1000)
    c1.tranfereValor(c2,300)
    print(f'Saldo conta 1: {c1.saldo}')
    print(f'Saldo conta 2: {c2.saldo}')

if __name__ == "__main__":
    main()