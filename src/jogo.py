from configuracao import *


class Jogo:
     def __init__(self):
          self.superficie = pygame.Surface((LARGURA_JOGO, ALTURA_JOGO))
          self.mostrar_superficie = pygame.display.get_surface()
          
     def executar(self):
          # blit = block image transfer
          self.mostrar_superficie.blit(self.superficie, (ESPACAMENTO, ESPACAMENTO))     
     