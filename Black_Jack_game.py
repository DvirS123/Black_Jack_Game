#in this file i am going to start the main program in which i am going to build the game
import dealer_AI
import load_card_img
import deck_module
import pygame
import random
import Instructions_page
import About_page
pygame.init()
#initiating pygame
################################################################## SETTINGS ####################################################
#-----------------------images load-----------
image = pygame.image.load(r'C:\Users\97254\Desktop\Python 3\Black_Jack_Project\Black_Jack_sprites\Title.png')
white_chip = pygame.image.load(r'C:\Users\97254\Desktop\Python 3\Black_Jack_Project\Black_Jack_sprites\chips\White.png')
red_chip = pygame.image.load(r'C:\Users\97254\Desktop\Python 3\Black_Jack_Project\Black_Jack_sprites\chips\Red.png')
blue_chip = pygame.image.load(r'C:\Users\97254\Desktop\Python 3\Black_Jack_Project\Black_Jack_sprites\chips\Blue.png')
green_chip = pygame.image.load(r'C:\Users\97254\Desktop\Python 3\Black_Jack_Project\Black_Jack_sprites\chips\Green.png')
black_chip = pygame.image.load(r'C:\Users\97254\Desktop\Python 3\Black_Jack_Project\Black_Jack_sprites\chips\Black.png')
card_back = pygame.image.load(r'C:\Users\97254\Desktop\Python 3\Black_Jack_Project\Black_Jack_sprites\cards\card_back.png')
#---------------------- sound load -------------
pygame.mixer.music.load('Sound_effects\Solar.mp3')
pygame.mixer.music.play(-1)
button_effect = pygame.mixer.Sound('Sound_effects\Metal Click.wav')
draw_effect = pygame.mixer.Sound('Sound_effects\draw.wav')
pass_effect = pygame.mixer.Sound('Sound_effects\Passturn.wav')
won_effect = pygame.mixer.Sound('Sound_effects\end_level.flac')
lose_effect = pygame.mixer.Sound('Sound_effects\lose.wav')
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
class Player():
	def __init__(self,name,start_chip,balance):
		#attributes for a player in the game
		self.name = name
		self.start_chip = start_chip#for the convenience of setting chip amount back to start
		self.balance = balance

		print('Player {} was created succecfully'.format(self.name))
	#so the player can see the name and the balance
	def __str__(self):
		return 'Player playing... {} \n Balance: {}'.format(self.name,self.balance)#will show when one's turn
	#when exiting game allow new players to enter name
	def __del__(self):
		print('player {} deleted'.format(self.name))
	#bet method so the player can bet
	def bet(self,bet_amount):
		if self.balance>= bet_amount:
			self.balance -= bet_amount
			print('bet for {} chips Accepted!\n new balance {}'.format(bet_amount,self.balance))
		else:
			return 'Balance insuficcient please choose an appropriate amount'
	#winning method when u recive chips
	def win(self,win_amount):
		self.balance+=win_amount
		if self.name == 'table':
			print('{} new chips added for bet succecfully!'.format(win_amount))
		else:
			print('{} Won {} chips!'.format(self.name,win_amount))
	#hit method so the player can ask for hit
	def hit(self):
		pass



#create object button
class Button():
	def __init__(self,color,x,y,width,height,text = '',font_size = 30):
		##attributes to define a button
		self.color = color
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.text = text
		self.font_size = font_size
	#now lets create a method to actually draw the button
	def draw(self,win,outline = None):
		#check if outline desired
		if outline:#draw rectangle(at,color ,properties,width line)
			pygame.draw.rect(win,outline,(self.x-2,self.y-2,self.width+4,self.height+4),0)
		#draw the button itself
		pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height),0)
		#check if there is text to fill:
		if self.text!='':
			#set font:(font type, size)
			font = pygame.font.SysFont('comiscans',self.font_size)
			#color font
			text = font.render(self.text, 1, (0,0,0))
			#place the text inside the box properly:(text,(x,y)location tuple)
			win.blit(text,(self.x +(self.width/2 - text.get_width()/2),self.y + (self.height/2 - text.get_height()/2)))
	#check mouse position method
	def is_over(self,pos):
		#pos is set by mouse position(x and y tuple)
		if pos[0] in range(self.x,self.x + self.width + 1) and pos[1] in range(self.y,self.y + self.height + 1):
			return True
		return False
