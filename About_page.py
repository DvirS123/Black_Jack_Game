import pygame


#This page was ment to show about

def show_about(win):
	'''
	Page to show instructions about the game
	'''
	def write(text,size,x,y):
		win.blit(((pygame.font.SysFont('comiscans',size)).render(text,1,(0,0,0))),(x,y))
		return 0
	line1 = " - soon to be built by Dvir Shiri"
	line2 = " - fix logo "
	line3 = " - create options page"
	line4 = " - offer option to mute in options page"
	line5 = " - add more sound effects and songs to background"
	line6 = " - offer option to change name in options"
	line7 = " - save progress and game?"
	win.fill((0,150,0))
	pygame.draw.rect(win,(0,0,0),(18,68,79,54),0)#Outlining
	write(line1,25,25,150)
	write(line2,25,25,175)
	write(line3,25,25,200)
	write(line4,25,25,225)
	write(line5,25,25,250)
	write(line6,25,25,275)
	write(line7,25,25,300)
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
