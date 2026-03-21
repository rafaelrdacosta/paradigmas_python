from Animal import Animal
from Cachorro import Cachorro
from Gato import Gato
from Vaca import Vaca
from Pato import Pato
from Jacare import Jacare

def fazer_som(animal):
    return animal.falar()

def fazer_movimento(animal):
    return animal.mover()


#Instância de classes
cachorro = Cachorro('Lug')
gato = Gato('Floquinho')
vaca = Vaca('Mimosa')
pato = Pato('Pato Donald')
jacare = Jacare('Crocodilo')

#Chamando os métodos polimórficos
print(fazer_som(cachorro))
print(fazer_som(gato))
print(fazer_som(vaca))
print(fazer_som(pato))
print(fazer_som(jacare))

print(fazer_movimento(cachorro))
print(fazer_movimento(gato))
print(fazer_movimento(vaca))
print(fazer_movimento(pato))
print(fazer_movimento(jacare))