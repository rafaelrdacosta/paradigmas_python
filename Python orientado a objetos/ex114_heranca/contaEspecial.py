#Conta especial herança de conta

from conta import Conta
import datetime

class ContaEspecial(Conta):

    def __init__(self, clientes, numero, saldo, limite):
        '''super().__init__(clientes, numero, saldo) chama o construtor
        e inicializa os atributos herdados'''
        super().__init__(clientes, numero, saldo)
        #atributo limite exclusivo da conta especial
        self.limite = limite

    '''Poliformisfo
    Sobescrever o método sacar para adicionar a lógica que permite sacar
    além do saldo até o limite definido'''

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print(f"Não existe saldo suficiente na conta número {self.numero}")
            return False
        else:
            self.saldo -= valor
            if (self.saldo < 0):
                self.limite += self.saldo
            self.extrato.transacoes.append(["SAQUE", valor, datetime.datetime.today()])
            return True

    #método depositar precisa ser reescrito para conta especial
    def depositar(self, valor):
        pass

