import pygame
import Classes_objects
import Sound_effects
import Deck_module
import Load_image
import Check_reasults
import Developer_help


##################################################### lOAD #################3

#------------------------------------------------------------ buttons -------------------------
pass_turn_button = Classes_objects.get_button('PASS_TURN')
hit_button = Classes_objects.get_button('HIT')
back_button = Classes_objects.get_button('BACK')
low_ace_button = Classes_objects.get_button('LOW_ACE')
high_ace_button = Classes_objects.get_button('HIGH_ACE')
split_button = Classes_objects.get_button('SPLIT')
#------------------------------------------------------------- sound --------------------------
draw_effect = Sound_effects.get_sound('DRAW')
pass_effect = Sound_effects.get_sound('PASS')
button_effect = Sound_effects.get_sound('BUTTON')


def split(win,card1,card2,player1_name):

	pygame.draw.rect(win,(0,150,0),(175,200,450,250),0)#to reset the board
	card1_image = pygame.image.load(Load_image.get_card_image(card1))
	card2_image = pygame.image.load(Load_image.get_card_image(card2))
	card1 = Developer_help.correct_card_value(card1)
	card2 = Developer_help.correct_card_value(card2)
	hand1_x = 400
	hand1_y = 200
	hand2_x = 200
	hand2_y = 200
	win.blit(card1_image,(hand1_x,hand1_y))
	win.blit(card2_image,(hand2_x,hand2_y))
	pygame.display.update()
	is_ace = False
	is_natural = True
	cards_sum = Check_reasults.check_cards_sum(win,is_natural,card2[0])
	low_ace_button.x-=150
	high_ace_button.x-=150

	while cards_sum < 21:
		#check if ace
		if card1[0] == 1 or card2[0] == 1 :
			is_ace = True 

		pass_turn_button.draw(win,(0,0,0))
		hit_button.draw(win,(0,0,0))
		back_button.draw(win,(0,0,0))

		#----------------------------------Turn-------------------------------#
		pygame.time.delay(50)
		pygame.display.update()
		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()
			###############################################if mouse moves
			if event.type == pygame.MOUSEMOTION:
				if back_button.is_over(pos):
					back_button.color = (0,0,255)
				else:
					back_button.color = (255,0,0)

				if pass_turn_button.is_over(pos):
					pass_turn_button.color = (0,0,255)
				else:
					pass_turn_button.color = (255,0,0)

				if hit_button.is_over(pos):
					hit_button.color = (0,0,255)
				else:
					hit_button.color = (255,0,0)

				if is_ace:
					#show buttons first
					low_ace_button.draw(win,(0,0,0))
					high_ace_button.draw(win,(0,0,0))

					if low_ace_button.is_over(pos):
						low_ace_button.color = (0,0,255)
					else:
						low_ace_button.color = (255,0,0)
					if high_ace_button.is_over(pos):
						high_ace_button.color = (0,0,255)
					else:
						high_ace_button.color = (255,0,0)

						
					#####################################################if mouse clicks
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.is_over(pos):
					button_effect.play()
					return 'back'
				if pass_turn_button.is_over(pos):
					pass_effect.play()
					is_split = False
					print('Player {} has ended his first hand with sum of {}'.format(player1_name,cards_sum))
					Developer_help.write(win,'Stand',90,200,100)
					pygame.display.update()
					pygame.time.delay(2000)
					pygame.draw.rect(win,(0,150,0),(175,0,300,200),0)#to reset the boar
					pygame.display.update()
					return cards_sum
				if hit_button.is_over(pos):
					draw_effect.play()
					is_natural = False
					new_card = Deck_module.pull_card()
					hand2_x+=40
					hand2_y+=40
					#post card image changes cordination so new posting could be shown
					new_card_image = pygame.image.load(Load_image.get_card_image(new_card))
					win.blit(new_card_image,(hand2_x,hand2_y))
					pygame.display.update()
					pygame.time.delay(1000)
					##################change j,q,k values to 10
					new_card = Developer_help.correct_card_value(new_card)
					if new_card[0] == 1:
						is_ace = True
					else:
						is_ace = False
					cards_sum = Check_reasults.check_cards_sum(win,is_natural,new_card[0],cards_sum)
					last_card = new_card
					if cards_sum is False:
						return False
					elif cards_sum is True:
						return 21
					#so the function would stop and wont let the game continue
				if low_ace_button.is_over(pos):
					button_effect.play()
					is_ace = False
					pygame.draw.rect(win,(0,150,0),(40,190,120,275),0)#scrap button
				if high_ace_button.is_over(pos):
					button_effect.play()
					is_ace = False
					pygame.draw.rect(win,(0,150,0),(40,190,120,275),0)#scrap button
					cards_sum = Check_reasults.check_cards_sum(win,is_natural,10,cards_sum)
					if cards_sum is True:
						return 21
					elif cards_sum is False:
						return False


			if event.type == pygame.QUIT:
				return 'quit'

	#returns 21 if value is equal to 21!
	return cards_sum

