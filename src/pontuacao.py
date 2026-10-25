from configuracao import *


class Pontuacao:
     def __init__(self):
          self.superficie = pygame.Surface((LARGURA_BARRA_LATERAL, ALTURA_JOGO * FRACAO_ALTURA_PONTUACAO - ESPACAMENTO))
          self.rect = self.superficie.get_rect(bottomright = (LARGURA_JANELA - ESPACAMENTO, ALTURA_JANELA - ESPACAMENTO))
          self.mostrar_superficie = pygame.display.get_surface()
          
     def executar(self):
          self.mostrar_superficie.blit(self.superficie, self.rect)     