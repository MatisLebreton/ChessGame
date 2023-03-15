import pygame
from classes.pieces.piece import Piece

img_pion_blanc = pygame.image.load("img/pion_blanc")
img_pion_noir = pygame.image.load("img/pion_noir")


class Pion(Piece):
    def __init__(self, couleur, h, v, type, img):
        Piece.__init__(couleur, h, v, "pion")
