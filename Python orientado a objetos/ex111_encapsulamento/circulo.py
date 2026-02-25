class Circulo():
    #Atributo de classe
    #a variável de classe dever ser marcada como privada, usando um underscore (_) antes do seu nome.
    _total_circulos = 0

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        #Incremento do atributo de classe
        Circulo._total_circulos += 1

circ1 = Circulo(1, 1, 10)
print(circ1._total_circulos) #isso agora imprimirá 1

circ2 = Circulo(2, 2, 20)
print(circ1._total_circulos)  # Isso agora imprimirá 2
print(circ2._total_circulos)  # Isso também imprimirá 2

print(Circulo._total_circulos)  # Isso imprimirá 2, já que é o valor compartilhado por todas as instâncias