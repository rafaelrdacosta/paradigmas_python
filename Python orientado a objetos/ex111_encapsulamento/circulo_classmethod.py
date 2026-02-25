class Circulo():
    _total_circulos = 0

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        '''Usar type(self)._total_circulos é equivalente a usar Circulo._total_circulos,
         mas permite que o código funcione corretamente mesmo se for usado em subclasses,
        garantindo que o incremento seja realizado na classe apropriada.'''
        type(self)._total_circulos += 1

    @classmethod
    def get_total_circulos(cls):
        return cls._total_circulos

circ1 = Circulo(1, 1, 10)
circ2 = Circulo(2, 2, 20)

print(Circulo.get_total_circulos())