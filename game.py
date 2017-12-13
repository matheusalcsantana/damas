#!/usr/bin/env python
#coding:utf-8

import pygame

white = 255,255,255

screen = pygame.display.set_mode((640,400))

Exit = True

while Exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Exit = False

	screen.fill(white)
	pygame.display.flip()

pygame.quit()
quit
	
