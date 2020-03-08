import pygame 
import Classes_objects
import Sound_effects
import Developer_help
from Developer_help import write

text_box_block = Classes_objects.get_button('TEXT_BOX')
player1 = Classes_objects.get_player('PLAYER1')
vol0 = Classes_objects.get_button('VOL0')
vol1 = Classes_objects.get_button('VOL1')
vol2 = Classes_objects.get_button('VOL2')
vol3 = Classes_objects.get_button('VOL3')
vol4 = Classes_objects.get_button('VOL4')
vol5 = Classes_objects.get_button('VOL5')
vol6 = Classes_objects.get_button('VOL6')
vol7 = Classes_objects.get_button('VOL7')
vol8 = Classes_objects.get_button('VOL8')
vol9 = Classes_objects.get_button('VOL9')
vol10 = Classes_objects.get_button('VOL10')
back_button = Classes_objects.get_button('BACK')
button_effect = Sound_effects.get_sound('BUTTON')

def show_options_page(win):
	win.fill((0,150,0))
	write(win,'Options',90,230,100)
	write(win,"Enter you'r name here(1-10 charachters):",30,190,200)
	text_box_block.draw(win,(255,0,0))
	write(win,'Set music volume',30,250,370)

	while True:
		pygame.time.delay(50)
		pygame.display.update()
		#screen support
		vol0.draw(win,(0,0,0))
		vol1.draw(win,(0,0,0))
		vol2.draw(win,(0,0,0))
		vol3.draw(win,(0,0,0))
		vol4.draw(win,(0,0,0))
		vol5.draw(win,(0,0,0))
		vol6.draw(win,(0,0,0))
		vol7.draw(win,(0,0,0))
		vol8.draw(win,(0,0,0))
		vol9.draw(win,(0,0,0))
		vol10.draw(win,(0,0,0))
		back_button.draw(win,(0,0,0))
		write(win,"You'r name currently: {}".format(player1.name),30,210,325)
		if pygame.mixer.music.get_volume() == 0:
			vol0.color = (0,0,255)
		if pygame.mixer.music.get_volume() <= 0.1 and pygame.mixer.music.get_volume() > 0: 
			vol1.color = (0,0,255)
		if pygame.mixer.music.get_volume() <= 0.2 and pygame.mixer.music.get_volume() > 0.1: 
			vol2.color = (0,0,255)
		if pygame.mixer.music.get_volume() <= 0.3 and pygame.mixer.music.get_volume() > 0.2: 
			vol3.color = (0,0,255)
		if pygame.mixer.music.get_volume() <= 0.4 and pygame.mixer.music.get_volume() > 0.3: 
			vol4.color = (0,0,255)
		if pygame.mixer.music.get_volume() <= 0.5 and pygame.mixer.music.get_volume() > 0.4: 
			vol5.color = (0,0,255)
		if pygame.mixer.music.get_volume() <= 0.6 and pygame.mixer.music.get_volume() > 0.5: 
			vol6.color = (0,0,255)
		if pygame.mixer.music.get_volume() <= 0.7 and pygame.mixer.music.get_volume() > 0.6: 
			vol7.color = (0,0,255)
		if pygame.mixer.music.get_volume() <= 0.8 and pygame.mixer.music.get_volume() > 0.7: 
			vol8.color = (0,0,255)
		if pygame.mixer.music.get_volume() <= 0.9 and pygame.mixer.music.get_volume() > 0.8: 
			vol9.color = (0,0,255)
		if pygame.mixer.music.get_volume() <= 1.0 and pygame.mixer.music.get_volume() > 0.9: 
			vol10.color = (0,0,255)

		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()
			#get mouse position
			if event.type == pygame.MOUSEMOTION:

				if back_button.is_over(pos):
					back_button.color = (0,0,255)
				else:
					back_button.color = (255,0,0)

			if event.type == pygame.MOUSEBUTTONDOWN:
				if text_box_block.is_over(pos):
					player1.name = Developer_help.text_box(win)
					if player1.name == False:
						return False
				if back_button.is_over(pos):#in range of 'back' button
					button_effect.play()
					return True #back to main
				if vol0.is_over(pos):
					vol1.color = (0,0,255)
					pygame.mixer.music.set_volume(0)
				else:
					vol0.color = (255,0,0)
					
				if vol1.is_over(pos):
					vol1.color = (0,0,255)
					pygame.mixer.music.set_volume(0.1)
				else:
					vol1.color = (255,0,0)
				if vol2.is_over(pos):
					vol2.color = (0,0,255)
					pygame.mixer.music.set_volume(0.2)
				else:
					vol2.color = (255,0,0)
				if vol3.is_over(pos):
					vol3.color = (0,0,255)
					pygame.mixer.music.set_volume(0.3)
				else:
					vol3.color = (255,0,0)
				if vol4.is_over(pos):
					vol4.color = (0,0,255)
					pygame.mixer.music.set_volume(0.4)
				else:
					vol4.color = (255,0,0)
				if vol5.is_over(pos):
					vol5.color = (0,0,255)
					pygame.mixer.music.set_volume(0.5)
				else:
					vol5.color = (255,0,0)
				if vol6.is_over(pos):
					vol6.color = (0,0,255)
					pygame.mixer.music.set_volume(0.6)
				else:
					vol6.color = (255,0,0)
				if vol7.is_over(pos):
					vol7.color = (0,0,255)
					pygame.mixer.music.set_volume(0.7)
				else:
					vol7.color = (255,0,0)
				if vol8.is_over(pos):
					vol8.color = (0,0,255)
					pygame.mixer.music.set_volume(0.8)
				else:
					vol8.color = (255,0,0)
				if vol9.is_over(pos):
					vol9.color = (0,0,255)
					pygame.mixer.music.set_volume(0.9)
				else:
					vol9.color = (255,0,0)
				if vol10.is_over(pos):
					vol10.color = (0,0,255)
					pygame.mixer.music.set_volume(1.0)
				else:
					vol10.color = (255,0,0)


			if event.type == pygame.QUIT:
				return False
