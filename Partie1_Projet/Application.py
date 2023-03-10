import pygame
from arbre import AB


class App:
    def __init__(self, arbre):
        pygame.init()
        self.screen_width = 1500
        self.screen_height = 1000
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption("Arbre binaire")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 16)
        self.arbre = arbre
        self.x = self.screen_width // 2 + 100
        self.y = 50
        self.dy = self.screen_height // (self.arbre.hauteur() + 2)
        self.dx = self.screen_width // 8
        self.rayon = 20
        self.noeuds = []
        self.branches = []
        self.dessiner_arbre(self.arbre)

    def dessiner_arbre(self, arbre):
        if arbre is not None:
            valeur = arbre.getRacine()
            self.noeuds.append((valeur, self.x, self.y))
            if arbre.getGauche() is not None:
                gauche = arbre.getGauche()
                self.branches.append(
                    ((self.x, self.y + self.rayon), (self.x - self.dx, self.y + self.dy - self.rayon)))
                self.x -= self.dx
                self.y += self.dy
                self.dessiner_arbre(gauche)
                self.y -= self.dy
                self.x += self.dx
            if arbre.getDroite() is not None:
                droite = arbre.getDroite()
                self.branches.append(
                    ((self.x, self.y + self.rayon), (self.x + self.dx, self.y + self.dy + 2 - self.rayon)))
                self.x += self.dx
                self.y += self.dy
                self.dessiner_arbre(droite)
                self.y -= self.dy
                self.x -= self.dx

    def afficher(self):
        self.screen.fill((255, 255, 255))
        for valeur, x, y in self.noeuds:
            pygame.draw.circle(self.screen, (0, 0, 0), (x, y), self.rayon)
            text = self.font.render(str(valeur), True, (255, 0, 0))
            text_rect = text.get_rect(center=(x, y))
            self.screen.blit(text, text_rect)
        for debut, fin in self.branches:
            pygame.draw.line(self.screen, (0, 0, 0), debut, fin, 5)
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.afficher()
            self.clock.tick(60)
        pygame.quit()


A5 = AB(5, AB(3), AB(8))
A12 = AB(12, AB(9), AB(14))
Atest = AB(10, A5, A12)
app = App(Atest)
app.run()
