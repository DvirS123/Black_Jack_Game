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
	rule1 = "1 - The goal of blackjack is to beat the dealer's hand without going over 21."
	rule2 = "2 - Face cards are worth 10..."
	rule3 = "3 - Each player starts with two cards."
	rule4 = "4 - To 'Hit' is to ask for another card. ..."
	rule5 = "5 - If you go over 21 you bust, and the dealer wins regardless of the dealer's hand."
	rule6 = "6 - In order to win the game you must aquire a balance of 3000 chips"
	rule7 = "7 - If you reach a balance of 0 you lose"
	rule8 = "8 - Doubling down means doubling the origina bet, this can occur only when the"
	line8 = "	   value of the cards is 9,10 or 11."
	rule9 = "9 - Spliting means to divide you hand to two seprate hands plus adding"
	line9 = "	   original bet,this can occur only when original cards are identical"

	win.fill((0,150,0))

	write(win,rule1,25,5,200)
	write(win,rule2,25,5,230)
	write(win,rule3,25,5,260)
	write(win,rule4,25,5,290)
	write(win,rule5,25,5,320)
	write(win,rule6,25,5,350)
	write(win,rule7,25,5,380)
	write(win,rule8,25,5,410)
	write(win,line8,25,5,430)
	write(win,rule9,25,5,460)
	write(win,line9,25,5,480)
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
