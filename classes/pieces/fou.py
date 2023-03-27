import pygame
from classes.pieces.piece import Piece

img_fou_blanc = pygame.image.load("img/fou_blanc.png")
img_fou_blanc = pygame.transform.scale(img_fou_blanc, (25, 50))
img_fou_noir = pygame.image.load("img/fou_noir.png")
img_fou_noir = pygame.transform.scale(img_fou_noir, (25, 50))


class Fou(Piece):
    def __init__(self, couleur, h, v):
        Piece.__init__(self, couleur, h, v)
        if couleur == "blanc":
            self.img = img_fou_blanc
        else:
            self.img = img_fou_noir

    def afficher(self, surf):
        return super().afficher(surf)
