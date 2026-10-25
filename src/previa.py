from configuracao import *


class Previa:
     def __init__(self):
          self.superficie = pygame.Surface((LARGURA_BARRA_LATERAL, ALTURA_JOGO * FRACAO_ALTURA_PREVIA - ESPACAMENTO))
          self.rect = self.superficie.get_rect(topright = (LARGURA_JANELA - ESPACAMENTO, ESPACAMENTO))
          self.mostrar_superficie = pygame.display.get_surface()
          
     def executar(self):
          self.mostrar_superficie.blit(self.superficie, self.rect)     