#set a player(self,name,start_chip,balance)
#-----------------------------------------------------------------PLAYERS-------------------------------#
table = Player('table',0,0)
dealer = Player('Dealer',400,0)
player1 = Player('Dvir',400,0)
#for now that is enough
#set a button(self,color,x,y,width,height,text = '',font_size = 30) 
#-------------------------------------------- MENU BUTTONS --------------------------
start_button = Button((255,0,0),275,250,200,75,'Start Game',40)
instructions_button = Button((255,0,0),300,350,150,50,'Instructions',30)
options_button = Button((255,0,0),300,425,150,50,'Options',30)
about_button = Button((255,0,0),300,500,150,50,'About Me',30)
#note: because the back note is a global variable in order to change its color i need to make 
#two buttons and draw each one in diffrent color
#-----------------------------------ALL WINDOWS BUTTONS ---------------------#
red_back_button = Button((255,0,0),20,70,75,50,'Back',20)
blue_back_button = Button((0,0,255),20,70,75,50,'Back',20)
#----------------------------------------------------GAME_SCREENS BUTTONS ------------------------#
red_hit_button = Button((255,0,0),100,475,150,50,'Hit',30)
blue_hit_button = Button((0,0,255),100,475,150,50,'Hit',30)
red_pass_turn_button = Button((255,0,0),300,475,150,50,'End turn',30)
blue_pass_turn_button = Button((0,0,255),300,475,150,50,'End turn',30)
red_bet_approve_button = Button((255,0,0),200,250,100,50,'Approve',30)
blue_bet_approve_button = Button((0,0,255),200,250,100,50,'Approve',30)
red_bet_clear_button = Button((255,0,0),25,250,100,50,'Clear',30)
blue_bet_clear_button = Button((0,0,255),25,250,100,50,'Clear',30)
red_bet_allin_button = Button((255,0,0),112,175,100,50,'All in',30)
blue_bet_allin_button = Button((0,0,255),112,175,100,50,'All in',30)
red_low_ace_button = Button((255,0,0),200,200,100,50,'Ace = 1',30)
blue_low_ace_button = Button((0,0,255),200,200,100,50,'Ace = 1',30)
red_high_ace_button = Button((255,0,0),200,350,100,50,'Ace = 11',30)
blue_high_ace_button = Button((0,0,255),200,350,100,50,'Ace = 11',30)
#--------------------------------------------------------------set a helpfull function-------------------------------------------
def write(text,size,x,y):
	win.blit(((pygame.font.SysFont('comiscans',size)).render(text,1,(0,0,0))),(x,y))
	return 0

def correct_card_value(card):
	'''
	Function takes card and corrects it to the right card value according to the game rules
	'''
	if card[0] in range(11,14):
		return (10,card[1])
	else:
		return card
#----------------------------------------------------------------------defining what is the menu window--------------------------------
def menu_window():
	win.fill((0,150,0))
	#Title
	win.blit(image,(175,125))
	win.blit(((pygame.font.SysFont('comiscans',90)).render('Black', 1, (0,0,0))),(225,50))
	win.blit(((pygame.font.SysFont('comiscans',90)).render('Jack', 1, (0,0,255))),(400,100))
	#------------------------- Make buttons for menu ---------------#
	start_button.draw(win,(0,0,0))
	instructions_button.draw(win,(0,0,0))
	options_button.draw(win,(0,0,0))
	about_button.draw(win,(0,0,0))
#------------------------------------------------------------define the bet at the start of a turn------------------------------------
def set_bet(balance):
	reset_balance = balance
	win.fill((0,150,0))
	win.blit(card_back,(350,350))
	win.blit(card_back,(450,350))
	amount = 0
	while True:
		pygame.draw.rect(win,(100,150,0),(520,40,200,100),0)#to reset the board
		write('Balance: {}'.format(balance),30,550,50)
		write('bet amount: {}'.format(amount),30,550,100)
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
				if red_back_button.is_over(pos):
					blue_back_button.draw(win,(0,0,0))
				else:
					red_back_button.draw(win,(0,0,0))
				if red_bet_approve_button.is_over(pos):
					blue_bet_approve_button.draw(win,(0,0,0))
				else:
					red_bet_approve_button.draw(win,(0,0,0))
				if red_bet_clear_button.is_over(pos):
					blue_bet_clear_button.draw(win,(0,0,0))
				else:
					red_bet_clear_button.draw(win,(0,0,0))
				if red_bet_allin_button.is_over(pos):
					blue_bet_allin_button.draw(win,(0,0,0))
				else:
					red_bet_allin_button.draw(win,(0,0,0))


			if event.type == pygame.MOUSEBUTTONDOWN:
				if red_back_button.is_over(pos):
					return 'back'#keyword to signal the outer function game screen
				#Buttons for raising the bet
				#White
				if pos[0] in range(40,110) and pos[1] in range(350,420) and balance >=1:
					balance-=1
					amount+=1
				#Red
				if pos[0] in range(115,185) and pos[1] in range(350,420) and balance >=5:
					balance-=5
					amount+=5
				#Blue
				if pos[0] in range(190,260) and pos[1] in range(350,420) and balance >=10:
					balance-=10
					amount+=10
				#Green
				if pos[0] in range(75,145) and pos[1] in range(425,495) and balance >=25:
					balance-=25
					amount+=25
				#Black
				if pos[0] in range(150,220) and pos[1] in range(425,495) and balance >= 100:
					balance-=100
					amount+=100


				if red_bet_allin_button.is_over(pos):
					amount += balance
					balance = 0
				if red_bet_clear_button.is_over(pos):#clears bet amount and reset balance
					amount = 0
					balance = reset_balance
				if red_bet_approve_button.is_over(pos):
					return amount

							

			if event.type == pygame.QUIT:
				return 'quit'

