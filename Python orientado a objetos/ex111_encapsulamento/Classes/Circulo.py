'''Atributo de classe
Usado para controlar valores associados à classe,
e não aos objtos.'''

class Circulo:
    #Atributo da classe fora do init
    totalCirculos = 0

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        Circulo.totalCirculos += 1