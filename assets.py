import pygame
import gamesettings as gs

class Assets:
    def __init__(self):
        self.spritesheet = self.load_sprite_sheet("assets", "spritesheet.png", 192 * 4, 272 * 4)

    def load_sprite_sheet(self, path, filename, width, height):
        image = pygame.image.load(f"{path}/{filename}").convert_alpha()
        image = pygame.transform.scale(image, (width, height))
        return image