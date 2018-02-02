#!/usr/bin/env python
#coding:utf-8

import pygame

pygame.init()

#cores
white = 255,255,255
black = 0,0,0
tabuleiro1 = 183, 105, 56
tabuleiro2 = 253, 239, 192
cor_pretas = 84, 40, 0
cor_brancas = 216, 210, 141
verde = 0, 204, 0
#Tamanho da tela
screen = pygame.display.set_mode((800,600))
#Tamanho tabuleiro e peças
l = 50
r = 22

#Matriz Tabuleiro - Coordenadas inicias
yi = 100
matriz_tab = []
for i in range(8):
	linha = []
	if i % 2 == 0:
		xi = 200 + l
	else:
		xi = 200

	if i >= 0 and i <= 2: aux = 'p'
 	elif i > 2 and i <= 4: aux = ' '
	else: aux = 'b'

	for j in range(4):
			coord = [aux, xi, yi, tabuleiro1]
			linha.append(coord)
			xi += 2*l
	matriz_tab.append(linha)
	yi += l

#Função que vai receber a cor da matriz_tab e mudar de acordo com a necessidade
def desenhar_tab1(matriz):
	for i in range(8):
		for j in range(4):
			xi = matriz[i][j][1]
			yi = matriz[i][j][2]
			pygame.draw.rect(screen, matriz[i][j][3], [xi, yi, l, l])

#Função desenhar peças
def desenhar_pecas(matriz):
	for i in range(8):
		for j in range(4):
			#Peças brancas
			if matriz_tab[i][j][0] == 'b':
				pygame.draw.circle(screen, cor_brancas, [matriz[i][j][1] + l/2, matriz[i][j][2] + l/2], r)
				pygame.draw.circle(screen, black, [matriz[i][j][1] + l/2, matriz[i][j][2] + l/2], r, 1)
				pygame.draw.circle(screen, black, [matriz[i][j][1] + l/2, matriz[i][j][2] + l/2], 15, 1)

			#Peças pretas
			if matriz_tab[i][j][0] == 'p':
				pygame.draw.circle(screen, cor_pretas, [matriz[i][j][1] + l/2, matriz[i][j][2] + l/2], r)
				pygame.draw.circle(screen, black, [matriz[i][j][1] + l/2, matriz[i][j][2] + l/2], r, 1)
				pygame.draw.circle(screen, black, [matriz[i][j][1] + l/2, matriz[i][j][2] + l/2], 15, 1)

def val_mouse_click(c):
	for i in range(8):
		for j in range(4):
			if (c[0] >= matriz_tab[i][j][1] and c[0] <= matriz_tab[i][j][1] + l) and (c[1] >= matriz_tab[i][j][2] and c[1] <= matriz_tab[i][j][2] + l):
				if matriz_tab[i][j][0] == 'p' or matriz_tab[i][j][0] == 'b':
					return (i, j)
				else: return 0
	else: return 0

def casas_validas(coord):
	i = coord[0]
	j = coord[1]
	ls = []
	if i % 2 == 0:
		if i - 1 >= 0:
			ls.append([i - 1, j, verde])
			if j + 1 <= 3:
				ls.append([i-1, j+1, verde])
	else:
		ls.append([i-1, j, verde])
		if j-1 >= 0:
			ls.append([i-1, j-1, verde])

	return ls






Exit = True

while Exit:

	for event in pygame.event.get():
		#Evento para quitar game
		if event.type == pygame.QUIT:
			Exit = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			if val_mouse_click(mouse_pos) != 0:
				coord = val_mouse_click(mouse_pos)
				lista = casas_validas(coord)
				for a in range(len(lista)):
					matriz_tab[lista[a][0]][lista[a][1]][3] = lista[a][2]



	#Cor da tela (Branca)
	screen.fill(white)
	#Retângulo grande (Tabuleiro 2)
	pygame.draw.rect(screen, tabuleiro2, [200,100,400,400])
	#Retangulos pequenos (Tabuleiro 1)
	desenhar_tab1(matriz_tab)
	desenhar_pecas(matriz_tab)
	#locais onde as peças podem ir

	#Atualizar a tela
	pygame.display.update()

pygame.quit()
quit
