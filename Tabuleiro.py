import tkinter as tk
class Tabuleiro:
	def __init__ (self):
		self.window=tk.Tk()
		self.window.title("Jogo da velha!")
		botao1=tk.Button(self.window)
		botao1.grid(row=0, column=0)
		botao1.config(height=10, width=20)
		#botao1.configure(command=selec_x)
		#botao1["text"]="X"
		botao1.bind("<Button-1>",selec_x)

		botao2=tk.Button(self.window)
		botao2.grid(row=0, column=1)
		botao2.config(height=10, width=20)

		botao3=tk.Button(self.window)
		botao3.grid(row=0, column=2)
		botao3.config(height=10, width=20)

		botao4=tk.Button(self.window)
		botao4.grid(row=1, column=0)
		botao4.config(height=10, width=20)
	
		botao5=tk.Button(self.window)
		botao5.grid(row=1, column=1)
		botao5.config(height=10, width=20)

		botao6=tk.Button(self.window)
		botao6.grid(row=1, column=2)
		botao6.config(height=10, width=20)

		botao7=tk.Button(self.window)
		botao7.grid(row=2, column=0)
		botao7.config(height=10, width=20)
	
		botao8=tk.Button(self.window)
		botao8.grid(row=2, column=1)
		botao8.config(height=10, width=20)

		botao9=tk.Button(self.window)
		botao9.grid(row=2, column=2)
		botao9.config(height=10, width=20)

	def iniciar(self):
		self.window.mainloop()

	def selec_x(event):
		#["text"]="X"
		
		
	def selec_o(event):
		#["text"]="O"
	
	
	def escolha(self):
		return False

jogo=Tabuleiro()
jogo.iniciar()
#jogo.selec_x()
