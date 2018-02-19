#!/usr/bin/env python
#coding:utf-8

import pygame

pygame.init()
pygame.font.init()

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

	movimentos = []
	origem = []
	pulo_pretas = 0
	pulo_brancas = 0
	pecas_puladas = []

	def __init__(self):
		global matriz_tab

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
						print "movimentos zerado"
						self.casas_validas((i,j))
						self.origem = [i, j]
					else:
						print "movimentos n zerado"
						if [i, j] in self.movimentos:
							print "se i, j in movimentos"
							destino = [i, j]
							print "origem", self.origem
							self.movimentar_peca(self.origem, destino)
							self.resetar_cor_tab()
							self.zerar_atributos()
						elif matriz_tab[i][j][0] == 'p' or matriz_tab[i][j][0] == 'b':
							print "click em cima peca"
							self.zerar_atributos()
							self.resetar_cor_tab()
							self.casas_validas((i,j))
							self.origem = [i, j]
						else:
							print "misclick"
							self.resetar_cor_tab()
							self.zerar_atributos()
		if e != 0:
			print "misclick"
			self.resetar_cor_tab()
			self.zerar_atributos()

	def casas_validas(self, coord):
		i = coord[0]
		j = coord[1]
		ls = []
		movs = []
		if self.matriz_tab[i][j][0] == 'b':
			#Peça branca, linha par
			if i % 2 == 0:
				#Verificar se a casa acima existe
				if i - 1 >= 0:
					#Verificar se a casa acima j é vazia
					if self.matriz_tab[i-1][j][0] == ' ':
						ls.append([i - 1, j, verde])
					#Verificar se a casa acima j tem uma peça preta
					elif self.matriz_tab[i-1][j][0] == 'p':
						#Verificar se a casa acima da j, [i-2, j-1], existe
						if i-2 >= 0 and j-1 >=0:
							#Verificar se a casa acima da j, [i-2, j-1], é vazia
							if self.matriz_tab[i-2][j-1][0] == ' ':
								ls.append([i-2, j-1, verde])
								self.pecas_puladas.append([i-1, j])
					#Verificar se a casa acima j + 1 existe
					if j + 1 <= 3:
						#Verificar se a casa acima j + 1 é vazia
						if self.matriz_tab[i-1][j+1][0] == ' ':
							ls.append([i - 1, j + 1, verde])
						#Verificar se a casa acima j + 1 tem uma peça preta
						elif self.matriz_tab[i-1][j+1][0] == 'p':
							#Verificar se a casa acima da j + 1, [i-2, j+1], existe
							if i-2 >= 0 and j+1 <= 3:
								#Verificar se a casa da j + 1 acima, [i-2, j+1], é vazia
								if self.matriz_tab[i-2][j+1][0] == ' ':
									ls.append([i-2, j+1, verde])
									self.pecas_puladas.append([i-1, j+1])

			else:
				#Peça branca, linha impar
				#Verificar se a casa acima j é vazia
				if self.matriz_tab[i-1][j][0] == ' ':
					ls.append([i - 1, j, verde])
				#Verificar se a casa acima j tem uma peça preta
				elif self.matriz_tab[i-1][j][0] == 'p':
					#Verificar se a casa acima da j, [i-2, j+1], existe
					if i-2 >= 0 and j+1 <= 3:
						#Verificar se a casa acima da j, [i-2, j+1], é vazia
						if self.matriz_tab[i-2][j+1][0] == ' ':
							ls.append([i-2, j+1, verde])
							self.pecas_puladas.append([i-1, j])
				#Verificar se a casa acima j - 1 existe
				if j-1 >= 0:
					#Verificar se a casa acima j -1  é vazia
					if self.matriz_tab[i-1][j-1][0] == ' ':
						ls.append([i - 1, j -1, verde])
					#Verificar se a casa acima j -1 tem uma peça preta
					elif self.matriz_tab[i-1][j-1][0] == 'p':
						#Verificar se a casa acima da j -1, [i-2, j-1], existe
						if i-2 >= 0 and j-1 >= 0:
							#Verificar se a casa acima da j, [i-2, j-1], é vazia
							if self.matriz_tab[i-2][j-1][0] == ' ':
								ls.append([i-2, j-1, verde])
								self.pecas_puladas.append([i-1, j-1])

		elif self.matriz_tab[i][j][0] == 'p':
			if i % 2 != 0:
				j -= 1
				par = False
			else:
				par = True
				#Peças PRETAS, linha PAR
					#Verificar se casa [i+1, j] é VAZIA ou BRANCA
			if self.matriz_tab[i+1][j][0] == ' ':
				ls.append([i+1, j, verde])
			elif self.matriz_tab[i+1][j][0] == 'b':
				#Verificar se casa acima [i+2, j-1] existe e é vazia
				if par:
					if i + 2 <= 7 and j - 1 >= 0:
						if self.matriz_tab[i+2][j-1][0] == ' ':
							ls.append([i+2, j-1, verde])
							self.pecas_puladas.append([i+1, j])
				else:
					if i + 2 <= 7:
						if self.matriz_tab[i+2][j][0] == ' ':
							ls.append([i+2, j, verde])
							self.pecas_puladas.append([i+1, j])
			#Verificar se casa [i+1, j+1] existe
			if j + 1 <= 3:
				#Verificar se casa [i+1, j+1] é VAZIA ou BRANCA
				if self.matriz_tab[i+1][j+1][0] == ' ':
					ls.append([i+1, j+1, verde])
				if self.matriz_tab[i+1][j+1][0] == 'b':
					if par:
						if i + 2 <= 7 and j + 1 <= 3:
							if self.matriz_tab[i+2][j+1][0] == ' ':
								ls.append([i+2, j+1, verde])
								self.pecas_puladas.append([i+1, j+1])
					else:
						if i + 2 <= 7 and j + 2 <= 3:
							if self.matriz_tab[i+2][j+2][0] == ' ':
								ls.append([i+2, j+2, verde])
								self.pecas_puladas.append([i+1, j+1])
			'''else:
				if i + 1 <= 7:
					ls.append([i+1, j, verde])
					if j-1 >= 0:
						ls.append([i+1, j-1, verde])'''

		for a in range(len(ls)):
			self.matriz_tab[ls[a][0]][ls[a][1]][3] = ls[a][2]
			self.movimentos.append([ls[a][0], ls[a][1]])

	#Função para resetar cores tabuleiro
	def resetar_cor_tab(self):
		for i in range(8):
			for j in range(4):
				self.matriz_tab[i][j][3] = tabuleiro1

	#Função movimentar a peça
	def movimentar_peca(self, origem, destino):
		self.matriz_tab[origem[0]][origem[1]][0], self.matriz_tab[destino[0]][destino[1]][0] = self.matriz_tab[destino[0]][destino[1]][0], self.matriz_tab[origem[0]][origem[1]][0]
		if self.pecas_puladas != []:
			for m in self.pecas_puladas:
				i = m[0]
				j = m[1]
				self.matriz_tab[i][j][0] = ' '
			self.pecas_puladas = []

	def zerar_atributos(self):
		self.movimentos = []
		self.origem = []
		self.pecas_puladas = []

font_ingame = pygame.font.SysFont('Comic Sans MS', 25)

def msg_ingame(msg, coordenas):
	text = font_ingame.render(msg, True, black)
	screen.blit(text, coordenas)

Exit = True

jogo = Jogo()

while Exit:

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
	texto_teste = pygame.font.SysFont('Comic Sans MS', 30)

	#Atualizar a tela
	pygame.display.update()

pygame.quit()
quit
