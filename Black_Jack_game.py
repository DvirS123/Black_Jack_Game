#in this file i am going to start the main program in which i am going to build the game
import Dealer_AI
import Load_image
import Deck_module
import pygame
import random
import Instructions_page
import About_page
import Menu_page
import Classes_objects
import Developer_help
import Player_phases
import Sound_effects
import Check_reasults
pygame.init()
#initiating pygame
################################################################## SETTINGS ####################################################

#Creating a window
win = pygame.display.set_mode((750,600))
# color fill green
win.fill((0,150,0))
#naming game
pygame.display.set_caption('Black Jack game')
#create object player
used_cards = []#cards that were already played cannot show again that is why cards will accumulate here as game keeps going
is_turn = True#refering the turns
in_natural = True


#------------------------------------------------------------------defining what is going on the game screen----------------------------------------
def game_screen():
	#------------------------settings--------------#
	win.fill((0,150,0))
	#used_cards = []#cards that were already played cannot show again that is why cards will accumulate here as game keeps going
	#----------------------------------------------------PULL RAND FUNCTION------------------------------
	#------------------------------------------------------Check action reasult -------------------------------
	#-------------------------------------------------------------GAME LOOP-------------------------#
	gameScreen = True
	while gameScreen:
		#small delay
		pygame.time.delay(50)
		#update window
		pygame.display.update()
		#----------------------------------Events---------------------------------
		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()
			#get mouse position
			#############CHECK IF MOUSE IS OVER A BUTTON######
			if event.type == pygame.MOUSEMOTION:
				if red_back_button.is_over(pos):
					blue_back_button.draw(win,(0,0,0))
				else:
					red_back_button.draw(win,(0,0,0))
			############## check if mouse is pressing button############
			if event.type == pygame.MOUSEBUTTONDOWN:
				if red_back_button.is_over(pos):
					#return true for keep running and end function
					print('back button pressed')
					return True
			#================================================================DEFINE THE GAME ===============================================
			dealer.balance = dealer.start_chip
			player1.balance = player1.start_chip
			is_round = True
			while is_round:#############################round loop#########################
				#check if a player lost:
				if player1.balance == 0:

					return True

				#first pull cards

				######################################################################
				if True:
					player1_bet = set_bet(player1.balance)
					if player1_bet == 'back':
						return True
					elif player1_bet == 'quit':
						return False
					player_turn = player1_turn(player1_card1,player1_card2,table.balance)
					# returned 'back' if pressed back
					if player_turn == 'back' :
						return True
					#returned 'quit' if event quit
					elif player_turn == 'quit':
						return False
					elif player_turn is False:
						#if player 1 lost which means dealer won
						dealer.win(table.balance)
						write('Dealer takes {} chips'.format(table.balance),90,50,300)
						table.balance = 0
						pygame.display.update()
						pygame.time.delay(2000)
					if player_turn == 21 and is_natural:
						#if player1 won 21 first turn
						write('{} Wins {} chips'.format(player1.name,round(table.balance*1.5)),90,50,300)
						pygame.display.update()
						pygame.time.delay(2000)
						player1.win(round(table.balance*1.5))
						table.balance = 0
					if player_turn is True and is_natural is False:
						#if player1 won not naturally
						is_dealer_turn = dealer_turn(dealer_card1,dealer_card2,table.balance)
						# returned 'back' if pressed back
						if is_dealer_turn == 'back' :
							return True
						#returned 'quit' if event quit
						elif is_dealer_turn == 'quit':
							return False
						#dealer_turn(dealer_card1,dealer_card2)
						elif is_dealer_turn is True:
							#Tie both got 21
							print('Its a TIE')
							#if its a tie than cut the vet to half and give one more chip to dealer
							player1.win(player1_bet)
							#splittig chips
							table.balance=0
							write('Tie',90,250,300)
							pygame.display.update()
							pygame.time.delay(1000)

						else:
							#in case player 1 won and dealer lost
							player1.win(table.balance)
							write('{} wins {} chips'.format(player1.name,player1.balance),90,50,300)
							pygame.display.update()
							pygame.time.delay(2000)

					elif player_turn <= 20 and player_turn is not False and player_turn is not True:
						#if player ones turn has ended with a sum
						if player_turn <=20:
							is_dealer_turn = dealer_turn(dealer_card1,dealer_card2,table.balance)
							# returned 'back' if pressed back
							if is_dealer_turn == 'back' :
								return True
							#returned 'quit' if event quit
							elif is_dealer_turn == 'quit':
								return False





							else:
								#in case player 1 won and dealer lost
								player1.win(table.balance)
								write('{} wins {} chips'.format(player1.name,table.balance),90,50,300)
								table.balance = 0
								pygame.display.update()
								pygame.time.delay(2000)
							



						

				#########################################GAME TURNS LOOP HERE ################################



			#if closing window than quit
			if event.type == pygame.QUIT:
				return False 
