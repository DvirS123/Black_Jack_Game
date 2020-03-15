import pygame
import Sound_effects
import Classes_objects
from Developer_help import write

button_effect = Sound_effects.get_sound('BUTTON')
back_button = Classes_objects.get_button('BACK')


#This page was ment to show about 1

def show_about(win):
	'''
	Page to show instructions about the game
	'''
	line1 = " - made by Dvir Shiri"
	line2 = " - Hi, my name is dvir and i am new to python and programing "
	line3 = " - I made tis game in order to practice my abillities at python"
	line4 = " - This is one of many projects i am creating"
	line5 = " - If you are intrested in more projects check my website at:@web address@"
	line6 = " - or enter here: @link to web@"
	line7 = " - If you have comments about the projects please contact me:@mail address link@"
	line8 = "Thank you!"
	win.fill((0,150,0))
	pygame.draw.rect(win,(0,0,0),(18,68,79,54),0)#Outlining
	write(win,line1,25,25,150)
	write(win,line2,25,25,175)
	write(win,line3,25,25,200)
	write(win,line4,25,25,225)
	write(win,line5,25,25,250)
	write(win,line6,25,25,275)
	write(win,line7,25,25,300)
	write(win,line8,40,300,400)
	while True:
		pygame.time.delay(50)
		pygame.display.update()
		#screen support
		back_button.draw(win,(0,0,0))
		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()
			#get mouse position
			if event.type == pygame.MOUSEMOTION:
				if back_button.is_over(pos):
					back_button.color = (0,0,255)
				else:
					back_button.color = (255,0,0)

			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.is_over(pos):
					button_effect.play()
					return True
			if event.type == pygame.QUIT:
				return False
