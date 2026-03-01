'''Método sacar - para evitar alteração indevida no saldo da conta
Definição do método sacar, se o saldo for menor do que o valor solicitado
para o saque não será possível realizar o saque'''
from datetime import datetime


def sacar(self, valor):
    if self.saldo < valor:
        return False
    else:
        self.saldo -= valor
        self.extrato.transacoes.append(['SAQUE', valor, 'Data', datetime.datetime.today()])
        return True