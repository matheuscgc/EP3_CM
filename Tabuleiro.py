import tkinter as tk
from Jogo import Jogo
class Tabuleiro(Jogo):
	def __init__ (self):		
		self.window=tk.Tk()
		self.window.title("Jogo da velha!")
		self.joguinho = Jogo()
		botao1=tk.Button(self.window)
		botao1.grid(row=0, column=0)
		botao1.config(height=10, width=20)
		botao1.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao1)and self.joguinho.recebe_jogada(0, 0))
		#botao1.configure(command=lambda: self.joguinho.recebe_jogada(0, 0))

		botao2=tk.Button(self.window)
		botao2.grid(row=0, column=1)
		botao2.config(height=10, width=20)
		botao2.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao2)and self.joguinho.recebe_jogada(0, 1))
		#botao2.configure(command=lambda: self.joguinho.recebe_jogada(0, 1))

		botao3=tk.Button(self.window)
		botao3.grid(row=0, column=2)
		botao3.config(height=10, width=20)
		botao3.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao3)and self.joguinho.recebe_jogada(0, 2))
		#botao3.configure(command=lambda: self.joguinho.recebe_jogada(0, 2))

		botao4=tk.Button(self.window)
		botao4.grid(row=1, column=0)
		botao4.config(height=10, width=20)
		botao4.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao4)and self.joguinho.recebe_jogada(1, 0))
		#3botao4.configure(command=lambda: self.joguinho.recebe_jogada(1, 0))
	
		botao5=tk.Button(self.window)
		botao5.grid(row=1, column=1)
		botao5.config(height=10, width=20)
		botao5.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao5)and self.joguinho.recebe_jogada(1, 1))
		#botao5.configure(command=lambda: self.joguinho.recebe_jogada(1, 1))

		botao6=tk.Button(self.window)
		botao6.grid(row=1, column=2)
		botao6.config(height=10, width=20)
		botao6.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao6)and self.joguinho.recebe_jogada(1, 2))
		#botao6.configure(command=lambda: self.joguinho.recebe_jogada(1, 2))

		botao7=tk.Button(self.window)
		botao7.grid(row=2, column=0)
		botao7.config(height=10, width=20)
		botao7.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao7)and self.joguinho.recebe_jogada(2, 0))
		#botao7.configure(command=lambda: self.joguinho.recebe_jogada(2, 0))

		botao8=tk.Button(self.window)
		botao8.grid(row=2, column=1)
		botao8.config(height=10, width=20)
		botao8.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao8)and self.joguinho.recebe_jogada(2, 1))
		#botao8.configure(command=lambda: self.joguinho.recebe_jogada(2, 1))

		botao9=tk.Button(self.window)
		botao9.grid(row=2, column=2)
		botao9.config(height=10, width=20)
		botao9.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao9) and self.joguinho.recebe_jogada(2, 2))		
		
		prox_jogada=tk.Message()
		prox_jogada.config(text="Próxima jogada: X")
		prox_jogada.grid(row=3, sticky = tk.W+tk.E)
		

	
	def iniciar(self):
		self.window.mainloop()
				

	def alterna(self, prox_jogada, botao):
		if self.joguinho.n_zeros%2 == 1:# and self.joguinho.n_zeros>=0:
			botao["text"]="O"
			prox_jogada.config(text="Próxima jogada: X")
			self.joguinho.n_zeros-=1			
			
		elif self.joguinho.n_zeros%2==0:# and self.joguinho.n_zeros>=0: 
			botao["text"]="X"
			prox_jogada.config(text="Próxima jogada: O")
			self.joguinho.n_zeros-=1
		
		
		
jogo=Tabuleiro()
jogo.iniciar()

jogo.joguinho.verifica_ganhador()
print (jogo.joguinho.game)
print (jogo.joguinho.verifica_ganhador())
jogo.joguinho.limpa_jogadas()

print (jogo.joguinho.game)
print (jogo.joguinho.n_zeros)