#Utilizando métodos decorados

class Conta:
    def __init__(self, numero):
        self.numero = numero
        '''Uso de somente um _ indicando atributo que é protegido
        e deve ser manipulado apenas internamente.'''
        self._saldo = 0

    '''Utilizando o decorador @property, podemos proteger os atributos
    e acessá-los somente por meio de métodos "decorados".'''

    #Definindo método decorado
    @property
    def saldo(self):
        return self._saldo

    '''O decorador @setter força todas as alterações de valor dos
    atributos privados a passar por esses métodos.'''
    #Definindo método setter
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print('Saldo inválido')
        else:
            self._saldo = saldo

def main():
    conta = Conta(1)
    #Usando o @saldo.setter
    conta.saldo = 1000
    #Usando o @property
    print(f'Saldo da conta = {conta.saldo}')

if __name__ == "__main__":
    main()