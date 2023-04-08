import pygame
from classes.pieces.piece import Piece

img_tour_blanc = pygame.image.load("img/tour_blanc.png")
img_tour_blanc = pygame.transform.scale(img_tour_blanc, (25, 50))
img_tour_noir = pygame.image.load("img/tour_noir.png")
img_tour_noir = pygame.transform.scale(img_tour_noir, (25, 50))


class Tour(Piece):
    def __init__(self, couleur, h, v):
        Piece.__init__(self, couleur, h, v)
        if couleur == "blanc":
            self.img = img_tour_blanc
        else:
            self.img = img_tour_noir

    def afficher(self, surf):
        return super().afficher(surf)

    def afficherMvt(self):
        return super().afficherMvt()
