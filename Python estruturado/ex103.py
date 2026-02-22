import tkinter as tk
from tkinter import messagebox
from webbrowser import Error


def calcular_imc():

    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / altura ** 2

        #Classificar o IMC
        if imc < 18.5:
            grau = 'Abaixo do peso.'
        elif imc < 25:
            grau = 'Peso Normal.'
        elif imc < 30:
            grau = 'Sobrepeso.'
        elif imc < 40:
            grau = 'Obesidade.'
        else:
            grau = 'Obesidade grave.'
        messagebox.showinfo('Classificação do IMC', f'IMC: {imc:.2f} - Grau: {grau}')
    except ValueError:
        messagebox.showinfo('Erro:', 'Por favor insira números válidos.')
    except Error as e:
        messagebox.showinfo('Erro:', f'{e}')

#Criando a janela
janela = tk.Tk()
janela.geometry('400x200')
janela.title('Calculadora de IMC')

#Criando os widgets
label_peso=tk.Label(janela, text='Peso(kg):')
label_peso.grid(row=0, column=0, padx=10, pady=10)

entry_peso=tk.Entry(janela)
entry_peso.grid(row=0, column=1, padx=10, pady=10)

label_altura=tk.Label(janela, text='Altura(m):')
label_altura.grid(row=1, column=0, padx=10, pady=10)

entry_altura=tk.Entry(janela)
entry_altura.grid(row=1, column=1, padx=10, pady=10)

butao_imc=tk.Button(janela, text='Calcular IMC', command=calcular_imc)
butao_imc.grid(row=2, columnspan=4, padx=20, pady=10)

#Rodando a janela principal
janela.mainloop()

