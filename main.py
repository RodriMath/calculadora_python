# Importando as bibliotecas necessárias
from tkinter import *
from tkinter import ttk

# Cores

cor1 = "#3b3b3b" # black/preta
cor2 = "#feffff" # white/branca
cor3 = "#38576b" # Azul carregado
cor4 = "#ECEFF1" # cizenta
cor5 = '#FFAB40' # Orange/laranja


# Criação da janela e suas configurações básicas
janela = Tk()
janela.title("Calculadora")
janela.geometry("300x518")
janela.config(bg=cor1)

# Criação dos Frames

frame_tela = Frame(janela, width=335, height=150, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=335, height=65, bg=cor2)
frame_corpo.grid(row=1, column=0)

# Criação dos Botões 

janela.mainloop()