# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 09:22:39 2018

@author: Nathan
"""
import pygame

# Was trying to make an object where we imported our png's from. Didn't go to
# plan really will come back to this if we need to / give it to one of you

class Token:
    def __init__(self):
        pass



class Player_token(Token):
    
    def __init__(self,*arg,**karg):
        self.token = pygame.image.load('./PNGs/Old Hero.png')
        self.x_loc = (app.display_width * 0.45)
        self.y_loc = (app.display_height * 0.75)
    
    def render_player(x,y,app):
        gameDisplay.blit(self.token,(x,y))
        

