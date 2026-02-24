'''
Crie uma classe chamada televisão que siga os requisitos a seguir.
Receba como parâmetros em seu construtor o canal inicial, o maior canal e o menor canal.
Possua como atributos o canal sintonizado, o número do maior canal e o número do menor canal.
Possua dois métodos, um para diminuir o canal atual e outro para aumentar o canal sintonizado.
Instancie uma tv e teste as trocas de canal.
'''

class Televisao:
    def __init__(self, pcanal, min, max):
        self.canal = pcanal
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin

tv1 = Televisao(2, 2, 10)
print(tv1.canal)
for x in range(1, 20):
    tv1.muda_canal_para_cima()
    print(tv1.canal)

tv2 = Televisao(10, 2, 10)
print(tv2.canal)
for x in range(1, 20):
    tv2.muda_canal_para_baixo()
    print(tv2.canal)