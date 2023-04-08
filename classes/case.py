import pygame


class Case:
    def __init__(self, h, v):
        self.pos_h = h
        self.pos_v = v  # Position de la case
        self.largeur = 50  # Taille des cases
        self.caractere = '-'

        if (h+v) % 2 == 0:
            self.couleurInit = [100, 100, 100]
        else:
            self.couleurInit = 'white'

        self.couleur = self.couleurInit

        self.contientPiece = False

    def dessiner(self, surf):  # On dessine les cases
        dessin = pygame.draw.rect(surf, self.couleur, pygame.Rect(
            (self.pos_h+1)*self.largeur, (self.pos_v+1)*self.largeur, self.largeur, self.largeur))
        return dessin
