import pygame
from classes.pieces.piece import Piece

img_pion_blanc = pygame.image.load("ChessGame/img/pion_blanc.png")
img_pion_noir = pygame.image.load("ChessGame/img/pion_noir.png")


class Pion(Piece):
    def __init__(self, couleur, h, v):
        Piece.__init__(self, couleur, h, v)
        if couleur == "white":
            self.img = img_pion_blanc
        else:
            self.img = img_pion_noir

    def afficher(self, surf):
        return super().afficher(surf)
