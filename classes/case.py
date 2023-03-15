import pygame


class Case:
    def __init__(self, h, v):
        self.pos_h = h
        self.pos_v = v  # Position de la case
        self.largeur = 50  # Taille des cases
        if (h+v) % 2 == 0:
            self.couleur = 'black'
        else:
            self.couleur = 'white'

    def dessiner(self, surf):  # On dessine les cases
        pygame.draw.rect(surf, self.couleur, pygame.Rect(
            (self.pos_h+1)*self.largeur, (self.pos_v+1)*self.largeur, self.largeur, self.largeur))
