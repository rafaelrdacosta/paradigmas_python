'''Métodos estáticos podem ser chamados sem uma
referência a um objeto da classe'''


class MinhaClasse:
    #Definindo método estático
    @staticmethod
    def metodo_estatico(x, y):
        return x + y

'''Usando o método estático
Não é necessário instaciar nenhum objeto de classe
para usar o método estático'''
resultado = MinhaClasse.metodo_estatico(3, 5)
print(resultado)

#Podendo também instaciar um objeto de classe
obj = MinhaClasse()
resultado = obj.metodo_estatico(10, 20)
print(resultado)