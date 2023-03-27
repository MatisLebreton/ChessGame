import pygame
from classes.case import Case


class Piece:
    def __init__(self, couleur, h, v):
        self.couleur = couleur
        self.pos_h = h
        self.pos_v = v

    def afficher(self, surf):
        surf.blit(self.img, ((self.pos_h)*50+10, (self.pos_v)*50))
