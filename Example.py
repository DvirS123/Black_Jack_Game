import pygame
'''
This file was ment to learn how to add the chip buttons properly
'''
pygame.init()

win = pygame.display.set_mode((750,500))

win.fill((0,0,0))

pygame.display.set_caption('Example')

white_chip = pygame.image.load(r'C:\Users\97254\Desktop\Python 3\Black_Jack_Project\Black_Jack_sprites\chips\White.png')

run = True
while run:
	pygame.draw.circle(win,(150,0,0),(100,285),35)
	win.blit(white_chip,(250,250))
	pygame.time.delay(50)
	pygame.display.update()
	for event in pygame.event.get():
		pos = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEMOTION and pos[0] in range(255,315) and pos[1] in range(255,315):
			print('is over')
		if event.type == pygame.QUIT:
			run = False