#------------------------------------------------------------------defining what is going on the game screen----------------------------------------
def game_screen():
	#------------------------settings--------------#
	win.fill((0,150,0))
	#used_cards = []#cards that were already played cannot show again that is why cards will accumulate here as game keeps going
	#----------------------------------------------------PULL RAND FUNCTION------------------------------
	def pull_card():
		'''
		Checks if a card was burnt
		and makes sure circulation occurs after a deck is done
		'''
		global used_cards#declare as global variable
		pulled_card = deck_module.deck_for_game()
		while pulled_card in used_cards:#all the cards
			pulled_card = deck_module.deck_for_game()#set new card
			if len(used_cards) == 51:
				#if all cards were used
				print('All cards were burned , reseting deck now')
				used_cards = []
				pulled_card = deck_module.deck_for_game()
				break
				#break from while loop to return card
		used_cards.append(pulled_card)
		return pulled_card
	#------------------------------------------------------Check action reasult -------------------------------
	def check_cards_sum(card1 , card2 = 0, cards_sum = 0):
		'''
		After a hit or at the start of a turn checks the situation of the player
		'''
		new_cards_sum = cards_sum + card1 + card2
		if new_cards_sum == 21:#if won
			# if 21 first turn return stand which is true
			print('21!, Stand')
			pygame.time.delay(3000)
			return True
		elif new_cards_sum > 21 :
			print('BUST')
			pygame.time.delay(3000)
			return False
		else:
			return new_cards_sum
	#-------------------------------------------------------Dealer turn-------------------------------------------------
	def dealer_turn(dealer_card1,dealer_card2,at_table):
		'''
		Because I need to create an AI player i will use a lot the random module
		takes in 2 card parameters and almost no user interface
		'''
		card1_image = pygame.image.load(load_card_img.get_card_image(dealer_card1))
		card2_image = pygame.image.load(load_card_img.get_card_image(dealer_card2))
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
		print('{} it is your turn \nchip balance:{}'.format(dealer.name,dealer.balance))
		######### correct the value
		dealer_card1 = correct_card_value(dealer_card1)
		dealer_card2 = correct_card_value(dealer_card2)
		cards_sum = check_cards_sum(dealer_card1[0],dealer_card2[0])
		#i there is an ace let him decide
		if dealer_card1[0] == 1 or dealer_card2[0] == 1:
			if dealer_AI.ace_ans(cards_sum) is True:
				cards_sum+=10
		dealer_turn = True
		while dealer_turn:
			pygame.time.delay(1000)
			dealer_turn = dealer_AI.hit_answer_rules(cards_sum)
			if dealer_turn is True:
				draw_effect.play()
				new_card = pull_card()
				card_x+=40
				card_y+=40
				#post card image changes cordination so new posting could be shown
				new_card_image = pygame.image.load(load_card_img.get_card_image(new_card))
				win.blit(new_card_image,(card_x,card_y))
				pygame.display.update()
				pygame.time.delay(1000)
				if new_card[0] == 1:
					if dealer_AI.ace_ans(cards_sum):
						value_new_card = (11,'')#to save the same data type
					else:
						value_new_card = (1,'')
				value_new_card = correct_card_value(new_card)
				cards_sum = check_cards_sum(value_new_card[0],cards_sum)
				#so the function would stop and wont let the game continue
				if cards_sum is False:
					write('BUST',90,200,250)
					pygame.display.update()
					pygame.time.delay(2000)
					return cards_sum
				elif cards_sum is True:
					write('21 Stand!',90,200,250)
					pygame.display.update()
					pygame.time.delay(2000)
					return cards_sum
			else:
				pass_effect.play()
				print('Dealer has ended his turn with sum of {}'.format(cards_sum))
				write('Stand',90,200,250)
				pygame.display.update()
				pygame.time.delay(2000)
				return cards_sum


		#if came out first bust or 21 without hit
		if cards_sum is False:
			#so the user can see the cards first
			pygame.display.update()
			pygame.time.delay(1000)
			write('BUST',90,200,250)
			pygame.display.update()
			pygame.time.delay(2000)
			return cards_sum
		elif cards_sum is True:
			#so the user can see the cards first
			pygame.display.update()
			pygame.time.delay(1000)
			write('21 Stand!',90,200,250)
			pygame.display.update()
			pygame.time.delay(2000)
			return cards_sum

	#---------------------------------------------------- player1 turn function -------------------------------------------
	def player1_turn(player1_card1,player1_card2,at_table):
		'''
		Dictates what a players turn should be like
		takes in (card1,card2,amount at table)
		'''
		#options to bet via function set_bet
		global is_natural
		is_ace = False
		is_natural = True
		if player1_card1[0] == 1 or player1_card2[0] == 1 :
			is_ace = True 
		card1_image = pygame.image.load(load_card_img.get_card_image(player1_card1))
		card2_image = pygame.image.load(load_card_img.get_card_image(player1_card2))
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
		print('{} it is your turn \nchip balance:{}'.format(player1.name,player1.balance))
		#################################turn j,q,k cards to value 10##################
		player1_card1 = correct_card_value(player1_card1)
		player1_card2 =  correct_card_value(player1_card2)
		cards_sum = check_cards_sum(player1_card1[0],player1_card2[0])
		while cards_sum < 21:
			#----------------------------------Turn-------------------------------#
			pygame.draw.rect(win,(100,150,0),(470,40,300,100),0)#to reset the board
			write("{}'s Balance: {}".format(player1.name,player1.balance),30,500,50)
			write('Overall bet amount: {}'.format(at_table),30,500,100)
			pygame.time.delay(50)
			pygame.display.update()
			for event in pygame.event.get():
				pos = pygame.mouse.get_pos()
				###############################################if mouse moves
				if event.type == pygame.MOUSEMOTION:
					if red_back_button.is_over(pos):
						blue_back_button.draw(win,(0,0,0))
					else:
						red_back_button.draw(win,(0,0,0))
					if red_pass_turn_button.is_over(pos):
						blue_pass_turn_button.draw(win,(0,0,0))
					else:
						red_pass_turn_button.draw(win,(0,0,0))
					if red_hit_button.is_over(pos):
						blue_hit_button.draw(win,(0,0,0))
					else:
						red_hit_button.draw(win,(0,0,0))
					if is_ace:
						if red_low_ace_button.is_over(pos):
							blue_low_ace_button.draw(win,(0,0,0))
						else:
							red_low_ace_button.draw(win,(0,0,0))
						if red_high_ace_button.is_over(pos):
							blue_high_ace_button.draw(win,(0,0,0))
						else:
							red_high_ace_button.draw(win,(0,0,0))
					else:#To erase the buttons
						pygame.draw.rect(win,(0,150,0),(190,190,120,220),0)

							
						#####################################################if mouse clicks
				if event.type == pygame.MOUSEBUTTONDOWN:
					if red_back_button.is_over(pos):
						return 'back'
					if red_pass_turn_button.is_over(pos):
						pass_effect.play()
						print('Player {} has ended his turn with sum of {}'.format(player1.name,cards_sum))
						write('Stand',90,200,250)
						pygame.display.update()
						pygame.time.delay(2000)
						return cards_sum
					if red_hit_button.is_over(pos):
						draw_effect.play()
						is_natural = False
						new_card = pull_card()
						card_x+=40
						card_y+=40
						#post card image changes cordination so new posting could be shown
						new_card_image = pygame.image.load(load_card_img.get_card_image(new_card))
						win.blit(new_card_image,(card_x,card_y))
						pygame.display.update()
						pygame.time.delay(1000)
						##################change j,q,k values to 10
						new_card = correct_card_value(new_card)
						if new_card[0] == 1:
							is_ace = True
						else:
							is_ace = False
						cards_sum = check_cards_sum(new_card[0],cards_sum)
						#so the function would stop and wont let the game continue
					if red_low_ace_button.is_over(pos):
						is_ace = False
					if red_high_ace_button.is_over(pos):
						cards_sum+=10
						is_ace = False
				if cards_sum is False:
					write('BUST',90,200,250)
					pygame.display.update()
					pygame.time.delay(2000)
					return cards_sum
				#if won natural
				if cards_sum == 21 and is_natural:
					write('Black Jack!',90,200,250)
					pygame.display.update()
					pygame.time.delay(2000)
					return cards_sum
				#if won non natural
				elif cards_sum is True:
					write('21, Stand!',90,200,250)
					pygame.display.update()
					pygame.time.delay(2000)
					return cards_sum

				if event.type == pygame.QUIT:
					return 'quit'
					#if came out first bust or 21 without hit
			if cards_sum is False:
				#so the user can see the cards first
				pygame.display.update()
				pygame.time.delay(1000)
				write('BUST',90,200,250)
				pygame.display.update()
				pygame.time.delay(2000)
				return cards_sum
			elif cards_sum is True or cards_sum == 21:
				#so the user can see the cards first
				pygame.display.update()
				pygame.time.delay(1000)
				write('21 Stand!',90,200,250)
				pygame.display.update()
				pygame.time.delay(2000)
				return cards_sum



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
					write('{} Has lost'.format(player1.name),90,200,100)
					pygame.display.update()
					lose_effect.play()
					pygame.time.delay(3000)
					return True
				elif player1.balance >= 800:
					write('{} Has won , Congrats!'.format(player1.name),90,50,100)
					pygame.display.update()
					won_effect.play()
					pygame.time.delay(3000)
					return True
				#first pull cards
				print('Drawing Player1 cards..')
				player1_card1 = pull_card()
				player1_card2 = pull_card()
				print('Drawing Dealer cards..')
				dealer_card1 = pull_card()
				dealer_card2 = pull_card()
				######################################################################
				if True:
					player1_bet = set_bet(player1.balance)
					if player1_bet == 'back':
						return True
					elif player1_bet == 'quit':
						return False
					rand_bet = random.randint(2,150)
					dealer.bet(rand_bet)#for the sake of the game EXAMPLE 
					player1.bet(player1_bet)#lose the bet money
					table.win(rand_bet)
					table.win(player1_bet)#give money to table
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

							elif is_dealer_turn == player_turn:
								#tie
								print('Its a TIE')
								#if its a tie than cut the vet to half and give one more chip to dealer
								player1.win(player1_bet)
								#splittig chips
								table.balance=0
								write('Tie',90,250,300)
								pygame.display.update()
								pygame.time.delay(1000)

								#if player 1 lost
							elif is_dealer_turn > player_turn or is_dealer_turn is True:
								dealer.win(table.balance)
								write('{} takes {} chips'.format(dealer.name,table.balance),90,50,300)
								table.balance = 0
								pygame.display.update()
								pygame.time.delay(2000)


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


