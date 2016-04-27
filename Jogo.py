# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 20:28:05 2016

@author: caioades
"""


'''
Jogo da Velha
'''
class Jogo():
    def __init__(self):
        self.game = [[0,0,0],[0,0,0],[0,0,0]]
        self.n_zeros = 9       
								
    def recebe_jogada (self, linha, coluna):
        if self.n_zeros%2 == 1 and self.game[linha][coluna]==0:
            self.game[linha][coluna] = "X"
            self.n_zeros-=1
        elif self.n_zeros%2 == 0 and self.game[linha][coluna]==0: 
            self.game[linha][coluna] = "O"
            self.n_zeros-=1    
    
    def verifica_ganhador(self):                
        if self.game[0][0] == "X" and self.game[1][1] == "X" and self.game[2][2] == "X":
            return 1 
        elif self.game[0][2] == "X" and self.game[1][1] == "X" and self.game[2][0] == "X":
            return 1
        elif self.game[0][0] == "X" and self.game[0][1] == "X" and self.game[0][2] == "X":
            return 1 
        elif self.game[1][0] == "X" and self.game[1][1] == "X" and self.game[1][2] == "X":
            return 1
        elif self.game[2][0] == "X" and self.game[2][1] == "X" and self.game[2][2] == "X":
            return 1
        elif self.game[0][0] == "X" and self.game [1][0] == "X" and self.game[2][0] == "X":
            return 1
        elif self.game[0][1] == "X" and self.game[1][1] == "X" and self.game[2][1] == "X":
            return 1
        elif self.game[0][2] == "X" and self.game[1][2] == "X" and self.game[2][2] == "X":
            return 1
        elif self.game[0][0] == "O" and self.game[1][1] == "O" and self.game[2][2] == "O":
            return 2
        elif self.game[0][2] == "O" and self.game[1][1] == "O" and self.game[2][0] == "O":
            return 2 
        elif self.game[0][0] == "O" and self.game[0][1] == "O" and self.game[0][2] == "O":
            return 2
        elif self.game[1][0] == "O" and self.game[1][1] == "O" and self.game[1][2] == "O":
            return 2
        elif self.game[2][0] == "O" and self.game[2][1] == "O" and self.game[2][2] == "O":
            return 2
        elif self.game[0][0] == "O" and self.game [1][0] == "O" and self.game[2][0] == "O":
            return 2
        elif self.game[0][1] == "O" and self.game[1][1] == "O" and self.game[2][1] == "O":
            return 2
        elif self.game[0][2] == "O" and self.game[1][2] == "O" and self.game[2][2] == "O":
            return 2
        elif self.n_zeros==0:
            return 0
        elif self.n_zeros==-1:
            if self.game.count(0) == 0:
                return 0
            else:
                return -1
        else:
            return -1
                
    
    def limpa_jogadas(self): 
        self.game = [[0,0,0],[0,0,0],[0,0,0]]        