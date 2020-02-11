#in this file we are going to start the main program i which we are going to build the game
import pygame
pygame.init()
################################################################## SETTINGS ####################################################
#initiating pygame
#Creating a window
win = pygame.display.set_mode((750,600))
# color fill green
win.fill((0,150,0))
#naming game
pygame.display.set_caption('Black Jack game by Dvir Shiri')

#create obect button
class Button():
	#
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
#set a button(self,color,x,y,width,height,text = '',font_size = 30)
start_button = Button((255,0,0),275,250,200,75,'Start Game',40)
instructions_button = Button((255,0,0),300,350,150,50,'Instructions',30)
options_button = Button((255,0,0),300,425,150,50,'Options',30)
about_button = Button((255,0,0),300,500,150,50,'About Me',30)
#defining what is the menu window
def menu_window():
	win.fill((0,150,0))
	#Title
	win.blit(((pygame.font.SysFont('comiscans',90)).render('Black', 1, (0,0,0))),(225,50))
	win.blit(((pygame.font.SysFont('comiscans',90)).render('Jack', 1, (0,0,255))),(400,100))
	#------------------------- Make buttons for menu ---------------#
	start_button.draw(win,(0,0,0))
	instructions_button.draw(win,(0,0,0))
	options_button.draw(win,(0,0,0))
	about_button.draw(win,(0,0,0))


######################################################################## MAIN LOOP #############################################
run = True
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

		#if quit than stop running
		if event.type == pygame.QUIT:
			run = False
	'''
	First we are going to a make a 'start' button
	'''