######################################################################## MAIN LOOP #############################################
run = True
hasnt_played = True
while run:
	#everything that happens here occures at the game
	#delay time for program 50 milli sec
	pygame.time.delay(50)
	#update view
	pygame.display.update()
	#check whats hapenning on the window
	menu_window()#create menu window
	#------------------ check for an event ------------#
	for event in pygame.event.get():
		#get mouse position
		pos = pygame.mouse.get_pos()
		######### check if mouse is over a button and color it ######
		if event.type == pygame.MOUSEMOTION:
			if start_button.is_over(pos):
				start_button.color = (0,0,255)#BLUE
				if hasnt_played is True:
					hasnt_played = False
					button_effect.play()
					
			else:
				start_button.color = (255,0,0) #RED
				hasnt_played = True
			if instructions_button.is_over(pos):
				instructions_button.color = (0,0,255)#BLUE
				if hasnt_played:
					button_effect.play()
					hasnt_played = False
			else:
				instructions_button.color = (255,0,0)#RED
				hasnt_played = True
			if options_button.is_over(pos):
				options_button.color = (0,0,255)#BLUE
				if hasnt_played:
					button_effect.play()
					hasnt_played = False
			else:
				options_button.color = (255,0,0)#RED
				hasnt_played = True
			if about_button.is_over(pos):
				about_button.color = (0,0,255)#BLUE
				if hasnt_played:
					button_effect.play()
					hasnt_played = False
			else:
				about_button.color = (255,0,0)#RED
				hasnt_played = True
			#----------------------------------------------#
			######check if mouse clickes on a button####
		if event.type == pygame.MOUSEBUTTONDOWN:
			if start_button.is_over(pos):
				print('perssed Start game button')
				#&&&&&&&&&&&&&&&&&&&&&&&&&&& Main Gameplay here &&&&&&&&&&&&&#
				run = game_screen()

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


