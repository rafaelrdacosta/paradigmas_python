from Animal import Animal

class Vaca(Animal):
    def falar(self):
        return "Muuu!!"

    def mover(self):
        return f"{self.nome} está andando."