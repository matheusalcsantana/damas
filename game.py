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

class Jogo:

	def __init__(self):
		global matriz_tab
		self.movimentos = []
		self.obrigatorios = []
		self.origem = None
		self.matriz_tab = matriz_tab


	#Função que vai receber a cor da matriz_tab e mudar de acordo com a necessidade
	def desenhar_tab1(self):
		matriz_tab = self.matriz_tab
		for i in range(8):
			for j in range(4):
				xi = matriz_tab[i][j][1]
				yi = matriz_tab[i][j][2]
				pygame.draw.rect(screen, matriz_tab[i][j][3], [xi, yi, l, l])

	#Função desenhar peças
	def desenhar_pecas(self):
		for i in range(8):
			for j in range(4):
				matriz_tab = self.matriz_tab
				#Peças brancas
				if matriz_tab[i][j][0] == 'b':
					pygame.draw.circle(screen, cor_brancas, [matriz_tab[i][j][1] + l/2, matriz_tab[i][j][2] + l/2], r)
					pygame.draw.circle(screen, black, [matriz_tab[i][j][1] + l/2, matriz_tab[i][j][2] + l/2], r, 1)
					pygame.draw.circle(screen, black, [matriz_tab[i][j][1] + l/2, matriz_tab[i][j][2] + l/2], 15, 1)

				#Peças pretas
				if matriz_tab[i][j][0] == 'p':
					pygame.draw.circle(screen, cor_pretas, [matriz_tab[i][j][1] + l/2, matriz_tab[i][j][2] + l/2], r)
					pygame.draw.circle(screen, black, [matriz_tab[i][j][1] + l/2, matriz_tab[i][j][2] + l/2], r, 1)
					pygame.draw.circle(screen, black, [matriz_tab[i][j][1] + l/2, matriz_tab[i][j][2] + l/2], 15, 1)

	#Função receber as coordenas do click e encaminhar
	def val_mouse_click(self, c):
		e = 1
		matriz_tab = self.matriz_tab
		for i in range(8):
			for j in range(4):
				if (c[0] >= matriz_tab[i][j][1] and c[0] <= matriz_tab[i][j][1] + l) and (c[1] >= matriz_tab[i][j][2] and c[1] <= matriz_tab[i][j][2] + l):
					e = 0
					print self.movimentos
					if self.movimentos == []:
						print "flag1"
						self.casas_validas((i,j))
						self.origem = [i, j]
					else:
						print "flag2"
						if [i, j] in self.movimentos:
							print "flag3"
							destino = [i, j]
							self.movimentar_peca(self.origem, destino)
							self.resetar_cor_tab()
							self.movimentos = []
							self.origem = []
						elif matriz_tab[i][j][0] == 'p' or matriz_tab[i][j][0] == 'b':
							print "flag4"
							self.movimentos = []
							self.resetar_cor_tab()
							self.casas_validas((i,j))
							self.origem = [i, j]
						else:
							print "flag5"
							self.resetar_cor_tab()
							self.movimentos = []
		if e != 0:
			print "flag6"
			self.resetar_cor_tab()
			self.movimentos = []

	def casas_validas(self, coord):
		i = coord[0]
		j = coord[1]
		ls = []
		movs = []
		if self.matriz_tab[i][j][0] == 'b':
			if i % 2 == 0:
				if i - 1 >= 0:
					ls.append([i - 1, j, verde])
					if j + 1 <= 3:
						ls.append([i-1, j+1, verde])
			else:
				ls.append([i-1, j, verde])
				if j-1 >= 0:
					ls.append([i-1, j-1, verde])

		for a in range(len(ls)):
			self.matriz_tab[ls[a][0]][ls[a][1]][3] = ls[a][2]
			movs.append([ls[a][0], ls[a][1]])
			self.movimentos = movs

	#Função para resetar cores tabuleiro
	def resetar_cor_tab(self):
		for i in range(8):
			for j in range(4):
				self.matriz_tab[i][j][3] = tabuleiro1

	#Função movimentar a peça
	def movimentar_peca(self, origem, destino):
		self.matriz_tab[origem[0]][origem[1]][0], self.matriz_tab[destino[0]][destino[1]][0] = self.matriz_tab[destino[0]][destino[1]][0], self.matriz_tab[origem[0]][origem[1]][0]

Exit = True

while Exit:
	jogo = Jogo()
	for event in pygame.event.get():
		#Evento para quitar game
		if event.type == pygame.QUIT:
			Exit = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			jogo.val_mouse_click(mouse_pos)


	#Cor da tela (Branca)
	screen.fill(white)
	#Retângulo grande (Tabuleiro 2)
	pygame.draw.rect(screen, tabuleiro2, [200,100,400,400])
	#Retangulos pequenos (Tabuleiro 1)
	jogo.desenhar_tab1()
	jogo.desenhar_pecas()
	#locais onde as peças podem ir

	#Atualizar a tela
	pygame.display.update()

pygame.quit()
quit
