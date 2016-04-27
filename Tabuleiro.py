import tkinter as tk
from Jogo import Jogo
class Tabuleiro(Jogo):
	def __init__ (self):		
		self.window=tk.Tk()
		self.window.title("Jogo da velha!")
		self.joguinho = Jogo()
		self.cria_tabuleiro()

	def cria_tabuleiro(self):		
		if self.joguinho.verifica_ganhador() == -1:		
			prox_jogada=tk.Message()
			prox_jogada.config(text="Próxima jogada: X")
			prox_jogada.grid(row=3, sticky = tk.W+tk.E)		
		
		elif self.joguinho.verifica_ganhador() == 1:
			prox_jogada=tk.Message()			
			prox_jogada.config(text="Vencedor: X. Próxima jogada: O")
			prox_jogada.grid(row=3, sticky = tk.W+tk.E)
		
		elif self.joguinho.verifica_ganhador() == 2:
			prox_jogada=tk.Message()			
			prox_jogada.config(text="Vencedor: O. Próxima jogada: X")
			prox_jogada.grid(row=3, sticky = tk.W+tk.E)
			
		elif self.joguinho.verifica_ganhador() == 0:
			prox_jogada=tk.Message()			
			prox_jogada.config(text="Empate. O Jogo reinicia, então quem começa agora é quem começou o anterior")
			prox_jogada.grid(row=3, sticky = tk.W+tk.E)
		
		botao1=tk.Button(self.window)
		botao1.grid(row=0, column=0)
		botao1.config(height=10, width=20)
		botao1.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao1, 0, 0))

		botao2=tk.Button(self.window)
		botao2.grid(row=0, column=1)
		botao2.config(height=10, width=20)
		botao2.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao2, 0, 1))

		botao3=tk.Button(self.window)
		botao3.grid(row=0, column=2)
		botao3.config(height=10, width=20)
		botao3.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao3, 0, 2))

		botao4=tk.Button(self.window)
		botao4.grid(row=1, column=0)
		botao4.config(height=10, width=20)
		botao4.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao4, 1, 0))
	
		botao5=tk.Button(self.window)
		botao5.grid(row=1, column=1)
		botao5.config(height=10, width=20)
		botao5.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao5, 1, 1))
		
		botao6=tk.Button(self.window)
		botao6.grid(row=1, column=2)
		botao6.config(height=10, width=20)
		botao6.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao6, 1, 2))

		botao7=tk.Button(self.window)
		botao7.grid(row=2, column=0)
		botao7.config(height=10, width=20)
		botao7.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao7, 2, 0))

		botao8=tk.Button(self.window)
		botao8.grid(row=2, column=1)
		botao8.config(height=10, width=20)
		botao8.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao8, 2, 1))

		botao9=tk.Button(self.window)
		botao9.grid(row=2, column=2)
		botao9.config(height=10, width=20)
		botao9.configure(command=lambda: Tabuleiro.alterna(self, prox_jogada, botao9, 2, 2))
		
	def iniciar(self):
		self.window.mainloop()
			
	def alterna(self, prox_jogada, botao, linha, coluna):
		if self.joguinho.verifica_ganhador() == -1:		
			if self.joguinho.n_zeros%2 == 1 and self.joguinho.game[linha][coluna]==0:
				botao["text"]="X"
				prox_jogada.config(text="Próxima jogada: O")
				self.joguinho.recebe_jogada(linha, coluna)
				if self.joguinho.verifica_ganhador() == 1:
					Tabuleiro.cria_tabuleiro(self)					
					self.joguinho.n_zeros = 8			
					self.joguinho.limpa_jogadas()
			
				elif self.joguinho.verifica_ganhador() == 2:
					Tabuleiro.cria_tabuleiro(self)					
					self.joguinho.n_zeros = 9			
					self.joguinho.limpa_jogadas()
					
				elif self.joguinho.verifica_ganhador() == 0:
					Tabuleiro.cria_tabuleiro(self)					
					self.joguinho.n_zeros = 9
					self.joguinho.limpa_jogadas()
				
			elif self.joguinho.n_zeros%2 == 0 and self.joguinho.game[linha][coluna]==0: 
				botao["text"]="O"			
				prox_jogada.config(text="Próxima jogada: X")
				self.joguinho.recebe_jogada(linha, coluna)
				self.joguinho.verifica_ganhador()
				if self.joguinho.verifica_ganhador() == 1:
					Tabuleiro.cria_tabuleiro(self)					
					self.joguinho.n_zeros = 8			
					self.joguinho.limpa_jogadas()
			
				elif self.joguinho.verifica_ganhador() == 2:
					Tabuleiro.cria_tabuleiro(self)					
					self.joguinho.n_zeros = 9			
					self.joguinho.limpa_jogadas()
					
				elif self.joguinho.verifica_ganhador() == 0:
					Tabuleiro.cria_tabuleiro(self)					
					self.joguinho.n_zeros = 9
					self.joguinho.limpa_jogadas()
					
jogo=Tabuleiro()
jogo.iniciar()

jogo.joguinho.verifica_ganhador()
print (jogo.joguinho.game)
print (jogo.joguinho.verifica_ganhador())

print (jogo.joguinho.game)
print (jogo.joguinho.n_zeros)