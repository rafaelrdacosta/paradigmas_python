#tkinter

from tkinter import *

janelaPrincipal = Tk()

#define o título da janela
janelaPrincipal.title('Meu primeiro app')

#define o tamanho inicial
janelaPrincipal.geometry('400x300')

#adicionando um texto dentro da janela
texto = Label(janelaPrincipal, text='Olá, Mundo!!')
texto.pack() # O pack() serve para "encaixar" o elemento na janela

janelaPrincipal.mainloop()
