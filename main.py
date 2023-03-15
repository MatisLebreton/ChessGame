import pygame
from classes.plateau import Plateau

pygame.font.init()  # Initialisation de la police d'écritures

surf = pygame.display.set_mode((600, 600))  # Créé la fenêtre
surf.fill((255, 255, 255))  # background blanc

police = pygame.font.SysFont("arial", 20)  # on fixe la police d'écriture

board = Plateau(600, 600)  # On crée l'objet plateau
cases = board.creer_cases()  # On crée l'ensemble des cases dans une matrice

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # Permet de quitter en cliquant sur la croix
    board.afficher(surf, cases, police)  # Affichage du plateau
    pygame.display.flip()
pygame.quit()
