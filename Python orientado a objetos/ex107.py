#Classe sem método construtor
class A():
    #Definindo um método
    def f(self):
        print('foo')

def main():
    #Instanciando um objeto
    obj_A = A()
    obj_A.f()

if __name__ == '__main__':
    main()