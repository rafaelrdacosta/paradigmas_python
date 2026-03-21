'''Classe abstrata e método abstrato
Não pode ser instanciada
'''

from abc import ABC, abstractmethod


#abc (Abstract Base Classes) - super classe de uma classe abstrata

class ContaCliente(ABC):
    def __init__(self, numero, IOF, IR, valorInvestido, taxaRendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorInvestido = valorInvestido
        self.taxaRendimento = taxaRendimento
    #decorator @abstractmethod para indicar que o método cálculo_rendimento é abstrato
    @abstractmethod
    def CalcularRendimento(self):
        pass


class ContaReal(ContaCliente):
    def __init__(self, numero, IOF, IR, valorInvestido, taxaRendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorInvestido = valorInvestido
        self.taxaRendimento = taxaRendimento

    def CalcularRendimento(self):
        pass

cc1 = ContaReal(1, 0.1, 0.25, 10.1, 10)
print(cc1)
print(cc1.numero)
print(cc1.valorInvestido)