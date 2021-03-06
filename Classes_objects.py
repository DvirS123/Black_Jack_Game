import pygame


class Player():
	'''
	Create player object
	self,name,start_chip,balance
	'''
	def __init__(self,name,balance):
		#attributes for a player in the game
		self.name = name
		self.balance = balance
	#bet method so the player can bet
	def bet(self,bet_amount):
		if self.balance>= bet_amount:
			self.balance -= bet_amount
	#winning method when u recive chips
	def win(self,win_amount):
		self.balance+=win_amount
	#hit method so the player can ask for hit
	
#-----------------------------------------------------------------PLAYERS-------------------------------#
table = Player('table',0)
dealer = Player('Dealer',400)
player1 = Player('Player1',400)

def get_player(name):
	if name == 'PLAYER1':
		return player1
	elif name == 'DEALER':
		return dealer
	elif name == 'TABLE':
		return table


class Button():
	'''
	Create object button
	(self,color,x,y,width,height,text = '',font_size = 30):
	'''
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
			font = pygame.font.Font('Fonts/BadaboomBB_Reg.ttf',self.font_size)
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

#-------------------------------------------- MENU BUTTONS --------------------------
start_button = Button((255,0,0),275,250,200,75,'Start Game',40)
instructions_button = Button((255,0,0),300,350,150,50,'Instructions',30)
options_button = Button((255,0,0),300,425,150,50,'Options',30)
about_button = Button((255,0,0),300,500,150,50,'About Me',30)
#-----------------------------------ALL WINDOWS BUTTONS ---------------------#
back_button = Button((255,0,0),20,70,75,50,'Back',20)
#----------------------------------------------------GAME_SCREENS BUTTONS ------------------------#
hit_button = Button((255,0,0),100,475,150,50,'Hit',30)
pass_turn_button = Button((255,0,0),300,475,150,50,'End turn',30)
bet_approve_button = Button((255,0,0),200,250,100,50,'Approve',30)
bet_clear_button = Button((255,0,0),25,250,100,50,'Clear',30)
bet_allin_button = Button((255,0,0),112,175,100,50,'All in',30)
low_ace_button = Button((255,0,0),200,200,100,50,'Ace = 1',30)
high_ace_button = Button((255,0,0),200,400,100,50,'Ace = 11',30)
split_button = Button((255,0,0),225,275,150,100,'Split',30)
double_down_button = Button((255,0,0),50,275,150,100,'Double Down',30)
text_box = Button((0,0,0),250,245,200,50,'',10)
vol_bar0 = Button((255,0,0),75,425,50,50,'0',30)
vol_bar1 = Button((255,0,0),125,425,50,50,'1',30)
vol_bar2 = Button((255,0,0),175,425,50,50,'2',30)
vol_bar3 = Button((255,0,0),225,425,50,50,'3',30)
vol_bar4 = Button((255,0,0),275,425,50,50,'4',30)
vol_bar5 = Button((255,0,0),325,425,50,50,'5',30)
vol_bar6 = Button((255,0,0),375,425,50,50,'6',30)
vol_bar7 = Button((255,0,0),425,425,50,50,'7',30)
vol_bar8 = Button((255,0,0),475,425,50,50,'8',30)
vol_bar9 = Button((255,0,0),525,425,50,50,'9',30)
vol_bar10 = Button((255,0,0),575,425,50,50,'10',30)

def get_button(name):
	if name == 'START':
		return start_button
	elif name == 'INSTRUCTIONS':
		return instructions_button
	elif name == 'OPTIONS':
		return options_button
	elif name == 'ABOUT':
		return about_button
	elif name == 'BACK':
		return back_button
	elif name == 'HIT':
		return hit_button
	elif name == 'PASS_TURN':
		return pass_turn_button
	elif name == 'APPROVE':
		return bet_approve_button
	elif name == 'CLEAR':
		return bet_clear_button
	elif name == 'ALL_IN':
		return bet_allin_button
	elif name == 'LOW_ACE':
		return low_ace_button
	elif name == 'HIGH_ACE':
		return high_ace_button
	elif name == 'SPLIT':
		return split_button
	elif name == 'DOUBLE_DOWN':
		return double_down_button
	elif name == 'TEXT_BOX':
		return text_box
	elif name == 'VOL0':
		return vol_bar0
	elif name == 'VOL1':
		return vol_bar1
	elif name == 'VOL2':
		return vol_bar2
	elif name == 'VOL3':
		return vol_bar3
	elif name == 'VOL4':
		return vol_bar4
	elif name == 'VOL5':
		return vol_bar5
	elif name == 'VOL6':
		return vol_bar6
	elif name == 'VOL7':
		return vol_bar7
	elif name == 'VOL8':
		return vol_bar8
	elif name == 'VOL9':
		return vol_bar9
	elif name == 'VOL10':
		return vol_bar10



