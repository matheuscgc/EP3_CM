import tkinter as tk
c=[1]
class Tabuleiro:
	def __init__ (self):		
		self.window=tk.Tk()
		self.window.title("Jogo da velha!")
		botao1=tk.Button(self.window)
		botao1.grid(row=0, column=0)
		botao1.config(height=10, width=20)
		botao1["text"]="-"
		botao1.configure(command=lambda: Tabuleiro.alterna(c, prox_jogada, botao1))
		

		botao2=tk.Button(self.window)
		botao2.grid(row=0, column=1)
		botao2.config(height=10, width=20)
		botao2["text"]="-"
		botao2.configure(command=lambda: Tabuleiro.alterna(c, prox_jogada, botao2))


		botao3=tk.Button(self.window)
		botao3.grid(row=0, column=2)
		botao3.config(height=10, width=20)
		botao3["text"]="-"
		botao3.configure(command=lambda: Tabuleiro.alterna(c, prox_jogada, botao3))


		botao4=tk.Button(self.window)
		botao4.grid(row=1, column=0)
		botao4.config(height=10, width=20)
		botao4["text"]="-"
		botao4.configure(command=lambda: Tabuleiro.alterna(c, prox_jogada, botao4))

	
		botao5=tk.Button(self.window)
		botao5.grid(row=1, column=1)
		botao5.config(height=10, width=20)
		botao5["text"]="-"
		botao5.configure(command=lambda: Tabuleiro.alterna(c, prox_jogada, botao5))


		botao6=tk.Button(self.window)
		botao6.grid(row=1, column=2)
		botao6.config(height=10, width=20)
		botao6["text"]="-"
		botao6.configure(command=lambda: Tabuleiro.alterna(c, prox_jogada, botao6))


		botao7=tk.Button(self.window)
		botao7.grid(row=2, column=0)
		botao7.config(height=10, width=20)
		botao7["text"]="-"	
		botao7.configure(command=lambda: Tabuleiro.alterna(c, prox_jogada, botao7))


		botao8=tk.Button(self.window)
		botao8.grid(row=2, column=1)
		botao8.config(height=10, width=20)
		botao8["text"]="-"
		botao8.configure(command=lambda: Tabuleiro.alterna(c, prox_jogada, botao8))


		botao9=tk.Button(self.window)
		botao9.grid(row=2, column=2)
		botao9.config(height=10, width=20)
		botao9["text"]="-"
		botao9.configure(command=lambda: Tabuleiro.alterna(c, prox_jogada, botao9))		
		
		
		prox_jogada=tk.Message()
		prox_jogada.config(text="Próxima jogada: X")
		prox_jogada.grid(row=3, column=0)

	
	def iniciar(self):
		self.window.mainloop()
				

	def alterna(c, prox_jogada,botao):
		if len(c)%2==0:
			botao["text"]="O"
			prox_jogada.config(text="Próxima jogada: X")
			c.append(1)
		
		elif len(c)%2==1:
			botao["text"]="X"
			prox_jogada.config(text="Próxima jogada: O")
			c.append(1)
		
jogo=Tabuleiro()
jogo.iniciar()