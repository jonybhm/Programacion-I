import pygame 
from constantes import *

class Form():
    def __init__(self):
        self.is_active = False

class FormMenu():
    def __init__(self):
        Form.__init__(self)
        self.is_active = False

class Widget(Form):
    def __init__ (self):
        Form.__init__(self)
        pass

    def render(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

class Button(Widget):
    def __init__ (self,x,y,text,screen,font_size=25):
        Widget.__init__(self)
        self.font_size = font_size
        self.font = pygame.font.Font(PATH + r"\\font\\alagard.ttf",self.font_size)
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.image_text = self.font.render(self.text,True,(255,255,255))
        self.rect = self.image_text.get_rect()
        self.rect.center = (x,y)
        self.click = False
        self.click_option_sfx = pygame.mixer.Sound(PATH +r"\\sfx\\menu_select.wav")

    def draw(self):
        
        #mostrar texto en pantalla
        self.screen.blit(self.image_text,(self.rect.x,self.rect.y))

    def button_pressed(self):
        action = False
        #posicion del mouse
        pos = pygame.mouse.get_pos()

        #colision mouse/boton
        if (self.rect.collidepoint(pos)):
            if (pygame.mouse.get_pressed()[0] == 1 and self.click == False):
                action = True
                self.click = True
                self.click_option_sfx.set_volume(0.2)
                self.click_option_sfx.play()
            if (pygame.mouse.get_pressed()[0] == 0):
                action = False
        
        return action

    def update(self):
        self.draw()
        self.button_pressed()
        




