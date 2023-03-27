import pygame
from classes.pieces.piece import Piece

img_roi_blanc = pygame.image.load("img/roi_blanc.png")
img_roi_blanc = pygame.transform.scale(img_roi_blanc, (25, 50))
img_roi_noir = pygame.image.load("img/roi_noir.png")
img_roi_noir = pygame.transform.scale(img_roi_noir, (25, 50))


class Roi(Piece):
    def __init__(self, couleur, h, v):
        Piece.__init__(self, couleur, h, v)
        if couleur == "blanc":
            self.img = img_roi_blanc
        else:
            self.img = img_roi_noir

    def afficher(self, surf):
        return super().afficher(surf)
