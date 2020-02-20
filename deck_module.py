import random
import pygame


#a list to contain used cards and monitor them
sign_list = ['spade','heart','clover','diamond']
class CardDeck():
	'''
	This Deck will include 52 cards and it is going to be defined in a deck_for_game function
	each card will be defined by a sign and a number.
	this class purpose is to create a gaming to work on with other projects.
	'''
	def __init__(self,number,sign):
		'''
		each card has its own sign and number
		'''
		self.number = number
		self.sign = sign

#--------------- spade cards ---------------#
spade_A_low = CardDeck(1,sign_list[0])
spade_2 = CardDeck(2,sign_list[0])
spade_3 = CardDeck(3,sign_list[0])
spade_4 = CardDeck(4,sign_list[0])
spade_5 = CardDeck(5,sign_list[0])
spade_6 = CardDeck(6,sign_list[0])
spade_7 = CardDeck(7,sign_list[0])
spade_8 = CardDeck(8,sign_list[0])
spade_9 = CardDeck(9,sign_list[0])
spade_10 = CardDeck(10,sign_list[0])
spade_j = CardDeck(11,sign_list[0])
spade_q = CardDeck(12,sign_list[0])
spade_k = CardDeck(13,sign_list[0])
spade_A_high = CardDeck(14,sign_list[0])
#--------------- heart cards ---------------#
heart_A_low = CardDeck(1,sign_list[1])
heart_2 = CardDeck(2,sign_list[1])
heart_3 = CardDeck(3,sign_list[1])
heart_4 = CardDeck(4,sign_list[1])
heart_5 = CardDeck(5,sign_list[1])
heart_6 = CardDeck(6,sign_list[1])
heart_7 = CardDeck(7,sign_list[1])
heart_8 = CardDeck(8,sign_list[1])
heart_9 = CardDeck(9,sign_list[1])
heart_10 = CardDeck(10,sign_list[1])
heart_j = CardDeck(11,sign_list[1])
heart_q = CardDeck(12,sign_list[1])
heart_k = CardDeck(13,sign_list[1])
heart_A_high = CardDeck(14,sign_list[1])
#--------------- clover cards ---------------#
clover_A_low = CardDeck(1,sign_list[2])
clover_2 = CardDeck(2,sign_list[2])
clover_3 = CardDeck(3,sign_list[2])
clover_4 = CardDeck(4,sign_list[2])
clover_5 = CardDeck(5,sign_list[2])
clover_6 = CardDeck(6,sign_list[2])
clover_7 = CardDeck(7,sign_list[2])
clover_8 = CardDeck(8,sign_list[2])
clover_9 = CardDeck(9,sign_list[2])
clover_10 = CardDeck(10,sign_list[2])
clover_j = CardDeck(11,sign_list[2])
clover_q = CardDeck(12,sign_list[2])
clover_k = CardDeck(13,sign_list[2])
clover_A_high = CardDeck(14,sign_list[2])#In case of need
#--------------- diamond cards ---------------#
diamond_A_low = CardDeck(1,sign_list[3])
diamond_2 = CardDeck(2,sign_list[3])
diamond_3 = CardDeck(3,sign_list[3])
diamond_4 = CardDeck(4,sign_list[3])
diamond_5 = CardDeck(5,sign_list[3])
diamond_6 = CardDeck(6,sign_list[3])
diamond_7 = CardDeck(7,sign_list[3])
diamond_8 = CardDeck(8,sign_list[3])
diamond_9 = CardDeck(9,sign_list[3])
diamond_10 = CardDeck(10,sign_list[3])
diamond_j = CardDeck(11,sign_list[3])
diamond_q = CardDeck(12,sign_list[3])
diamond_k = CardDeck(13,sign_list[3])
diamond_A_high = CardDeck(14,sign_list[3])
#--------------------------------------------#

deck = [spade_A_low,spade_2,spade_3,spade_4,spade_5,spade_6,spade_7,spade_8,spade_9,spade_10,spade_j,spade_q,spade_k,
heart_A_low,heart_2,heart_3,heart_4,heart_5,heart_6,heart_7,heart_8,heart_8,heart_9,heart_10,heart_j,heart_q,heart_k,
clover_A_low,clover_2,clover_3,clover_4,clover_5,clover_6,clover_7,clover_8,clover_9,clover_10,clover_j,clover_q,clover_k,
diamond_A_low,diamond_2,diamond_3,diamond_4,diamond_5,diamond_6,diamond_7,diamond_8,diamond_9,diamond_10,diamond_j,diamond_q,
diamond_k]


def pull_rand_card():
	#pull card from deck
	rand_num = random.randint(1,52)
	return (deck[rand_num].number,deck[rand_num].sign)
	return pull_rand_card() 

used_cards = []
def pull_card():
	'''
	Checks if a card was burnt
	and makes sure circulation occurs after a deck is done
	'''
	global used_cards
	pulled_card = pull_rand_card()
	while pulled_card in used_cards:#all the cards
		pulled_card = pull_rand_card()#set new card
		if len(used_cards) == 51:
			#if all cards were used
			print('All cards were burned , reseting deck now')
			used_cards = []
			pulled_card = pull_rand_card()
			break
			#break from while loop to return card
	used_cards.append(pulled_card)
	return pulled_card




if __name__ == '__main__':
	print('random card is:')
	deck_for_game()