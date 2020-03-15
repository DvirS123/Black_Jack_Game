import pygame
import Classes_objects
import Load_image

#----------------------------------------------------------------------defining what is the menu window--------------------------------
def menu_window(win):
	'''
	Create the menu window
	'''
	win.fill((0,150,0))
	#Title
	win.blit(Load_image.get_game_img('TITLE'),(175,125))
	win.blit(((pygame.font.Font('Fonts/Beyond Wonderland.ttf',90)).render('Black', 1, (0,0,0))),(225,50))
	win.blit(((pygame.font.Font('Fonts/Beyond Wonderland.ttf',90)).render('Jack', 1, (0,0,255))),(400,100))
	win.blit(((pygame.font.Font('Fonts/BadaboomBB_Reg.ttf',24)).render('©️ This game was made by Dvir shiri', 1, (0,0,255))),(190,575))
	#------------------------- Make buttons for menu ---------------#
	Classes_objects.get_button('START').draw(win,(0,0,0))
	Classes_objects.get_button('INSTRUCTIONS').draw(win,(0,0,0))
	Classes_objects.get_button('OPTIONS').draw(win,(0,0,0))
	Classes_objects.get_button('ABOUT').draw(win,(0,0,0))