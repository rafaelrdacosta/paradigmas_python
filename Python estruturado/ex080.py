from tkinter import *

janelaPrincipal = Tk()
janelaPrincipal.title('App com Tkinter')
janelaPrincipal.geometry('400x500')
texto = Label(master = janelaPrincipal, text = 'Minha janela exibida')
texto.place(x = 50, y = 100)
janelaPrincipal.mainloop()