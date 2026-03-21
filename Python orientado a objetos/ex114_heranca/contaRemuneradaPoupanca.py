#Herança múltipla

from conta import Conta
from poupanca import Poupanca

class ContaRemuneradaPoupanca(Conta, Poupanca):
    def __init__(self, taxa_remuneracao, clientes, numero, saldo):
        #inicializar os atributos herdados da classe Conta
        Conta.__init__(self, clientes, numero, saldo)
        #inicializar os atributos herdados da classe poupanca
        Poupanca.__init__(self, taxa_remuneracao)

    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxaremuneracaoMes / 30)