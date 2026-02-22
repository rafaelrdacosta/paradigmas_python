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
        print(f'\nNumero: {self.numero}\nCPF: {self.cpf}\nSaldo: {self.saldo}')

def main():
    # Instanciando um objeto
    c1 = Conta(1, 64194159349, 'Rafael', 0)
    print(f'Nome do titular da conta: {c1.nomeTitular}')
    print(f'Número da conta: {c1.numero}')
    print(f'CPF do titular da conta: {c1.cpf}')
    print(f'Saldo da conta: {c1.saldo}')

    c1.depositar(300)
    c1.gerar_extrato()
    c1.sacar(100)
    c1.gerar_extrato()
    #Endereço de memória de c1
    print(c1)

if __name__ == "__main__":
    main()