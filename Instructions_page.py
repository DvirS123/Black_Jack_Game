import pygame


#This page was ment to show instructions

def show_instructions(win):
	def write(text,size,x,y):
		win.blit(((pygame.font.SysFont('comiscans',size)).render(text,1,(0,0,0))),(x,y))
		return 0
	'''
	Page to show instructions about the game
	'''
	rule1 = " - The goal of blackjack is to beat the dealer's hand without going over 21."
	rule2 = " - Face cards are worth 10..."
	rule3 = " - Each player starts with two cards, one of the dealer's cards is hidden until the end."
	rule4 = " - To 'Hit' is to ask for another card. ..."
	rule5 = " - If you go over 21 you bust, and the dealer wins regardless of the dealer's hand."
	rule6 = " - In order to win the game you must aquire a balance of 800 chips"
	rule7 = " - If you reach a balance of 0 you lose"

	win.fill((0,150,0))
	pygame.draw.rect(win,(0,0,0),(18,68,79,54),0)#Outlining
	write(rule1,25,25,200)
	write(rule2,25,25,250)
	write(rule3,25,25,300)
	write(rule4,25,25,350)
	write(rule5,25,25,400)
	write(rule6,25,25,450)
	write(rule7,25,25,500)
	write('Good Luck!',50,275,550)
	while True:
		pygame.time.delay(50)
		pygame.display.update()
		#screen support

		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()
			#get mouse position
			if event.type == pygame.MOUSEMOTION:
				if pos[0] in range(20,95) and pos[1] in range(70,120):#in range of 'back' button
					pygame.draw.rect(win,(0,0,255),(20,70,75,50),0)
					write('Back',20,42,90)
				else:
					pygame.draw.rect(win,(255,0,0),(20,70,75,50),0)
					write('Back',20,42,90)
			pygame.display.update()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if pos[0] in range(20,95) and pos[1] in range(70,120):#in range of 'back' button
					return True
			if event.type == pygame.QUIT:
				return False
