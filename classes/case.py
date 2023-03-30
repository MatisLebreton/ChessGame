import pygame


class Case:
    def __init__(self, h, v):
        self.pos_h = h
        self.pos_v = v  # Position de la case
        self.largeur = 50  # Taille des cases

        if (h+v) % 2 == 0:
            self.couleur = [100, 100, 100]
        else:
            self.couleur = 'white'

        self.estLibre = True

    def dessiner(self, surf):  # On dessine les cases
        dessin = pygame.draw.rect(surf, self.couleur, pygame.Rect(
            (self.pos_h+1)*self.largeur, (self.pos_v+1)*self.largeur, self.largeur, self.largeur))
        return dessin
