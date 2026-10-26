'''
     Este arquivo serve para representarmos a aba de pontuação do jogador.
'''

from configuracao import *


class Pontuacao:
     def __init__(self):
          # Define a superficie da aba de "pontuacao"
          self.superficie = pygame.Surface((LARGURA_BARRA_LATERAL, ALTURA_JOGO * FRACAO_ALTURA_PONTUACAO - ESPACAMENTO))
          '''  O retangulo é uma forma de separarmos o display, sem ele, todas as abas ficariam umas sobrepostas às outras.
               Observe que no "get_rect" informamos a posição desajada que iremos colocar essa aba, no caso, "bottomright", ou
               canto inferior direito.'''
          self.rect = self.superficie.get_rect(bottomright = (LARGURA_JANELA - ESPACAMENTO, ALTURA_JANELA - ESPACAMENTO))
          # Esse metodo permite com que obtenhamos o exibir_superficie, ou melhor dizendo, o display da superfície que estamos usando
          self.mostrar_superficie = pygame.display.get_surface()
          
     def executar(self):
          # O método blit serve para colocarmos uma superficie em cima de outra superficie, nesse caso "superficie" -> "mostrar_superficie"
          self.mostrar_superficie.blit(self.superficie, self.rect)     