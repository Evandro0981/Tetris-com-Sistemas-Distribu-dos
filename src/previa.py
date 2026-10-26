'''
     Este arquivo serve para representarmos a aba de prévia das peças.
'''

from configuracao import *


class Previa:
     def __init__(self):
          # Define a superficie da aba de "previa"
          self.superficie = pygame.Surface((LARGURA_BARRA_LATERAL, ALTURA_JOGO * FRACAO_ALTURA_PREVIA - ESPACAMENTO))
          '''  O retangulo é uma forma de separarmos o display, sem ele, todas as abas ficariam umas sobrepostas às outras.
               Observe que no "get_rect" informamos a posição desajada que iremos colocar essa aba, no caso, "topright", ou
               canto superior direito.'''
          self.retangulo = self.superficie.get_rect(topright = (LARGURA_JANELA - ESPACAMENTO, ESPACAMENTO))
          # Esse metodo permite com que obtenhamos o exibir_superficie, ou melhor dizendo, o display da superfície que estamos usando
          self.mostrar_superficie = pygame.display.get_surface()
          
     def executar(self):
          # O método blit serve para colocarmos uma superficie em cima de outra superficie, nesse caso "superficie" -> "mostrar_superficie"
          self.mostrar_superficie.blit(self.superficie, self.retangulo)