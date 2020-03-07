import pygame
import Classes_objects
import Developer_help
import Load_image
import Sound_effects
import Check_reasults
import Deck_module
import Speical_moves



#-------------------------------------------------------- load data -----------------------------
#----------------------------------------------------players --------------------------------
player1 = Classes_objects.get_player('PLAYER1')
dealer = Classes_objects.get_player('DEALER')
table = Classes_objects.get_player('TABLE')
#--------------------------------------------------images----------------------
card_back = Load_image.get_game_img('CARD_BACK')
white_chip =Load_image.get_game_img('WHITE_CHIP')
red_chip =Load_image.get_game_img('RED_CHIP')
blue_chip =Load_image.get_game_img('BLUE_CHIP')
green_chip =Load_image.get_game_img('GREEN_CHIP')
black_chip =Load_image.get_game_img('BLACK_CHIP')

#--------------------------------------------------buttons---------------------
back_button = Classes_objects.get_button('BACK')
bet_allin_button = Classes_objects.get_button('ALL_IN')
bet_approve_button = Classes_objects.get_button('APPROVE')
bet_clear_button = Classes_objects.get_button('CLEAR')
split_button = Classes_objects.get_button('SPLIT')
#------------------------------------------------------sound------------------------------------------
button_effect = Sound_effects.get_sound('BUTTON')
chip_effect = Sound_effects.get_sound('CHIP')

def set_bet(win,balance):

	'''
	#------------------------------------------------------------define the bet at the start of a turn------------------------------------
	'''

	win.fill((0,150,0))
	win.blit(card_back,(350,350))
	win.blit(card_back,(450,350))
	reset_balance = balance
	amount = 0
	while True:
		back_button.draw(win,(0,0,0))
		bet_allin_button.draw(win,(0,0,0))
		bet_approve_button.draw(win,(0,0,0))
		bet_clear_button.draw(win,(0,0,0))
		win.blit(white_chip,(40,350))
		win.blit(red_chip,(115,350))
		win.blit(blue_chip,(190,350))
		win.blit(green_chip,(75,425))
		win.blit(black_chip,(150,425))


		pygame.draw.rect(win,(100,150,0),(520,40,200,100),0)#to reset the board
		Developer_help.write(win,'Balance: {}'.format(balance),30,550,50)
		Developer_help.write(win,'bet amount: {}'.format(amount),30,550,100)

		pygame.time.delay(50)
		pygame.display.update()

		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()
			if event.type == pygame.MOUSEMOTION:
				#------------------------------------------------------------chips------------------------------------------------------
				if balance >=1:
				#WHITE
					if pos[0] in range(40,110) and pos[1] in range(350,420):
						#HIGHLIGHT THE CHIPS
						pygame.draw.circle(win,(0,0,0),(75,385),37)
						win.blit(white_chip,(40,350))
					else:
						pygame.draw.circle(win,(0,150,0),(75,385),37)
						win.blit(white_chip,(40,350))
				if balance >=5:
					#RED
					if pos[0] in range(115,185) and pos[1] in range(350,420):
						#HIGHLIGHT THE CHIPS
						pygame.draw.circle(win,(0,0,0),(150,385),37)
						win.blit(red_chip,(115,350))
					else:
						pygame.draw.circle(win,(0,150,0),(150,385),37)
						win.blit(red_chip,(115,350))
				if balance >=10:
						#BLUE
					if pos[0] in range(190,260) and pos[1] in range(350,420):
						#HIGHLIGHT THE CHIPS
						pygame.draw.circle(win,(0,0,0),(225,385),37)
						win.blit(blue_chip,(190,350))
					else:
						pygame.draw.circle(win,(0,150,0),(225,385),37)
						win.blit(blue_chip,(190,350))
				if balance >=25:
					#GREEN
					if pos[0] in range(75,145) and pos[1] in range(425,495):
						#HIGHLIGHT THE CHIPS
						pygame.draw.circle(win,(0,0,0),(110,460),37)
						win.blit(green_chip,(75,425))
					else:
						pygame.draw.circle(win,(0,150,0),(110,460),37)
						win.blit(green_chip,(75,425))
				if balance >= 100:
					#BLACK
					if pos[0] in range(150,220) and pos[1] in range(425,495):
						#HIGHLIGHT THE CHIPS
						pygame.draw.circle(win,(0,0,0),(185,460),37)
						win.blit(black_chip,(150,425))
					else:
						pygame.draw.circle(win,(0,150,0),(185,460),37)
						win.blit(black_chip,(150,425))
				#----------------------------------------------------------------------buttons------------------------------------
				if back_button.is_over(pos):
					back_button.color = (0,0,255)
				else:
					back_button.color = (255,0,0)

				if bet_approve_button.is_over(pos):
					bet_approve_button.color = (0,0,255)
				else:
					bet_approve_button.color = (255,0,0)

				if bet_clear_button.is_over(pos):
					bet_clear_button.color = (0,0,255)
				else:
					bet_clear_button.color = (255,0,0)

				if bet_allin_button.is_over(pos):
					bet_allin_button.color = (0,0,255)
				else:
					bet_allin_button.color = (255,0,0)


			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.is_over(pos):
					button_effect.play()
					return 'back'#keyword to signal the outer function game screen
				#Buttons for raising the bet
				#White
				if pos[0] in range(40,110) and pos[1] in range(350,420) and balance >=1:
					chip_effect.play()
					balance-=1
					amount+=1
				#Red
				if pos[0] in range(115,185) and pos[1] in range(350,420) and balance >=5:
					chip_effect.play()
					balance-=5
					amount+=5
				#Blue
				if pos[0] in range(190,260) and pos[1] in range(350,420) and balance >=10:
					chip_effect.play()
					balance-=10
					amount+=10
				#Green
				if pos[0] in range(75,145) and pos[1] in range(425,495) and balance >=25:
					chip_effect.play()
					balance-=25
					amount+=25
				#Black
				if pos[0] in range(150,220) and pos[1] in range(425,495) and balance >= 100:
					chip_effect.play()
					balance-=100
					amount+=100


				if bet_allin_button.is_over(pos):
					button_effect.play()
					amount += balance
					balance = 0
				if bet_clear_button.is_over(pos):#clears bet amount and reset balance
					button_effect.play()
					amount = 0
					balance = reset_balance
				if bet_approve_button.is_over(pos):
					#check bet limit
					if amount <2 or amount > 500:
						Developer_help.write(win,'Limit is between 2 and 500 $',30,175,100)
					else:
						button_effect.play()
						return amount,balance

							

			if event.type == pygame.QUIT:
				print('Exiting')
				return 'quit'







	#---------------------------------------------------- player1 turn function -------------------------------------------
