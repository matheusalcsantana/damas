#!/usr/bin/env python
#coding:utf-8

import pygame

pygame.init()

#cores
white = 255,255,255
black = 0,0,0
tabuleiro1 = 183, 105, 56
tabuleiro2 = 253, 239, 192
pecas1 = 84, 40, 0
pecas2 = 216, 210, 141
#Tamanho da tela
screen = pygame.display.set_mode((800,600))
#Tamanho tabuleiro e peças
l = 50
r = 22
#Função desenhar peças
def desenhar_pecas():
	yi1 = 125
	yi2 = 475
	for i in range(3):
		if i % 2 == 0:
			xi1 = 200 + (l/2)*3
			xi2 = 200 + (l/2)
		else:
			xi1 = 200 + (l/2)
			xi2 = 200 + (l/2)*3
		for j in range(4):
			#Pecas1
			pygame.draw.circle(screen, pecas1, [xi1,yi1], r)
			pygame.draw.circle(screen, black, [xi1,yi1], r, 1)
			pygame.draw.circle(screen, black, [xi1,yi1], 15, 1)
			#Pecas2
			pygame.draw.circle(screen, pecas2, [xi2,yi2], r)
			pygame.draw.circle(screen, black, [xi2,yi2], r, 1)
			pygame.draw.circle(screen, black, [xi2,yi2], 15, 1)
			
			xi1 += 2*l
			xi2 += 2*l
			
		yi1 += l
		yi2 -= l
		
		
Exit = True

while Exit:
	
	for event in pygame.event.get():
		#Evento para quitar game
		if event.type == pygame.QUIT:
			Exit = False
			
	#Cor da tela (Branca)
	screen.fill(white)
	#Retângulo grande (Tabuleiro 1)
	pygame.draw.rect(screen, tabuleiro1, [200,100,400,400])
	#Retangulos pequenos (Tabuleiro 2)
	yi = 100
	for i in range(8):
		if i % 2 == 0:
			xi = 200
		else: 
			xi = 200 + l
			
		for j in range(4):
				pygame.draw.rect(screen, tabuleiro2, [xi, yi, l, l])
				xi += 2*l
		yi += l
		
	desenhar_pecas()
	
	#Atualizar a tela
	pygame.display.update()

pygame.quit()
quit
	
