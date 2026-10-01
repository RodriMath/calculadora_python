# Importando as bibliotecas necessárias
from tkinter import *
from tkinter import ttk

"""A biblioteca Tkinter serve para criar interfaces gráficas de usuário (GUI) em Python, permitindo transformar scripts de linha de comando em programas visuais para desktop.
O ttk serve para fornecer widgets modernos e visuais nativos para as interfaces gráficas."""

# Cores

cor1 = "#0a0d0c" # black/preta
cor2 = "#feffff" # white/branca
cor3 = "#38576b" # Azul carregado
cor4 = "#ECEFF1" # cizenta
cor5 = "#FFAB40" # Orange/laranja

# Criação da janela e suas configurações básicas

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

# Criação dos Frames

frame_tela = Frame(janela, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

"""Em desenvolvimento de interfaces gráficas e programação, row significa linha (horizontal) e column significa coluna (vertical). Eles são usados para organizar os elementos na tela como se fosse uma planilha de Excel (uma tabela ou matriz).
Quando você posiciona componentes no Tkinter usando o método .grid(), você define a posição exata deles através de coordenadas:
    • row (Linha): Controla a posição de cima para baixo. A linha 0 é a primeira, a linha 1 fica logo abaixo, e assim por diante.
    • column (Coluna): Controla a posição da esquerda para a direita. A coluna 0 é a primeira, a coluna 1 fica à direita dela, e assim sucessivamente.
"""

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)


# Criando Função para entrada de valores na calculadora

all_values = ""

val_txt = StringVar()

def entrada_valores(event):
    global all_values

    all_values += str(event)

    val_txt.set(all_values)

# Função para realizar as operações

def calcular():
    resultado = eval(all_values)

    val_txt.set(str(resultado))

# Função para utilizar o botão Clear para limpeza de valores

def clear():
    global all_values

    all_values = ""
    
    val_txt.set("")

# Criando o Label

app_label = Label(frame_tela, textvariable=val_txt, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18"), bg=cor1, fg=cor4)
app_label.place(x=0, y=0)

# Botões Clear, porcentagem e barra

b1_clear = Button(frame_corpo, command = clear, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão C da calculadora: clear (limpar)
b1_clear.place(x=0, y=0) # posicionamento do botão no frame

b2_porcentagem = Button(frame_corpo, command = lambda: entrada_valores('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão % da calculadora
b2_porcentagem.place(x=118, y=0)

b3_barra = Button(frame_corpo, command = lambda: entrada_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão / da calculadora
b3_barra.place(x=177, y=0)

# Botões 7, 8, 9 e asterisco (multiplicação)

b4_num7 = Button(frame_corpo, command = lambda: entrada_valores('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4_num7.place(x=0, y=52)

b5_num8 = Button(frame_corpo, command = lambda: entrada_valores('8'), text="8", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5_num8.place(x=59, y=52)

b6_num9 = Button(frame_corpo, command = lambda: entrada_valores('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6_num9.place(x=118, y=52)

b7_astec = Button(frame_corpo, command = lambda: entrada_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7_astec.place(x=177, y=52)

# Botões 4, 5, 6 e - (subtração)

b8_num4 = Button(frame_corpo, command = lambda: entrada_valores('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8_num4.place(x=0, y=104)

b9_num5 = Button(frame_corpo, command = lambda: entrada_valores('5'), text="5", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9_num5.place(x=59, y=104)

b10_num6 = Button(frame_corpo, command = lambda: entrada_valores('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10_num6.place(x=118, y=104)

b11_sub = Button(frame_corpo, command = lambda: entrada_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11_sub.place(x=177, y=104)

# Botões 1, 2, 3 e + (adiçã0)

b12_num1 = Button(frame_corpo, command = lambda: entrada_valores('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12_num1.place(x=0, y=156)

b13_num2 = Button(frame_corpo, command = lambda: entrada_valores('2'), text="2", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13_num2.place(x=59, y=156)

b14_num3 = Button(frame_corpo, command = lambda: entrada_valores('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14_num3.place(x=118, y=156)

b15_adc = Button(frame_corpo,  command = lambda: entrada_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15_adc.place(x=177, y=156)

# Botões 0, . (ponto/vírgula) e = (igual)

b16_num0 = Button(frame_corpo,  command = lambda: entrada_valores('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão C da calculadora: clear (limpar)
b16_num0.place(x=0, y=208) # posicionamento do botão no frame

b17_ponto = Button(frame_corpo,  command = lambda: entrada_valores('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão % da calculadora
b17_ponto.place(x=118, y=208)

b18_igual = Button(frame_corpo,  command = calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Botão / da calculadora
b18_igual.place(x=177, y=208)

entrada_valores

janela.mainloop()