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
        #self.jogador = jogador
        self.game = [[0,0,0],[0,0,0],[0,0,0]]
        self.n_zeros = 9       
								
    def recebe_jogada (self, linha, coluna):
        if self.n_zeros%2 == 1 and self.n_zeros>=0:
            self.game[linha][coluna] = 'X'
            self.n_zeros-=1
        elif self.n_zeros%2 == 0 and self.n_zeros>=0: 
            self.game[linha][coluna] = 'O'
            self.n_zeros-=1
        #return self.n_zeros
    
    
    def verifica_ganhador(self):
        for i in range(len(self.game)):
            if self.game[0][i] == self.game[1][i] and self.game[0][i] == self.game[2][i]:
                if self.game[0][i] == 'X':
                    return 1
                elif self.game[i][0] == 'O':
                    return 2    
                
            elif self.game[i] == ['X','X','X']:
                return 1
            elif self.game[i] == ['O','O','O']:
                return 2
#            else:
#                return -1
                
        if self.game[0][0] == self.game[1][1] and self.game[0][0] == self.game[2][2]:
            if self.game[0][0] == 'X':
                return 1
            elif self.game[0][0] == 'O':
                return 2
#            else:
#                return -1
        elif self.game[0][2] == self.game[1][1] and self.game[0][2] == self.game[2][0]:
            if self.game[0][2] == 'X':
                return 1
            elif self.game[0][2] == 'O':
                return 2
#            else:
#                return -1
        elif self.n_zeros == 0:
            return 0
        else:
            return -1

                
    
    def limpa_jogadas(self): 
        
        if self.verifica_ganhador() >= 0:
            self.game = [[0,0,0],[0,0,0],[0,0,0]]
 
            
