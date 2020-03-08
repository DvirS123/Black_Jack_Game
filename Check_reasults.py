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
		Developer_help.write(win,'Black Jack!',90,175,100)
		pygame.display.update()
		pygame.time.delay(2000)
		pygame.draw.rect(win,(0,150,0),(175,0,350,200),0)#to reset the board
		pygame.display.update()
		return True

	elif new_cards_sum == 21:#if won
		# if 21 first turn return stand which is true
		print('21!, Stand')
		Developer_help.write(win,'21!, Stand',90,200,100)
		pygame.display.update()
		pygame.time.delay(3000)
		pygame.draw.rect(win,(0,150,0),(175,0,350,200),0)#to reset the board
		pygame.display.update()
		return 21

		#if Bust
	elif new_cards_sum > 21 :
		print('BUST')
		pygame.time.delay(1000)
		Developer_help.write(win,'BUST',90,200,100)
		pygame.display.update()
		pygame.time.delay(2000)
		pygame.draw.rect(win,(0,150,0),(175,0,300,200),0)#to reset the board
		pygame.display.update()
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


def check_game_reasults_split(win, dealer_reasults, player1_hand1, player1_hand2, table_balance, player1_bet, player1_name):
	'''
	Function takes two numbers and makes comparison between them to show who won
	'''
	if dealer_reasults == player1_hand1 and dealer_reasults == player1_hand2:
		#tie
		print('Its a TIE')
		Developer_help.write(win,'Tie',90,100,300)
		pygame.display.update()
		pygame.time.delay(2000)
		# return the amount the player has bet
		return player1_bet

	elif dealer_reasults > player1_hand1 and dealer_reasults == player1_hand2:
		print('Its a TIE')
		Developer_help.write(win,'Tie with one hand',90,100,300)
		pygame.display.update()
		pygame.time.delay(2000)
		# return the amount the player has bet divided by two
		return round(player1_bet/2)

	elif dealer_reasults == player1_hand1 and dealer_reasults > player1_hand2:
		print('Its a TIE')
		Developer_help.write(win,'Tie with one hand',90,100,300)
		pygame.display.update()
		pygame.time.delay(2000)
		# return the amount the player has bet divided by two
		return round(player1_bet/2)

	elif dealer_reasults > player1_hand1 and dealer_reasults > player1_hand2:
		#if dealer won
		print('The Dealer has won')
		Developer_help.write(win,'The Dealer has won!',90,100,300)
		pygame.display.update()
		pygame.time.delay(2000)
		#player1 lost no amount to return
		return 0

	elif player1_hand1 > dealer_reasults and player1_hand2 > dealer_reasults:
		#if player1 won with two hands
		print('Player1 won')
		Developer_help.write(win,'{} has won {} chips!'.format(player1_name,table_balance),90,20,300)
		pygame.display.update()
		pygame.time.delay(2000)
		return table_balance

	elif player1_hand1 > dealer_reasults or player1_hand2 > dealer_reasults:
		#if player1 won with one hand only
		print('Player1 won')
		Developer_help.write(win,'{} has won {} chips!'.format(player1_name,table_balance - player1_bet),90,20,300)
		pygame.display.update()
		pygame.time.delay(2000)
		return table_balance - player1_bet


def check_if_won(win, player1_balance, player1_name):

	if player1_balance >=3000:
		Developer_help.write(win,'{} Has won , Congrats!'.format(player1_name),90,20,100)
		pygame.display.update()
		pygame.mixer.music.pause()
		pygame.time.delay(500)
		Sound_effects.get_sound('WIN').play()
		pygame.time.delay(4000)
		pygame.mixer.music.unpause()

	elif player1_balance <=0:
		Developer_help.write(win,'{} Has lost'.format(player1_name),90,200,100)
		pygame.display.update()
		pygame.mixer.music.pause()
		pygame.time.delay(500)
		Sound_effects.get_sound('LOSE').play()
		pygame.time.delay(3000)
		pygame.mixer.music.unpause()
		pygame.time.delay(500)