def player1_turn(win,player1_card1,player1_card2,at_table,player1_balance,player1_name,player1_bet):
	'''
	Dictates what a players turn should be like
	takes in (card1,card2,amount at table)
	'''
	#options to bet via function set_bet
	#------------------------------------------------------------ LOAD DATA -----------------------
	#------------------------------------------------------------ buttons -------------------------
	pass_turn_button = Classes_objects.get_button('PASS_TURN')
	hit_button = Classes_objects.get_button('HIT')
	back_button = Classes_objects.get_button('BACK')
	low_ace_button = Classes_objects.get_button('LOW_ACE')
	high_ace_button = Classes_objects.get_button('HIGH_ACE')
	split_button = Classes_objects.get_button('SPLIT')
	double_down_button = Classes_objects.get_button('DOUBLE_DOWN')
	#------------------------------------------------------------- sound --------------------------
	draw_effect = Sound_effects.get_sound('DRAW')
	pass_effect = Sound_effects.get_sound('PASS')
	button_effect = Sound_effects.get_sound('BUTTON')

	is_double_down = False
	is_split = False
	is_ace = False
	is_natural = True
	if player1_card1[0] == 1 or player1_card2[0] == 1 :
		is_ace = True 
	card1_image = pygame.image.load(Load_image.get_card_image(player1_card1))
	card2_image = pygame.image.load(Load_image.get_card_image(player1_card2))
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
	print('{} it is your turn \nchip balance:{}'.format(player1_name,player1_balance))
	#### check if split ###
	split = False
	if player1_card1[0] == player1_card2[0]:
		is_split = True
	#################################turn j,q,k cards to value 10##################
	player1_card1 = Developer_help.correct_card_value(player1_card1)
	player1_card2 =  Developer_help.correct_card_value(player1_card2)
	cards_sum = Check_reasults.check_cards_sum(win,is_natural,player1_card1[0],player1_card2[0])
	if cards_sum in range(9,12):
		is_double_down = True
	cards_used = [player1_card1,player1_card2]
	while cards_sum < 21:

		pass_turn_button.draw(win,(0,0,0))
		hit_button.draw(win,(0,0,0))
		back_button.draw(win,(0,0,0))
		if split is False:
			low_ace_button.x = 200
			high_ace_button.x = 200

		#----------------------------------Turn-------------------------------#
		pygame.draw.rect(win,(100,150,0),(470,40,300,100),0)#to reset the board
		Developer_help.write(win,"{}'s Balance: {}".format(player1_name,player1_balance),30,500,50)
		Developer_help.write(win,'Overall bet amount: {}'.format(at_table),30,500,100)
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

				#---------------------------------- Speical buttons --------------------------

				if is_double_down:
					double_down_button.draw(win,(0,0,0))
					if double_down_button.is_over(pos):
						double_down_button.color = (0,0,255)
					else:
						double_down_button.color = (255,0,0)

				if is_split:
					split_button.draw(win,(0,0,0))
					if split_button.is_over(pos):
						split_button.color = (0,0,255)
					else:
						split_button.color = (255,0,0)

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
					if split:
						cards_sum = [hand1,cards_sum]
					pass_effect.play()
					is_split = False
					print('Player {} has ended his turn with sum of {}'.format(player1_name,cards_sum))
					Developer_help.write(win,'Stand',90,200,100)
					pygame.display.update()
					pygame.time.delay(2000)
					return cards_sum
				if hit_button.is_over(pos):
					draw_effect.play()
					if split:
						pygame.draw.rect(win,(0,150,0),(40,190,120,275),0)#scrap button
					else:
						pygame.draw.rect(win,(0,150,0),(190,190,120,275),0)#scrap button
					is_split = False
					is_natural = False
					new_card = Deck_module.pull_card()#pull card
					cards_used.append(new_card)
					card_x+=40
					card_y+=40
					#post card image changes cordination so new posting could be shown
					new_card_image = pygame.image.load(Load_image.get_card_image(new_card))
					win.blit(new_card_image,(card_x,card_y))
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
						if split:
							return hand1
						else:
							return False
					elif cards_sum is True:
						return True
					#so the function would stop and wont let the game continue
				if low_ace_button.is_over(pos):
					button_effect.play()
					is_ace = False
					if split:
						pygame.draw.rect(win,(0,150,0),(40,190,120,275),0)#scrap button
					else:
						pygame.draw.rect(win,(0,150,0),(190,190,120,275),0)#scrap button
				if high_ace_button.is_over(pos):
					button_effect.play()
					is_ace = False
					if split:
						pygame.draw.rect(win,(0,150,0),(40,190,120,275),0)#scrap button
					else:
						pygame.draw.rect(win,(0,150,0),(190,190,120,275),0)#scrap button
					cards_sum = Check_reasults.check_cards_sum(win,is_natural,10,cards_sum)
					if cards_sum is True:
						return True
					elif cards_sum is False:
						return False
				if is_split is True:
					if split_button.is_over(pos):
						is_split = False
						is_double_down = False
						table.win(player1_bet)
						player1.bet(player1_bet)
						player1_balance = player1.balance
						at_table = table.balance
						pygame.draw.rect(win,(100,150,0),(470,40,300,100),0)#to reset the board
						pygame.draw.rect(win,(0,150,0),(40,190,150,275),0)#scrap button
						Developer_help.write(win,"{}'s Balance: {}".format(player1_name,player1_balance),30,500,50)
						Developer_help.write(win,'Overall bet amount: {}'.format(at_table),30,500,100)
						pygame.display.update()
						pygame.time.delay(50)
						hand1 = Speical_moves.split(win,player1_card1,player1_card2,player1_name)
						if hand1 == 'back':
							return 'back'
						elif hand1 == 'quit':
							return 'quit'
						cards_sum = player1_card1[0]
						#that a split has happened
						split = True
						card_x-=40
						card_y-=40
				if is_double_down and double_down_button.is_over(pos):
					if player1_balance >= player1_bet:
						is_double_down = False
						table.win(player1_bet)
						at_table += player1_bet
						player1.bet(player1_bet)
						player1_balance-= player1_bet
						pygame.draw.rect(win,(0,150,0),(40,190,150,275),0)#scrap button
						pygame.draw.rect(win,(0,150,0),(190,190,120,275),0)#scrap button
					else:
						Developer_help.write(win,'There are not enough chips for that',30,150,100)

			if event.type == pygame.QUIT:
				return 'quit'
	#returns 21 if value is equal to 21!
	return cards_sum
