import pygame
from classes.pieces.piece import Piece
from classes.case import Case

img_pion_blanc = pygame.image.load("img/pion_blanc.png")
img_pion_blanc = pygame.transform.scale(img_pion_blanc, (25, 50))
img_pion_noir = pygame.image.load("img/pion_noir.png")
img_pion_noir = pygame.transform.scale(img_pion_noir, (25, 50))


class Pion(Piece):
    def __init__(self, couleur, h, v):
        Piece.__init__(self, couleur, h, v)
        if couleur == "blanc":
            self.img = img_pion_blanc
        else:
            self.img = img_pion_noir

    def afficherMvt(self):
        self.mvtPoss = []
        if self.couleur == "blanc":
            self.mvtPoss.append(Case(self.pos_h - 1, self.pos_v))
        else:
            self.mvtPoss.append(Case(self.pos_h - 1, self.pos_v-2))
        return self.mvtPoss

    def afficher(self, surf):
        return super().afficher(surf)
