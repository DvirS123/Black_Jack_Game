import pygame

def write(win,text,size,x,y):
	win.blit(((pygame.font.SysFont('comiscans',size)).render(text,1,(0,0,0))),(x,y))
	return 0

def correct_card_value(card):
	'''
	Function takes card and corrects it to the right card value according to the game rules
	'''
	if card[0] in range(11,14):
		return (10,card[1])
	else:
		return card