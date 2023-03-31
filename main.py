import pygame
from classes.plateau import Plateau

pygame.font.init()  # Initialisation de la police d'écritures

surf = pygame.display.set_mode((600, 600))  # Créé la fenêtre
surf.fill((255, 255, 255))  # background blanc

police = pygame.font.SysFont("arial", 20)  # on fixe la police d'écriture

board = Plateau(600, 600)  # On crée l'objet plateau
cases = board.creer_cases()  # On crée l'ensemble des cases dans une matrice
pieces = board.creer_pieces()  # On crée l'ensemble des pièces


def cliquer():
    for i in range(8):
        for j in range(8):
            if pygame.Rect.collidepoint(cases[i, j].dessiner(surf), pygame.mouse.get_pos()):
                if cases[i, j].contientPiece:
                    cases[i, j].couleur = [20, 20, 20]


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # Permet de quitter en cliquant sur la croix
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Test de clic gauche souris
            cliquer()
    board.lienPiecesCases(cases, pieces)
    board.afficher(surf, cases, police, pieces)  # Affichage du plateau
    pygame.display.flip()
pygame.quit()
