'''Método de classe
Servem para manipular os atributos da classe'''

class Circulo2:
    #Atributo privado
    __totalCirculos = 0

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        type(self).__totalCirculos += 1

    #@classmethod criar o método de classe
    @classmethod
    def get_totalCirculos(cls):
        return cls.__totalCirculos