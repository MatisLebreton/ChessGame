import pygame


class Piece:
    def __init__(self, couleur, h, v, type, img):
        self.couleur = couleur
        self.pos_h = h
        self.pos_v = v
        self.type = type
        self.img = img