#------------------------------------------------------- players -----------------------------
player1 = Classes_objects.get_player('PLAYER1')
dealer = Classes_objects.get_player('DEALER')
table = Classes_objects.get_player('TABLE')
#------------------------------------------------------- Buttons main Screen ---------------------------
start_button = Classes_objects.get_button('START')
instructions_button = Classes_objects.get_button('INSTRUCTIONS')
options_button = Classes_objects.get_button('OPTIONS')
about_button = Classes_objects.get_button('ABOUT')
#--------------------------------------------------------Sound main Screen -----------------------------
button_effect = Sound_effects.get_sound('BUTTON')


######################################################################## MAIN LOOP #############################################
run = True
while run:
	#everything that happens here occures at the game
	#delay time for program 50 milli sec
	pygame.time.delay(50)
	#update view
	pygame.display.update()
	#check whats hapenning on the window
	Menu_page.menu_window(win)#create menu window
	#------------------ check for an event ------------#
	for event in pygame.event.get():
		#get mouse position
		pos = pygame.mouse.get_pos()
		######### check if mouse is over a button and color it ######
		if event.type == pygame.MOUSEMOTION:

			if start_button.is_over(pos):
				start_button.color = (0,0,255)#BLUE
				button_effect.play()
			else:
				start_button.color = (255,0,0) #RED

			if instructions_button.is_over(pos):
				instructions_button.color = (0,0,255)#BLUE
				button_effect.play()
			else:
				instructions_button.color = (255,0,0)#RED

			if options_button.is_over(pos):
				options_button.color = (0,0,255)#BLUE
				button_effect.play()
			else:
				options_button.color = (255,0,0)#RED

			if about_button.is_over(pos):
				about_button.color = (0,0,255)#BLUE
				button_effect.play()
			else:
				about_button.color = (255,0,0)#RED

			#----------------------------------------------#
					#Actual game
		if event.type == pygame.MOUSEBUTTONDOWN:
			if start_button.is_over(pos):
				print('perssed Start game button')
				############################################## set game for play################
				player1.balance = 400
				dealer.balance = 0
				table.balance = 0


				#&&&&&&&&&&&&&&&&&&&&&&&&&&& Main Gameplay here &&&&&&&&&&&&&#
				while player1.balance < 800 and player1.balance > 0:
					player1_bet =  Player_phases.set_bet(win,player1.balance)
					#Get away options
					if player1_bet == 'back':
						break
					elif player1_bet == 'quit':
						run = False
						break
					else:
						player1.balance = player1_bet[1]
						rand_bet = random.randint(2,150)
						dealer.bet(rand_bet)#for the sake of the game EXAMPLE 
						table.win(rand_bet)
						table.win(player1_bet[0])#give money to table
						print('Drawing Player1 cards..')
						player1_card1 = Deck_module.pull_card()
						player1_card2 = Deck_module.pull_card()
						print('Drawing Dealer cards..')
						dealer_card1 = Deck_module.pull_card()
						dealer_card2 = Deck_module.pull_card()
						#player turn
						player1_reasult = Player_phases.player1_turn(win,player1_card1,player1_card2,table.balance,player1.balance,player1.name)
						#Get away options
						if player1_reasult == 'back':
							break
						elif player1_reasult == 'quit':
							run = False
							break
						elif player1_reasult is False:
							#if player 1 lost							
							dealer.win(table.balance)
							Developer_help.write(win,'{} takes {} chips'.format(dealer.name,table.balance),90,50,300)
							table.balance = 0
							pygame.display.update()
							pygame.time.delay(2000)

						elif player1_reasult is True:
							#player 1 black jack
							player1.win(round(table.balance*1.5))
							Developer_help.write(win,'{} takes {} chips'.format(player1.name,round(table.balance*1.5)),90,50,300)
							table.balance = 0
							pygame.display.update()
							pygame.time.delay(2000)
						else:
							dealer_reasult = Dealer_AI.dealer_turn(win,dealer_card1,dealer_card2,table.balance)
							
							if dealer_reasult is False:
								#dealer bust
								player1.win(table.balance)
								Developer_help.write(win,'{} takes {} chips'.format(player1.name,table.balance),90,50,300)
								table.balance = 0
								pygame.display.update()
								pygame.time.delay(2000)
							else:
								#comparison func
								player1.win(Check_reasults.check_game_reasults(win,dealer_reasult,player1_reasult,table.balance,player1_bet[0],player1.name))
								table.balance = 0
						Check_reasults.check_if_won(win,player1.balance,player1.name)
									

							

				#-----------------------------------------------------------
			elif instructions_button.is_over(pos):
				#*************************************** instructions ***********
				print('Instructions Button pressed')
				#&&&&&&&&&&&&&&&&&&&&&&&&&&&7 Instructions &&&&&&&&&&&&&&&&&&
				run = Instructions_page.show_instructions(win)

				#---------------------------------------------------------------
			elif options_button.is_over(pos):
				#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ options ^^^^^^^^^^^^^^^
				print('Options button pressed')

				#------------------------------------------------------------------
			elif about_button.is_over(pos):
				#00000000000000000000000000000000000000000000000000 about 000000000
				print('About button pressed')
				#&&&&&&&&&&&&&&&&&& show page &&&&&&&&&&&&&&&&
				run = About_page.show_about(win)

				#-----------------------------------------------------------------

	#if quit than stop running
	if event.type == pygame.QUIT:
		run = False


