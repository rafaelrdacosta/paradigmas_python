from Animal import Animal
from Voador import Voador
from Nadador import Nadador

class Pato(Animal, Voador, Nadador):
    def falar(self):
        return "Quack!!"

    def andar(self):
        return f"{self.nome} está andando"

    def mover(self):
        return f"{self.andar()}, {self.nadar()} e {self.voar()}"

