import pygame
pygame.init()

pygame.mixer.music.load('Sound_effects\Solar.mp3')
pygame.mixer.music.play(-1)



def get_sound(name):
	'''
	#---------------------- sound load -------------
	'''
	if name == 'BUTTON':
		return pygame.mixer.Sound('Sound_effects\Metal Click.wav')
	elif name == 'DRAW':
		return pygame.mixer.Sound('Sound_effects\draw.wav')
	elif name == 'PASS':
		return pygame.mixer.Sound('Sound_effects\Passturn.wav')
	elif name == 'WIN':
		return pygame.mixer.Sound('Sound_effects\end_level.flac')
	elif name == 'LOSE':
		return pygame.mixer.Sound('Sound_effects\lose.wav')
	else:
		print('Please choose a valid sound')
