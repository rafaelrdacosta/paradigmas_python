from Animal import Animal
from Nadador import Nadador

class Jacare(Animal, Nadador):

    def falar(self):
        return "Grunnnnn!!"

    def andar(self):
        return f"{self.nome} está andando"

    def mover(self):
        return f"{self.andar()} e {self.nadar()}."
