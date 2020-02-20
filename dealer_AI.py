import random
import pygame
import Developer_help
import Check_reasults
import Load_image
import Sound_effects
import Deck_module
'''
Dealer Ai modle actually contains probablities for diffrent number summaries and according to that randomize between probabilities
the chances of hit or stand
chance that i will pre make
each number will contain probabilities for stand or hit

the function will take in a number between 1 to 20 inclucive and check the probabilities set for him by randomizing
eventually it will return True for Hit and  False for stand
'''
def hit_answer_rules(cards_sum):
	if cards_sum < 17:
		return True
	else:
		return False

def hit_answer_challenge(cards_sum):
	'''
	this play is not according to the rules but allows a more intresting and challenging game.
	takes in only a number between 1-20 inclucive and returns boolean
	'''
	if cards_sum == 20 and cards_sum < 21:
		#for 20 , 5% to ask for hit. because it is very unlikel for a human to do so
		if random.randint(0,100) in range(0,5):
			return True
		else:
			return False
	elif cards_sum == 19 and cards_sum < 21:
		#for 19 , 10% to ask for hit.
		if random.randint(0,100) in range(0,10):
			return True
		else:
			return False
	elif cards_sum == 18 and cards_sum < 21:
		#for 18 , 15% to ask for hit
		if random.randint(0,100) in range(0,15):
			return True
		else:
			return False
	elif cards_sum == 17 and cards_sum < 21:
		#for 17 , 30% to ask for hit
		if random.randint(0,100) in range(0,30):
			return True
		else:
			return False
	elif cards_sum == 16 and cards_sum < 21:
		#for 16 , 40% becoming more likely to ask for hit
		if random.randint(0,100) in range(0,40):
			return True
		else:
			return False
	elif cards_sum == 15 and cards_sum < 21:
		#for 15 , 60%
		if random.randint(0,100) in range(0,60):
			return True
		else:
			return False
	elif cards_sum == 14 and cards_sum < 21:
		#for 14: 80%
		if random.randint(0,100) in range(0,80):
			return True
		else:
			return False
	elif cards_sum in range(10,14) and cards_sum < 21:
		#for 10-13 , 92%
		if random.randint(0,100) in range(0,92):
			return True
		else:
			return False
	elif cards_sum in range(8,10) and cards_sum < 21:
		#for  8,9 95%
		if random.randint(0,100) in range(0,95):
			return True
		else:
			return False
	elif cards_sum in range(0,8)  and cards_sum < 21:
		#(100%)
		return True
	else:
		return False

def ace_ans(cards_sum):
	'''
	check if is possible to use ace is 11
	'''
	if cards_sum+10 in range(17,22):
		return True
	else:
		return False


if __name__ == '__main__':
	n = input('enter a number between 1-20: ')
	if get_answer(n) is True:
		print('True')
	else:
		print('False')



#-------------------------------------------------------Dealer turn-------------------------------------------------
def dealer_turn(win,dealer_card1,dealer_card2,at_table):
	'''
	Because I need to create an AI player i will use a lot the random module
	takes in 2 card parameters and almost no user interface
	'''
	draw_effect = Sound_effects.get_sound('DRAW')
	pass_effect = Sound_effects.get_sound('PASS')
	card1_image = pygame.image.load(Load_image.get_card_image(dealer_card1))
	card2_image = pygame.image.load(Load_image.get_card_image(dealer_card2))
	card_x = 400
	card_y = 200
	#in order to view the cards on the screen, get card function imported from load_card_image module allows me to access loaction of image
	#without any trouble
	win.fill((0,150,0))
	draw_effect.play()
	win.blit(card1_image,(card_x,card_y))
	pygame.display.update()
	card_x+=40
	card_y+=40
	#stored coordinations in a variable in order to allow posting of new cards over the board also
	pygame.time.delay(500)
	draw_effect.play()
	win.blit(card2_image,(card_x,card_y))
	pygame.display.update()
	print('{} it is your turn'.format('Dealer'))
	######### correct the value
	dealer_card1 = Developer_help.correct_card_value(dealer_card1)
	dealer_card2 = Developer_help.correct_card_value(dealer_card2)
	cards_sum = Check_reasults.check_cards_sum(win, False, dealer_card1[0], dealer_card2[0])
	#i there is an ace let him decide
	if dealer_card1[0] == 1 or dealer_card2[0] == 1:
		if ace_ans(cards_sum) is True:
			cards_sum+=10
	dealer_turn = True
	while dealer_turn:
		pygame.time.delay(1000)
		dealer_turn = hit_answer_rules(cards_sum)
		if dealer_turn is True:
			draw_effect.play()
			new_card = Deck_module.pull_card()
			card_x+=40
			card_y+=40
			#post card image changes cordination so new posting could be shown
			new_card_image = pygame.image.load(Load_image.get_card_image(new_card))
			win.blit(new_card_image,(card_x,card_y))
			pygame.display.update()
			pygame.time.delay(1000)
			if new_card[0] == 1:
				if ace_ans(cards_sum):
					value_new_card = (11,'')#to save the same data type *tuple
				else:
					value_new_card = (1,'')
			value_new_card = Developer_help.correct_card_value(new_card)
			cards_sum = Check_reasults.check_cards_sum(win, False, value_new_card[0], cards_sum)
			if cards_sum == 21:
				return cards_sum
			elif cards_sum is False:
				return False
	pass_effect.play()
	print('The {} has ended his turn with sum of {}'.format('Dealer',cards_sum))
	Developer_help.write(win,'Stand',90,200,250)
	pygame.display.update()
	pygame.time.delay(2000)
	return cards_sum

			#so the function would stop and wont let the game continue