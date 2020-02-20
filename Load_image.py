import pygame
'''
This module was ment to help load images to cards games

IN: tuple (value,sign)
OUT: image location

the card variable is comprised of value and sign
'''
def get_card_image(card):
	value = card[0]
	sign = card[1]
	if sign == 'heart':
		if value == 1:
			image = ('Black_Jack_sprites/cards/heart/a.png')
		elif value == 2:
			image = ('Black_Jack_sprites/cards/heart/2.png')
		elif value == 3:
			image = ('Black_Jack_sprites/cards/heart/3.png')
		elif value == 4:
			image = ('Black_Jack_sprites/cards/heart/4.png')
		elif value == 5:
			image = ('Black_Jack_sprites/cards/heart/5.png')
		elif value == 6:
			image = ('Black_Jack_sprites/cards/heart/6.png')
		elif value == 7:
			image = ('Black_Jack_sprites/cards/heart/7.png')
		elif value == 8:
			image = ('Black_Jack_sprites/cards/heart/8.png')
		elif value == 9:
			image = ('Black_Jack_sprites/cards/heart/9.png')
		elif value == 10:
			image = ('Black_Jack_sprites/cards/heart/10.png')
		elif value == 11:
			image = ('Black_Jack_sprites/cards/heart/j.png')
		elif value == 12:
			image = ('Black_Jack_sprites/cards/heart/q.png')
		elif value == 13:
			image = ('Black_Jack_sprites/cards/heart/k.png')
	elif sign == 'diamond':
		if value == 1:
			image = ('Black_Jack_sprites/cards/diamond/a.png')
		elif value == 2:
			image = ('Black_Jack_sprites/cards/diamond/2.png')
		elif value == 3:
			image = ('Black_Jack_sprites/cards/diamond/3.png')		
		elif value == 4:
			image = ('Black_Jack_sprites/cards/diamond/4.png')
		elif value == 5:
			image = ('Black_Jack_sprites/cards/diamond/5.png')
		elif value == 6:
			image = ('Black_Jack_sprites/cards/diamond/6.png')
		elif value == 7:
			image = ('Black_Jack_sprites/cards/diamond/7.png')
		elif value == 8:
			image = ('Black_Jack_sprites/cards/diamond/8.png')		
		elif value == 9:
			image = ('Black_Jack_sprites/cards/diamond/9.png')
		elif value == 10:
			image = ('Black_Jack_sprites/cards/diamond/10.png')
		elif value == 11:
			image = ('Black_Jack_sprites/cards/diamond/j.png')
		elif value == 12:
			image = ('Black_Jack_sprites/cards/diamond/q.png')
		elif value == 13:
			image = ('Black_Jack_sprites/cards/diamond/k.png')
	elif sign == 'spade':
		if value == 1:
			image = ('Black_Jack_sprites/cards/spade/a.png')
		elif value == 2:
			image = ('Black_Jack_sprites/cards/spade/2.png')
		elif value == 3:
			image = ('Black_Jack_sprites/cards/spade/3.png')
		elif value == 4:
			image = ('Black_Jack_sprites/cards/spade/4.png')
		elif value == 5:
			image = ('Black_Jack_sprites/cards/spade/5.png')
		elif value == 6:
			image = ('Black_Jack_sprites/cards/spade/6.png')
		elif value == 7:
			image = ('Black_Jack_sprites/cards/spade/7.png')
		elif value == 8:
			image = ('Black_Jack_sprites/cards/spade/8.png')
		elif value == 9:
			image = ('Black_Jack_sprites/cards/spade/9.png')
		elif value == 10:
			image = ('Black_Jack_sprites/cards/spade/10.png')
		elif value == 11:
			image = ('Black_Jack_sprites/cards/spade/j.png')
		elif value == 12:
			image = ('Black_Jack_sprites/cards/spade/q.png')
		elif value == 13:
			image = ('Black_Jack_sprites/cards/spade/k.png')
	elif sign == 'clover':
		if value == 1:
			image = ('Black_Jack_sprites/cards/clover/a.png')
		elif value == 2:
			image = ('Black_Jack_sprites/cards/clover/2.png')
		elif value == 3:
			image = ('Black_Jack_sprites/cards/clover/3.png')
		elif value == 4:
			image = ('Black_Jack_sprites/cards/clover/4.png')
		elif value == 5:
			image = ('Black_Jack_sprites/cards/clover/5.png')
		elif value == 6:
			image = ('Black_Jack_sprites/cards/clover/6.png')
		elif value == 7:
			image = ('Black_Jack_sprites/cards/clover/7.png')
		elif value == 8:
			image = ('Black_Jack_sprites/cards/clover/8.png')
		elif value == 9:
			image = ('Black_Jack_sprites/cards/clover/9.png')
		elif value == 10:
			image = ('Black_Jack_sprites/cards/clover/10.png')
		elif value == 11:
			image = ('Black_Jack_sprites/cards/clover/j.png')
		elif value == 12:
			image = ('Black_Jack_sprites/cards/clover/q.png')
		elif value == 13:
			image = ('Black_Jack_sprites/cards/clover/k.png')
		else:
			return 0

	return image


def get_game_img(name):
	'''
		-----------------------images load-----------
		takes a 'name' in and puts out the image info according to the name recived
	'''

	image = pygame.image.load('Black_Jack_sprites/Title.png')
	white_chip = pygame.image.load('Black_Jack_sprites/chips/White.png')
	red_chip = pygame.image.load('Black_Jack_sprites/chips/Red.png')
	blue_chip = pygame.image.load('Black_Jack_sprites/chips/Blue.png')
	green_chip = pygame.image.load('Black_Jack_sprites/chips/Green.png')
	black_chip = pygame.image.load('Black_Jack_sprites/chips/Black.png')
	card_back = pygame.image.load('Black_Jack_sprites/cards/card_back.png')


	if name == 'TITLE':
		return image
	elif name == 'WHITE_CHIP':
		return white_chip
	elif name == 'RED_CHIP':
		return red_chip
	elif name == 'BLUE_CHIP':
		return blue_chip
	elif name == 'GREEN_CHIP':
		return green_chip
	elif name == 'BLACK_CHIP':
		return black_chip
	elif name == 'CARD_BACK':
		return card_back
	else:
		return 0
