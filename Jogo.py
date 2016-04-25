# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 20:28:05 2016

@author: caioades
"""


'''
Jogo da Velha
'''

class Jogo: 
    
    game = [[0,0,0],[0,0,0],[0,0,0]]
    log = ['O']
    
    def __init__(self, jogador):
        self.jogador = jogador
        
        
        
    def recebe_jogada(self,linha,coluna):
        x = len(self.log)
        if self.log[x-1] == 'O':
            self.game[linha][coluna] = 'X'
            self.log.append('X')
        elif self.log[x] == 'X': 
            self.game[linha][coluna] = 'O'
            self.log.append('O')
        else:
            self.game[linha][coluna] = self.log[x-1]
            self.log.append(self.log[x-1])
        return self.log
    
    
    def verifica_ganhador(self):
        
        for i in range(len(self.game)):
            if self.game[0][i] == self.game[1][i] and self.game[0][i] == self.game[2][i]:
                if self.game[0][i] == 'X':
                    return 1
                elif self.game[i][0] == 'O':
                    return      
            elif self.game[i] == ['X','X','X']:
                return 1
            elif self.game[i] == ['O','O','O']:
                return 2
                
                
        if self.game[0][0] == self.game[1][1] and self.game[0][0] == self.game[2][2]:
            if self.game[0][0] == 'X':
                return 1
            elif self.game[0][0] == 'O':
                return 2
        elif self.game[0][2] == self.game[1][1] and self.game[0][2] == self.game[2][0]:
            if self.game[0][2] == 'X':
                return 1
            elif self.game[0][2] == 'O':
                return 2
        elif len(self.log) == 10:
            return 0
        else:
            return -1

                
    
    def limpa_jogadas(self): 
        if self.verifica_ganhador() >= 0:
            self.game = [[0,0,0],[0,0,0],[0,0,0]]
            ultimo = self.log[9]
            self.log = []
            self.log.append(ultimo)
        return 
     
    

    