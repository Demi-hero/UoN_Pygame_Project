import pygame as pyg

class Images:

    def __init__(self):
        self.image_directory = Path("./PNGs")


class Character (Images):
    def __init__(self):
        self.charcter = os.path.join( self.image_directory, "Single_Old_Hero.png", )


player = Character()

print(type(player.charcter))