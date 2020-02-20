import pygame
import Developer_help
import Sound_effects

def check_cards_sum(win, is_natural, card1, card2 = 0, cards_sum = 0):
	'''
	After a hit or at the start of a turn checks the situation of the player
	return new sum of cards or reasult of actions
	'''
	new_cards_sum = cards_sum + card1 + card2

		#if won natural
	if new_cards_sum == 21 and is_natural:
		Developer_help.write(win,'Black Jack!',90,200,250)
		pygame.display.update()
		pygame.time.delay(2000)
		return True

	elif new_cards_sum == 21:#if won
		# if 21 first turn return stand which is true
		print('21!, Stand')
		Developer_help.write(win,'21!, Stand',90,200,250)
		pygame.display.update()
		pygame.time.delay(3000)
		return 21

		#if Bust
	elif new_cards_sum > 21 :
		print('BUST')
		pygame.time.delay(1000)
		Developer_help.write(win,'BUST',90,200,250)
		pygame.display.update()
		pygame.time.delay(2000)
		return False
	else:
		return new_cards_sum

def check_game_reasults(win, dealer_reasults, player1_reasults, table_balance, player1_bet, player1_name):
	'''
	Function takes two numbers and makes comparison between them to show who won
	'''
	if dealer_reasults == player1_reasults:
		#tie
		print('Its a TIE')
		Developer_help.write(win,'Tie',90,100,300)
		pygame.display.update()
		pygame.time.delay(2000)
		# return the amount the player has bet
		return player1_bet

	elif dealer_reasults > player1_reasults:
		#if dealer won
		print('The Dealer has won')
		Developer_help.write(win,'The Dealer has won!',90,100,300)
		pygame.display.update()
		pygame.time.delay(2000)
		#player1 lost no amount to return
		return 0

	elif player1_reasults > dealer_reasults:
		#if player1 won 
		print('Player1 won')
		Developer_help.write(win,'{} has won {} chips!'.format(player1_name,table_balance),90,20,300)
		pygame.display.update()
		pygame.time.delay(2000)
		return table_balance

def check_if_won(win, player1_balance, player1_name):

	if player1_balance >=800:
		Developer_help.write(win,'{} Has won , Congrats!'.format(player1_name),90,20,100)
		pygame.display.update()
		Sound_effects.get_sound('WIN').play()
		pygame.time.delay(3000)

	elif player1_balance <=0:
		Developer_help.write(win,'{} Has lost'.format(player1_name),90,200,100)
		pygame.display.update()
		Sound_effects.get_sound('LOSE').play()
		pygame.time.delay(3000)




