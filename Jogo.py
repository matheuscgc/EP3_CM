# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 20:28:05 2016

@author: caioades
"""


''' jogadores:
-X
-O

...um botão é apertado no tkinter:

recebe jogada:
    recebe do tkinter
    sabe qual jogador tem a vez
    executa a jogada
    registra(log?)
    
verifica (constantemente) se o jogo acabou 
     contém a lógica do jogo (possibilidades de ganhar)
     0 - empate
     1 - X vence
     2 - O vence
     -1 - else
     
se o jogo teriminar:
    termina jogo:
        reinicia o jogo
        mantém a vez do jogador'''
        
     
def recebe_jogada(linha,coluna):
    
    #importar jogada do tabuleiro?
    game[linha][coluna] = Jogo(jogador) 
    
     
    
    
    
    