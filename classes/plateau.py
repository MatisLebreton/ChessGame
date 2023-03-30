import pygame
import numpy as np
from classes.case import Case
from classes.pieces.piece import Piece
from classes.pieces.pion import Pion
from classes.pieces.tour import Tour
from classes.pieces.cavalier import Cavalier
from classes.pieces.fou import Fou
from classes.pieces.dame import Dame
from classes.pieces.roi import Roi


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

    def creer_pieces(self):  # Initialisation des pièces
        # Matrice regroupant toutes les pièces
        pieces = np.empty([2, 16], dtype=Piece)
        for i in range(8):
            pieces[0, i] = Pion("blanc", i+1, 2)
            pieces[1, i] = Pion("noir", i+1, 7)
        pieces[0, 8] = Tour("blanc", 1, 1)
        pieces[0, 9] = Tour("blanc", 8, 1)
        pieces[1, 8] = Tour("noir", 1, 8)
        pieces[1, 9] = Tour("noir", 8, 8)
        pieces[0, 10] = Cavalier("blanc", 2, 1)
        pieces[0, 11] = Cavalier("blanc", 7, 1)
        pieces[1, 10] = Cavalier("noir", 2, 8)
        pieces[1, 11] = Cavalier("noir", 7, 8)
        pieces[0, 12] = Fou("blanc", 3, 1)
        pieces[0, 13] = Fou("blanc", 6, 1)
        pieces[1, 12] = Fou("noir", 3, 8)
        pieces[1, 13] = Fou("noir", 6, 8)
        pieces[0, 14] = Dame("blanc", 4, 1)
        pieces[0, 15] = Roi("blanc", 5, 1)
        pieces[1, 14] = Dame("noir", 4, 8)
        pieces[1, 15] = Roi("noir", 5, 8)

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
                cases[h, v].dessiner(surf)  # Affchage des cases

        for i in range(2):
            for j in range(16):
                pieces[i, j].afficher(surf)  # Affichage des pièces
