#!/usr/bin/env python
#coding:utf-8

import pygame


#cores
white = 255,255,255
tabuleiro1 = 51, 25, 0
tabuleiro2 = 204, 153, 51
#Tamanho da tela
screen = pygame.display.set_mode((800,600))

Exit = True

while Exit:
	
	for event in pygame.event.get():
		#Evento para quitar game
		if event.type == pygame.QUIT:
			Exit = False
			
	#Cor da tela (Branca)
	screen.fill(white)
	pygame.draw.rect(screen, tabuleiro1, [150,50,500,500])
	#Atualizar a tela
	pygame.display.flip()

pygame.quit()
quit
	
