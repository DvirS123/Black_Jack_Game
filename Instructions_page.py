import pygame
import Classes_objects
import Sound_effects
from Developer_help import write

back_button = Classes_objects.get_button('BACK')
button_effect = Sound_effects.get_sound('BUTTON')


#This page was ment to show instructions

def show_instructions(win):
	'''
	Page to show instructions about the game
	'''
	rule1 = " - The goal of blackjack is to beat the dealer's hand without going over 21."
	rule2 = " - Face cards are worth 10..."
	rule3 = " - Each player starts with two cards."
	rule4 = " - To 'Hit' is to ask for another card. ..."
	rule5 = " - If you go over 21 you bust, and the dealer wins regardless of the dealer's hand."
	rule6 = " - In order to win the game you must aquire a balance of 800 chips"
	rule7 = " - If you reach a balance of 0 you lose"

	win.fill((0,150,0))

	write(win,rule1,25,25,200)
	write(win,rule2,25,25,250)
	write(win,rule3,25,25,300)
	write(win,rule4,25,25,350)
	write(win,rule5,25,25,400)
	write(win,rule6,25,25,450)
	write(win,rule7,25,25,500)
	write(win,'Good Luck!',50,275,550)

	while True:
		pygame.time.delay(50)
		pygame.display.update()
		#screen support

		back_button.draw(win,(0,0,0))

		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()
			#get mouse position
			if event.type == pygame.MOUSEMOTION:

				if back_button.is_over(pos):
					back_button.color = (0,0,255)
				else:
					back_button.color = (255,0,0)

			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.is_over(pos):#in range of 'back' button
					button_effect.play()
					return True #back to main

			if event.type == pygame.QUIT:
				return False
