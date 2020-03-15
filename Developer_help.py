import pygame as pg
import Classes_objects

text_box_block = Classes_objects.get_button('TEXT_BOX')

def write(win,text,size,x,y):
	win.blit(((pg.font.Font('Fonts\BadaboomBB_Reg.ttf',size-6)).render(text,1,(0,0,0))),(x,y))
	return 0

def correct_card_value(card):
	'''
	Function takes card and corrects it to the right card value according to the game rules
	'''
	if card[0] in range(11,14):
		return (10,card[1])
	else:
		return card

def text_box(win):
    font = pg.font.Font('Fonts\BadaboomBB_Reg.ttf', 70)
    clock = pg.time.Clock()
    input_box = pg.Rect(250, 250, 140, 60)
    color_inactive = (0,0,255)
    color_active = (0,0,255)
    color = color_inactive
    active = True
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
                # Change the current color of the input box.
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                    	if text == '' or text == 'None' or len(text) >= 11:
                    		return 'Player1'
                    	else:
                    		return text
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        pg.draw.rect(win,(0,150,0),(0,230,1000,120),0)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        win.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(win, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)
