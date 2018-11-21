# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:20:18 2018

@author: Nathan
"""

import pygame
import event_handler as EH
from pathlib import Path

image_directory = Path("PNGs")

class App(EH.Handle_Event): 
    # initialisation
    def __init__(self,*arg,**karg):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.size =self.width, self.height = 640, 400
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.green = (0,255,0)
        self.xpos_change = 0
        self.ypos_change = 0
        self.move = False
        self.hero = image_directory / 'Single_Old_Hero.png'
    # do on initialisation    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size,
                                                     pygame.HWSURFACE)
        # sets the window name
        self._running = True
        pygame.display.set_caption('A Try Force Production')
        
        # this is how I manage the frames per second
        self.clock = pygame.time.Clock()
        
        # loads the single image in to the image_surf variable
        self._image_surf = pygame.image.load(self.hero)
        self.player_xpos = self.width * .5
        self.player_ypos = self.height * .75
        return True
    
    # event handling done by my import template now
    
            
    # what to do after this event loop    
    def on_loop(self):
        pass
    
    # what to do when images render
    def on_render(self):
        self._display_surf.fill(self.white)
        self._display_surf.blit(self._image_surf, (self.player_xpos,
                                                  self.player_ypos))
        pygame.display.flip()
        
    # what to do when clearing images
    def on_cleanup(self):
        pygame.quit()
    
    def on_exit(self):
        self._running = False
    
    # what to do when exicuting the file.    
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
            
        while self._running :
            for event in pygame.event.get():
                self.on_event(event)
            
            self.player_xpos += self.xpos_change
            self.player_ypos += self.ypos_change
            pygame.display.update()
            self.clock.tick(60)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == '__main__':
    theApp = App()
    theApp.on_execute()
    
