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

#Matriz Tabuleiro - Coordenadas inicias
yi = 100
matriz_tab = []
for i in range(8):
	if i % 2 == 0:
		xi = 200 + l
	else: 
		xi = 200
		
	for j in range(4):
			coord = (xi, yi)
			matriz_tab.append(coord)
			xi += 2*l
	yi += l
	
print matriz_tab
#Função desenhar peças
def desenhar_pecas():
	for i in range(12):
		#Pecas1
		pygame.draw.circle(screen, pecas1, [matriz_tab[i][0] + l/2, matriz_tab[i][1] + l/2], r)
		pygame.draw.circle(screen, black, [matriz_tab[i][0] + l/2, matriz_tab[i][1] + l/2], r, 1)
		pygame.draw.circle(screen, black, [matriz_tab[i][0] + l/2, matriz_tab[i][1] + l/2], 15, 1)
		
	for j in range(len(matriz_tab) - 1, len(matriz_tab) - 13, -1):
		#Pecas2
		pygame.draw.circle(screen, pecas2, [matriz_tab[j][0] + l/2, matriz_tab[j][1] + l/2], r)
		pygame.draw.circle(screen, black, [matriz_tab[j][0] + l/2, matriz_tab[j][1] + l/2], r, 1)
		pygame.draw.circle(screen, black, [matriz_tab[j][0] + l/2, matriz_tab[j][1] + l/2], 15, 1)
			
	
		
Exit = True

while Exit:
	
	for event in pygame.event.get():
		#Evento para quitar game
		if event.type == pygame.QUIT:
			Exit = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			print MOUSEBUTTONDOWN	
	#Cor da tela (Branca)
	screen.fill(white)
	#Retângulo grande (Tabuleiro 1)
	pygame.draw.rect(screen, tabuleiro2, [200,100,400,400])
	#Retangulos pequenos (Tabuleiro 2)
	
	for i in range(32):
		xi = matriz_tab[i][0]
		yi = matriz_tab[i][1]
		pygame.draw.rect(screen, tabuleiro1, [xi, yi, l, l])
	
	desenhar_pecas()
	#locais onde as peças podem ir
	
	#Atualizar a tela
	pygame.display.update()

pygame.quit()
quit
	
