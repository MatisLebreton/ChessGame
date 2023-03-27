import pygame
from classes.pieces.piece import Piece

img_dame_blanc = pygame.image.load("img/dame_blanc.png")
img_dame_blanc = pygame.transform.scale(img_dame_blanc, (25, 50))
img_dame_noir = pygame.image.load("img/dame_noir.png")
img_dame_noir = pygame.transform.scale(img_dame_noir, (25, 50))


class Dame(Piece):
    def __init__(self, couleur, h, v):
        Piece.__init__(self, couleur, h, v)
        if couleur == "blanc":
            self.img = img_dame_blanc
        else:
            self.img = img_dame_noir

    def afficher(self, surf):
        return super().afficher(surf)
