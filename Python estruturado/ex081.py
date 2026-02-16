from doctest import master
from tkinter import *

def funcClicar():
    print('Botão pressionado')

janelaPrincipal = Tk()
janelaPrincipal.geometry('400x300')
texto = Label(master = janelaPrincipal, text = 'Minha janela principal')
texto.pack()

botao = Button(master = janelaPrincipal, text = 'Clique', command=funcClicar)
botao.pack()

janelaPrincipal.mainloop()