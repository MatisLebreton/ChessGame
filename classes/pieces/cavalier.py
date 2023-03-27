import pygame
from classes.pieces.piece import Piece

img_cavalier_blanc = pygame.image.load("img/cavalier_blanc.png")
img_cavalier_blanc = pygame.transform.scale(img_cavalier_blanc, (25, 50))
img_cavalier_noir = pygame.image.load("img/cavalier_noir.png")
img_cavalier_noir = pygame.transform.scale(img_cavalier_noir, (25, 50))


class Cavalier(Piece):
    def __init__(self, couleur, h, v):
        Piece.__init__(self, couleur, h, v)
        if couleur == "blanc":
            self.img = img_cavalier_blanc
        else:
            self.img = img_cavalier_noir

    def afficher(self, surf):
        return super().afficher(surf)
