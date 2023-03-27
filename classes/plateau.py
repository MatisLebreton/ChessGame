import pygame
import numpy as np
from classes.case import Case
from classes.pieces.piece import Piece
from classes.pieces.pion import Pion


class Plateau:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur  # Taille du plateau
        self.cote_v = ["1", "2", "3", "4", "5", "6", "7", "8"]
        self.cote_h = ["A", "B", "C", "D", "E", "F",
                       "G", "H"]  # Pour afficher les côtés

    def creer_cases(self):  # On créé une matrice avec 64 Cases
        cases = np.empty([8, 8], dtype=Case)  # liste de Case
        for h in range(8):
            for v in range(8):
                cases[h, v] = Case(h, v)
        return cases

    def creer_pieces(self):
        pieces = np.empty([2, 8], dtype=Piece)
        for i in range(8):
            pieces[0, i] = Pion("blanc", i+1, 2)
            pieces[1, i] = Pion("noir", i+1, 7)
        return pieces

    def afficher(self, surf, cases, police, pieces):
        for h in range(8):
            # On écrit les cotés de l'échiqiuer
            image_texte_cote = police.render(self.cote_v[h], False, "black")
            image_texte_haut_bas = police.render(
                self.cote_h[h], False, "black")

            # Affichage gauche
            surf.blit(image_texte_cote, (20, (h+1)*cases[0, 0].largeur+10))
            # Affichage haut
            surf.blit(image_texte_haut_bas, ((h+1)*cases[0, 0].largeur+20, 10))
            # Affichage droit
            surf.blit(image_texte_cote,
                      (9*cases[0, 0].largeur+20, (h+1)*cases[0, 0].largeur+10))
            # Affichage bas
            surf.blit(image_texte_haut_bas,
                      ((h+1)*cases[0, 0].largeur+20, 9*cases[0, 0].largeur+10))

            for v in range(8):
                cases[h, v].dessiner(surf)

        for i in pieces:
            i[0].afficher(surf)

        # pieces[0, 0].afficher(surf)
