from tkinter import *
from PIL import Image, ImageTk  # Importação necessária para JPEG

def funcClicar():
    print('Amor da minha vida!!')

janelaPrincipal = Tk()
janelaPrincipal.title("Meu amor")
janelaPrincipal.geometry('300x300')

texto = Label(master = janelaPrincipal, text='Linda!!!')
texto.pack()

try:
    # Abre a imagem usando o Pillow
    imagem_pil = Image.open("amor.jpeg").resize((200, 200))

    # Converte a imagem para um formato que o Tkinter aceita
    pic = ImageTk.PhotoImage(imagem_pil)

    logo = Label(master=janelaPrincipal, image=pic)
    # É importante manter uma referência da imagem para o garbage collector não apagá-la
    logo.image = pic
    logo.pack()
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")
    label_erro = Label(janelaPrincipal, text="Arquivo amor.jpeg não encontrado ou inválido", fg="red")
    label_erro.pack()

botao = Button(master = janelaPrincipal, text = 'Clique', command = funcClicar)
botao.pack()

janelaPrincipal.mainloop()