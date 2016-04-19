import tkinter as tk
from tkinter import *
class Tabuleiro:
	def __init__ (self, botao):
		self.botao = botao
	def selec_x():
		
		
	def selec_o():
		
		
		
window=tk.Tk()
botao1=tk.Button(window)
botao1.grid(row=0, column=0)
botao1.config(height=10, width=20)

botao2=tk.Button(window)
botao2.grid(row=0, column=1)
botao2.config(height=10, width=20)

botao3=tk.Button(window)
botao3.grid(row=0, column=2)
botao3.config(height=10, width=20)

botao4=tk.Button(window)
botao4.grid(row=1, column=0)
botao4.config(height=10, width=20)

botao5=tk.Button(window)
botao5.grid(row=1, column=1)
botao5.config(height=10, width=20)

botao6=tk.Button(window)
botao6.grid(row=1, column=2)
botao6.config(height=10, width=20)

botao7=tk.Button(window)
botao7.grid(row=2, column=0)
botao7.config(height=10, width=20)

botao8=tk.Button(window)
botao8.grid(row=2, column=1)
botao8.config(height=10, width=20)

botao9=tk.Button(window)
botao9.grid(row=2, column=2)
botao9.config(height=10, width=20)
		
window.mainloop()